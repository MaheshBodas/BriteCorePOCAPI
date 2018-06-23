release: python manage.py makemigrations riskapi
release: python manage.py migrate
web: gunicorn BriteCorePOCAPI.wsgi --log-file