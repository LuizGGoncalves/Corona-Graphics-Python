import os, random, string


class Config(object):
    CRSF_ENABLE = True
    SECRET = "seguro"
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template')
    Root_Dir = os.path.dirname(os.path.abspath(__file__))
    APP = None


class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_Host = 'Local host'
    PORT_HOST = 8000
    URL_MAIN = 'https//%s/%s' % (IP_Host, PORT_HOST)
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost:3306/csv'

app_config = {
    'dev': DevelopmentConfig(),
    'testing': None,
    'production': None}

app_active = 'dev'

if app_config is None:
    app_config = 'dev'
