import pytest
import peewee

from app.models import Book, Author


class TestBookDb(object):

    @pytest.fixture(scope='function')
    def author(self):
        return Author.create(
            name='bla',
            age=12,
            birthday="08/01/1971"
        )

    def test_insert_book_with_username_select_finds(self, author):
        book = Book.create(
            name="Harry Potter",
            author=author,
            year=1991,
            genre="fantasy"
        )
        search = Book.get(Book.name == book.name)
        assert search.author == book.author
        assert search.year == book.year
        assert search.genre == book.genre
