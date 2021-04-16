#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

supervisord -c /code/app/docker/supervisord.conf
