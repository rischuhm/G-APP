#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

./manage.py migrate --noinput
./manage.py collectstatic --noinput

supervisord -c /code/app/docker/supervisord.conf
