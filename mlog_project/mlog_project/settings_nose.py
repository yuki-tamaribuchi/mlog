#Setting for django-nose
#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS_LIST = {
    'local':{
        '--with-xunit',
        '--xunit-file=result/unittest.xml',
    },
    'docker':{
        '--with-xunit',
        '--xunit-file=mlog_project/result/unittest.xml',
    }
}

nose_args_selection = os.environ.get('NOSE_ARGS_SELECTION', 'local')
NOSE_ARGS = NOSE_ARGS_LIST[nose_args_selection]