import pytest
import peewee

from app.models import Author


class TestUserDb(object):
    def test_insert_author_with_username_select_finds(self):
        author = Author.create(
            name="Rick",
            age=50,
            birthday="08/01/1971"
        )
        search = Author.get(Author.name == author.name)
        assert search.age == author.age
        assert search.birthday == author.birthday
