release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn project.wsgi --bind 0.0.0.0:$PORT --workers 2 --timeout 120
