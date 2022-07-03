import os
from dotenv import load_dotenv

load_dotenv()


class DevConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    SECRET_KEY = os.getenv('SECRET_KEY')
    IP = os.getenv('IP')
    LOGIN = os.getenv('LOGIN')
    PASSWORD = os.getenv('PASSWORD')
    DATABASE_NAME = os.getenv('DATABASE_NAME')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
