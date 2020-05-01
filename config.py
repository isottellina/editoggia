# config.py --- 
# 
# Filename: config.py
# Author: Louise <louise>
# Created: Sat May  2 01:05:35 2020 (+0200)
# Last-Updated: Sat May  2 01:20:04 2020 (+0200)
#           By: Louise <louise>
# 
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
        'awa3&#-0xm3-g7h*rvw(=@h7@%9xd1vuo&1=&q4kja8hbvg&=j'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite://'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}