#!/bin/bash
# Railway start script

echo "Starting Django application..."

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn
exec gunicorn project.wsgi --bind 0.0.0.0:$PORT --workers 2 --timeout 120 