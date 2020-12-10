from app import db

import peewee


class User(db.Model):
    any_id = peewee.PrimaryKeyField(null=False, primary_key=True)
    name = peewee.CharField(null=False)
    age = peewee.IntegerField(null=False)
    email = peewee.CharField(null=False, unique=True)
    phone = peewee.CharField(null=False)


class Author(db.Model):
    any_id = peewee.PrimaryKeyField(null=False, primary_key=True)
    name = peewee.CharField(null=False)
    age = peewee.IntegerField(null=False)
    birthday = peewee.DateTimeField(null=False)
    deathdate = peewee.DateTimeField(null=True)


class Book(db.Model):
    any_id = peewee.PrimaryKeyField(null=False, primary_key=True)
    name = peewee.CharField(null=False)
    author = peewee.ForeignKeyField(Author, unique=True)
    year = peewee.IntegerField(null=False)
    genre = peewee.CharField(null=False)


class BorrowBooks(db.Model):
    any_id = peewee.PrimaryKeyField(null=False, primary_key=True)
    user = peewee.ForeignKeyField(User, unique=True)
    book = peewee.ForeignKeyField(Book, unique=True)


db.database.create_tables([User, Author, Book, BorrowBooks], fail_silently=True)
