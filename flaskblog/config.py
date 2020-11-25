import os


class Config:
    SECRET_KEY = '6755b79ff83a602ad6990894b5761cb0'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'rishabdhyani4@gmail.com'
    MAIL_PASSWORD = '****'
