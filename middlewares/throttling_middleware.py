from datetime import datetime, timedelta
from django.http import HttpResponseForbidden
from typing import Dict
from API_throttling_system.settings import API_LIMIT, TIME_GAP, API_REFERER


class APIMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.api_limit = API_LIMIT + 1
        self.time_gap = TIME_GAP
        self.requests: Dict[str, Dict[datetime, int]] = {}

    def __call__(self, request):
        if API_REFERER.lower() == 'i':
            referrer = request.META.get('REMOTE_ADDR')
        else:
            referrer = request.META.get('HTTP_REFERER')
        print(referrer)
        now = datetime.now()
        if referrer not in self.requests:
            self.requests[referrer] = {}

        counts = self.requests[referrer]
        api_in_time_difference = sum(
            counts.get(timestamp, 0) for timestamp in counts if now - timestamp < timedelta(seconds=self.time_gap))

        if api_in_time_difference >= self.api_limit:
            return HttpResponseForbidden('API limit exceeded')

        if now not in counts:
            counts[now] = 1
        else:
            counts[now] += 1

        return self.get_response(request)
