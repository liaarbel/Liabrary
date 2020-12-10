from flask import Flask

from flask_peewee.db import Database

DATABASE = {
    'name': 'books2.db',
    'engine': 'peewee.SqliteDatabase',
}

app = Flask(__name__, static_folder=r"C:\PythonCourse\week14\Day2\app\static")
app.config.from_object(__name__)

db = Database(app)
