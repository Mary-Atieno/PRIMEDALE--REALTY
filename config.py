import os

class Config:
    SECRET_KEY='secret'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abrighthuman:bright@localhost/primedalerealty'
    SQALCHEMY_TRACK_MODIFICATIONS = True
    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    uri = os.getenv('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
        
        SQLALCHEMY_DATABASE_URI = uri
DEBUG = True


class DevConfig(Config):
         SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abrighthuman:bright@localhost/primedalerealty'

DEBUG = True

config_options={
    'development':DevConfig,
    'production':ProdConfig
}
