from flask import Flask
from flask_peewee.db import Database

import os

DATABASE = {
    'name': os.environ['DATABASE_URL'],
    'engine': 'peewee.PostgresqlDatabase',
}

app = Flask(__name__, static_folder=r"C:\PythonCourse\week14\Day2\app\static")
app.config.from_object(__name__)

db = Database(app)
