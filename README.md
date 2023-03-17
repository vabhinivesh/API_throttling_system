## API throttling system

* Create a virtual environment.

`python -m virtualenv venv`

* Activate the virtual environment.

`venv\Scripts\activate`

* Install dependencies by 

`pip install -r requirements.txt`

* After installing all the dependencies run the server using

`python manage.py runserver`

* The pending migrations error(if any)  can be fixed by executing

`python manage.py migrate`

* Open the running server by going to http://127.0.0.1:8000/ on browser
* You can try the API throttling by clicking multiple times the GET button.
* Once, the API reaches the threshold limit. there will be a forbidden error with a message 'API limit exceeded'.
* The API will be re-enabled once the TIME_GAP period is over. 
* The application is hosted at https://django.abhinivesh.online/

##### For changing Limit and time:
We can update the limit and time by updating the settings file. 

* API_LIMIT = 10 - No of api's allowed before throttling
* TIME_GAP = 60 - Time in seconds to check throttling


### Plan and future enhancements:

For a Django  application we can either use a decorator, or a middleware for checking the rate of the request. 
##### Here I used a middleware because the functionality automatically adds to all the Url's we create.

When we scale the application we can use the same function and wrap it using a simple flask application or a fast api app (or use node or golang) and use the same code as a microservice.
This microservice will be placed in front of the actual application and checks the incoming requests before hitting the actual server.
