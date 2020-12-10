import os
from pathlib import Path
from urllib import parse

from flask import Flask
from flask_peewee.db import Database

url = parse.urlparse(os.environ['DATABASE_URL'])
DATABASE = {
    'engine': 'peewee.PostgresqlDatabase',
    'name': url.path[1:],
    'user': url.username,
    'password': url.password,
    'host': url.hostname,
    'port': url.port,
}

app = Flask(__name__, static_folder=str((Path(__file__).parent / 'static').absolute()))
app.config.from_object(__name__)

db = Database(app)

# noinspection PyUnresolvedReferences
# So that app can recognize the views
from app import views
