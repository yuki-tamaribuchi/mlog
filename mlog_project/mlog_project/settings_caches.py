import os

CACHES={
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'select2_local':{
        'BACKEND':'django_redis.cache.RedisCache',
        'LOCATION':'redis://127.0.0.1:6379/2',
        'OPTIONS':{
            'CLIENT_CLASS':'django_redis.client.DefaultClient',
        }
    },
    'select2_docker':{
        'BACKEND':'django_redis.cache.RedisCache',
        'LOCATION':'redis://redis:6379/2',
        'OPTIONS':{
            'CLIENT_CLASS':'django_redis.client.DefaultClient',
        }
    },
    'select2_elasticache':{
        'BACKEND':'django_redis.cache.RedisCache',
        'LOCATION':'redis://'+os.environ.get('MLOG_AWS_ELASTICACHE_DNS', ''),
        'OPTIONS':{
            'CLIENT_CLASS':'django_redis.client.DefaultClient',
        }
    }
}

CACHES['select2']=CACHES[os.environ.get('SELECT2_DEFAULT','select2_local')]

SELECT2_CACHE_BACKEND='select2'