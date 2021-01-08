import peewee


class User(peewee.Model):
    any_id = peewee.AutoField(null=False, primary_key=True)
    name = peewee.CharField(null=False)
    age = peewee.IntegerField(null=False)
    email = peewee.CharField(null=False, unique=True)
    phone = peewee.CharField(null=False)


class Author(peewee.Model):
    any_id = peewee.AutoField(null=False, primary_key=True)
    name = peewee.CharField(null=False)
    age = peewee.IntegerField(null=False)
    birthday = peewee.DateTimeField(null=False)
    deathdate = peewee.DateTimeField(null=True)


class Book(peewee.Model):
    any_id = peewee.AutoField(null=False, primary_key=True)
    name = peewee.CharField(null=False)
    author = peewee.ForeignKeyField(Author, unique=True)
    year = peewee.IntegerField(null=False)
    genre = peewee.CharField(null=False)


class BorrowBooks(peewee.Model):
    any_id = peewee.AutoField(null=False, primary_key=True)
    user = peewee.ForeignKeyField(User, unique=True)
    book = peewee.ForeignKeyField(Book, unique=True)


all_models = [User, Author, Book, BorrowBooks]
