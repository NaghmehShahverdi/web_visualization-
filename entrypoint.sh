#!/bin/sh

mkdir -p static
python manage.py makemigrations app users --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

if [[ "$PRODUCTION" == "True" ]]; then
    gunicorn --bind :${APP_PORT} --workers=2 --threads=2 --worker-class=sync mces.wsgi:application
else
    python manage.py runserver mces-app:${APP_PORT}
fi
