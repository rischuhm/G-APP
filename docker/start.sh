#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'


certbot --nginx --agree-toos --email richard.schuhmann94@gmail.com -d mapps-leipzig.tk -d www.mapps-leipzig.tk
./manage.py migrate --noinput
./manage.py collectstatic --noinput

supervisord -c /code/app/docker/supervisord.conf
