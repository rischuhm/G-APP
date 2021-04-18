FROM python:3.8-buster

RUN mkdir -p /code/app
WORKDIR /code/app

ADD requirements.txt /code/app/

RUN pip install -r requirements.txt \
 && pip install gunicorn \
 && pip install supervisor

RUN apt-get update \
 && apt-get install -y nginx

ADD docker/nginx.conf /etc/nginx/nginx.conf

ADD docker/start.sh /bin/start.sh
RUN chmod +x /bin/start.sh

ADD . /code/app

CMD ["/bin/start.sh"]
