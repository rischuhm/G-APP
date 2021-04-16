FROM quay.io/bitnami/python:3.8-prod

RUN mkdir -p /code/app
ADD . /code/app

WORKDIR /code/app

RUN pip install -r requirements.txt

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]