import datetime

from app.models import Author, Book, BorrowBooks, User


def get_all_books():
    return Book.select()


def get_book(any_id):
    return Book.get_by_id(any_id)


def add_book(name, author, year, genre):
    Book.create(name=name, author=author, year=year, genre=genre)


def update_book(book, name, author, year, genre):
    book.name = name
    book.author = author
    book.year = year
    book.genre = genre
    book.save()


def delete_book(any_id):
    book = get_book(any_id)
    book.delete_instance()


def get_all_authors():
    return Author.select()


def get_author(any_id):
    return Author.get_by_id(any_id)


def add_author(name, age, birthday, deathday=None):  # yyyy-mm-dd
    print(birthday, deathday)
    FORMAT = '%Y-%m-%d'
    birthday = datetime.datetime.strptime(birthday, FORMAT).date()
    if deathday is not None:
        deathday = datetime.datetime.strptime(deathday, FORMAT).date()
    Author.create(name=name, age=age, birthday=birthday, deathday=deathday)


def update_author(author, name, age, birthday, deathday=None):
    author.name = name
    author.age = age
    author.birthday = birthday
    author.deathdate = deathday
    author.save()


def delete_author(any_id):
    author = get_author(any_id)
    author.delete_instance()


def get_all_users():
    return User.select()


def get_user(any_id):
    return User.get_by_id(any_id)


def add_user(name, age, email, phone):
    return User.create(name=name, age=age, email=email, phone=phone)


def update_user(user, name, age, email, phone):
    user.name = name
    user.age = age
    user.email = email
    user.phone = phone
    user.save()


def delete_user(any_id):
    user = get_user(any_id)
    user.delete_instance()


def get_all_borrows():
    return BorrowBooks.select()


def get_borrow(any_id):
    return BorrowBooks.get_by_id(any_id)


def borrow_book(user, book):
    BorrowBooks.create(user=user, book=book)


def update_borrow(borrow, user, book):
    borrow.user = user
    borrow.book = book
    user.save()


def delete_borrow(any_id):
    borrow = get_borrow(any_id)
    borrow.delete_instance()
