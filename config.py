# -*- coding: utf-8 -*-
import os


class Config(object):
    SECRET_KEY = '123456790'
    SQLALCHEMY_ECHO = False
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_POOL_SIZE = 10
    #SQLALCHEMY_MAX_OVERFLOW = 5


class LocalConfig(Config):
    AMBIENTE = 'Local'
    DEBUG = True
    PORT = 5000
    DATABASE_FILE = 'basic_db.sqlite'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
