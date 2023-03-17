# API throttling system

* Create a virtual environment.

`python -m virtualenv venv`

* Activate the virtual environment.

`venv\Scripts\activate`

* Install dependencies by 

`pip install -r requirements.txt`

* After installing all the dependencies run the server using

`python manage.py runserver`

* Open the running server by going to http://127.0.0.1:8000/ on browser
* You can try the API throttling by clicking multiple times the GET button.
* Once, the API reaches the threshold limit. there will be a forbidden error with a message 'API limit exceeded'. 
