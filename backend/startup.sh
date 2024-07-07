#!/bin/sh

# Wait for MySQL to be ready
until nc -z -v -w30 db 3306
do
  echo 'Waiting for MySQL connection...'
  sleep 5
done

# Apply migrations or other setup tasks here
# Example: python manage.py migrate

# Start Gunicorn server
exec gunicorn base.wsgi:application --bind 0.0.0.0:8000
