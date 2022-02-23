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

Tree structure
========
.
├── README.md
├── api
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── celery.py
│   ├── management
│   │   └── commands
│   │       ├── create_superuser.py
│   │       └── wait_for_db.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tasks
│   │   └── db_task.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
├── static
└── the_eye
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py


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