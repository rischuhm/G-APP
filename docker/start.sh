#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

certbot --nginx --agree-tos --email richard.schuhmann94@gmail.com -d mapps-leipzig.tk -d www.mapps-leipzig.tk
./manage.py migrate --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell
./manage.py collectstatic --noinput

supervisord -c /code/app/docker/supervisord.conf
