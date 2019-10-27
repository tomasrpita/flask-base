import os


class Config(object):
    SECRECT_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    