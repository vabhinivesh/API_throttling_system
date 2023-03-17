import requests


def test_api():
    url = "http://127.0.0.1:8000/"
    headers = {"Content-Type": "application/json"}

    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert response.json() == {'message': 'API success'}
