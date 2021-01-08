import os
from pathlib import Path
from urllib import parse

from flask import Flask
from flask_peewee.db import Database

from app.models import all_models
from app.views import views_app

LOCAL = False

if __name__ == '__main__':
    if LOCAL:
        DATABASE = {
            'name': 'books2.db',
            'engine': 'peewee.SqliteDatabase',
        }
    else:
        url = parse.urlparse(os.environ['DATABASE_URL'])
        DATABASE = {
            'engine': 'peewee.PostgresqlDatabase',
            'name': url.path[1:],
            'user': url.username,
            'password': url.password,
            'host': url.hostname,
            'port': url.port,
        }

    app = Flask(__name__,
                static_folder=str((Path(__file__).parent / 'app' / 'static').absolute()),
                template_folder=str((Path(__file__).parent / 'app' / 'templates').absolute()))
    app.config.from_object(__name__)
    app.register_blueprint(views_app)
    db = Database(app)
    db.database.bind(all_models)
    db.database.create_tables(all_models, fail_silently=True)
    app.run(threaded=True, port=5000)
