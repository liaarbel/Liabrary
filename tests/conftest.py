import pytest
import peewee

from app.models import all_models


@pytest.fixture(scope='function', autouse=True)
def database():
    with peewee.SqliteDatabase(':memory:', pragmas={'foreign_keys': 1}) as db, \
            db.bind_ctx(all_models):
        db.create_tables(all_models)
        yield db
