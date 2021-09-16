CELERY_BROKER_URLS={
    'local':"redis://127.0.0.1:6379/1",
    'docker':"redis://redis:6379"
}

CELERY_BROKER_URL = CELERY_BROKER_URLS[os.environ.get('CELERY_BROKER_DEFAULT','local')]

CELERY_RESULT_BACKENDS={
    'local':"redis://127.0.0.1:6379",
    'docker':"redis://redis:6379"
}

CELERY_RESULT_BACKEND = CELERY_RESULT_BACKENDS[os.environ.get('CELERY_RESULT_BACKENDS_DEFAULT','local')]

CELERY_TIMEZONE = "Asia/Tokyo"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60