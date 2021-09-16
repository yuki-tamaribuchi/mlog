EMAIL_BACKEND = 'django_ses.SESBackend'

AWS_SES_ACCESS_KEY_ID = os.environ.get('MLOG_AWS_SES_ACCESS_KEY_ID')
AWS_SES_SECRET_ACCESS_KEY = os.environ.get('MLOG_AWS_SES_SECRET_ACCESS_KEY')

AWS_SES_REGION_NAME = 'ap-northeast-1'
AWS_SES_REGION_ENDPOINT = 'email.ap-northeast-1.amazonaws.com'
DEFAULT_FROM_EMAIL = os.environ.get('MLOG_DEFAULT_FROM_EMAIL')