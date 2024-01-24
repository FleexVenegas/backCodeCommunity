from decouple import config

class Config:
    SECRET_KEY = config("SECRET_KEY")

class DevelopmentConfig(Config):
    DEBUG = True
    # MYSQL_HOST = config('MYSQL_HOST')
    # MYSQL_USER = config('MYSQL_USER')
    # MYSQL_PASSWORD = config('MYSQL_PASSWORD')
    # MYSQL_DATABASE = config('MYSQL_DATABASE')


config={
    'development': DevelopmentConfig
}