THE EYE REST API
===
This API is developed with DRF and use JWT for user authentication

Description
=======
The API can be executed with docker-compose. It has the following services:

- app: The main django app, it migrates the database when the service starts and create a superuser. It queue the events using celery
- celery: The worker app, it inserts the data received from the main app.
- db: The mysql database for the app.
- redis: The redis server used for queue jobs.

It's built with Python 3.9 and Django 4.0

Docker services for development
=========
The app services runs in 8000 port
```
    # Run all services
    docker-compose up --build -d
``` 

API documentation
=========
The API documentation can be found in http://127.0.0.1:8000/docs/ or http://127.0.0.1:8000/swagger/

In order to create an event it is needed to create first the application and the session. For that purpose it's mandatory to create the JWT token and the send it to the next API calls.

A postman collection is provided to test the API.

The order of execution of the methods is:

1. authenticate
2. create_application
3. create_session
4. create_event
5. get_event_sessions

When an application is created it is assigned to the current user and only this user have permission to send events for this application.