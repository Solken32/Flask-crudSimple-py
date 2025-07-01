import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/inventarioflask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
