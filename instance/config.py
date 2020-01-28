import os

basedir = os.path.abspath(os.path.dirname(__file__))


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_SCHEMA = os.getenv("DB_SCHEMA")

DB_URI = "mysql+pymysql://{}:{}@{}/{}".format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_SCHEMA
)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
