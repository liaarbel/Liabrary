from flask import Flask
from flask_peewee.db import Database

from urllib import parse
import os

url = parse.urlparse(os.environ['DATABASE_URL'])
DATABASE = {
    'engine': 'peewee.PostgresqlDatabase',
    'name': url.path[1:],
    'user': url.username,
    'password': url.password,
    'host': url.hostname,
    'port': url.port,
}

app = Flask(__name__, static_folder=r"C:\PythonCourse\week14\Day2\app\static")
app.config.from_object(__name__)

db = Database(app)

from app import views
