import os

class Config:
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    CONTENT_TRUNCATE = 1000