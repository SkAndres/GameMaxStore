web: gunicorn GameMax.wsgi:application --log-file - --log-level debug
python manage.py static --noinput
manage.py migrate