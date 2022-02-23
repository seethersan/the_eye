FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apt-get install -y default-libmysqlclient-dev

RUN pip install -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput