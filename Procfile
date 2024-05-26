web: gunicorn newsletter_service.wsgi --log-file -
worker: celery -A newsletter_service worker --loglevel=info