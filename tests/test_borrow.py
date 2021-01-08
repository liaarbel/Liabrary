import pytest
import peewee

from app.models import BorrowBooks, Book, Author, User


class TestBorrowDb(object):
    @pytest.fixture(scope='function')
    def user(self):
        return User.create(
            name='bla',
            age=12,
            email="mashu@gmail.com",
            phone="056-145697"
        )

    @pytest.fixture(scope='function')
    def author(self):
        return Author.create(
            name='bla',
            age=12,
            birthday="08/01/1971"
        )

    @pytest.fixture(scope='function')
    def book(self, author):
        return Book.create(
            name='bla',
            author=author,
            year=1971,
            genre="drama"
        )

    def test_insert_book_with_user_select_finds(self, user, book):
        borrow = BorrowBooks.create(
            user=user,
            book=book
        )
        search = BorrowBooks.get(BorrowBooks.user == borrow.user)
        assert search.book == borrow.book
