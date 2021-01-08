# -*- coding: utf-8 -*-
from app import database
from flask import redirect
from flask import render_template
from flask import request
from flask import Blueprint


views_app = Blueprint("views_app", __name__)


@views_app.route('/', methods=['GET'])
def home():
    return redirect('/userForm', code=302)


@views_app.route('/userForm', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form["name"]
        age = request.form["age"]
        email = request.form["email"]
        phone = request.form["phone"]

        try:
            user = database.add_user(name, age, email, phone)
            return redirect(f'/userForm/{user.any_id}', code=302)
        except Exception as e:
            empty_user = {'name': '', 'age': '', 'email': '', 'phone': ''}
            return render_template("usersForm.j2", model=empty_user, error=str(e))

    empty_user = {'name': '', 'age': '', 'email': '', 'phone': ''}
    return render_template("usersForm.j2", model=empty_user)


@views_app.route('/userForm/<int:any_id>', methods=['GET', 'POST'])
def one_user(any_id):
    model = database.get_user(any_id)

    if request.method == 'POST':
        name = request.form["name"]
        age = request.form["age"]
        email = request.form["email"]
        phone = request.form["phone"]

        try:
            database.update_user(model, name, age, email, phone)
        except Exception as e:
            return render_template("usersForm.j2", model=model, error=str(e))

    return render_template("usersForm.j2", model=model)


@views_app.route('/deleteUser/<int:any_id>', methods=['POST'])
def delete_user(any_id):
    database.delete_user(any_id)
    return redirect('/userForm', code=302)


@views_app.route('/allUsers', methods=['GET'])
def all_users():
    users = database.get_all_users()
    return render_template("allUsers.j2", users=users)


@views_app.route('/booksForm', methods=['GET', 'POST'])
def add_books():
    if request.method == 'POST':
        name = request.form["name"]
        author = request.form["author"]
        year = request.form["year"]
        genre = request.form["genre"]

        try:
            database.add_book(name, author, year, genre)
        except Exception as e:
            return render_template("booksForm.j2", error=str(e))

    empty_book = {'name': '', 'author': '', 'year': '', 'genre': ''}
    return render_template("booksForm.j2", model=empty_book)


@views_app.route('/booksForm/<int:any_id>', methods=['GET', 'POST'])
def one_book(any_id):
    model = database.get_book(any_id)

    if request.method == 'POST':
        name = request.form["name"]
        author = request.form["author"]
        year = request.form["year"]
        genre = request.form["genre"]

        try:
            database.update_user(model, name, author, year, genre)
        except Exception as e:
            return render_template("booksForm.j2", model=model, error=str(e))

    return render_template("booksForm.j2", model=model)


@views_app.route('/deleteBook/<int:any_id>', methods=['POST'])
def delete_book(any_id):
    database.delete_book(any_id)
    return redirect('/booksForm', code=302)


@views_app.route('/allBooks', methods=['GET'])
def all_books():
    books = database.get_all_books()
    return render_template("allBooks.j2", books=books)


@views_app.route('/authorsForm', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        name = request.form["name"]
        age = request.form["age"]
        birthday = request.form["birthday"]
        deathday = request.form["deathday"]

        if deathday == '':
            deathday = None

        try:
            database.add_author(name, age, birthday, deathday)
        except Exception as e:
            return render_template("authorsForm.j2", error=str(e))

    empty_author = {'name': '', 'age': '', 'birthday': '', 'deathday': ''}
    return render_template("authorsForm.j2", model=empty_author)


@views_app.route('/authorsForm/<int:any_id>', methods=['GET', 'POST'])
def one_author(any_id):
    model = database.get_author(any_id)

    if request.method == 'POST':
        name = request.form["name"]
        age = request.form["age"]
        birthday = request.form["birthday"]
        deathday = request.form["deathday"]

        try:
            database.update_user(model, name, age, birthday, deathday)
        except Exception as e:
            return render_template("authorsForm.j2", model=model, error=str(e))

    return render_template("authorsForm.j2", model=model)


@views_app.route('/deleteAuthor/<int:any_id>', methods=['POST'])
def delete_author(any_id):
    database.delete_author(any_id)
    return redirect('/authorsForm', code=302)


@views_app.route('/allAuthors', methods=['GET'])
def all_authors():
    authors = database.get_all_authors()
    return render_template("allAuthors.j2", authors=authors)


@views_app.route('/borrow', methods=['GET', 'POST'])
def borrow():
    if request.method == 'POST':
        user_id = request.form["user"]
        book_id = request.form["book"]

        try:
            database.borrow_book(user_id, book_id)
        except Exception as e:
            return render_template("borrows.j2", error=str(e))
    empty_borrow = {'user': '', 'book': ''}
    return render_template("borrows.j2", model=empty_borrow)


@views_app.route('/borrow/<int:any_id>', methods=['GET', 'POST'])
def one_borrow(any_id):
    model = database.get_borrow(any_id)

    if request.method == 'POST':
        user = request.form["user"]
        book = request.form["book"]

        try:
            database.update_user(model, user, book)
        except Exception as e:
            return render_template("borrows.j2", model=model, error=str(e))

    return render_template("borrows.j2", model=model)


@views_app.route('/deleteBorrow/<int:any_id>', methods=['POST'])
def delete_borrow(any_id):
    database.delete_borrow(any_id)
    return redirect('/borrow', code=302)


@views_app.route('/allBorrows', methods=['GET'])
def all_borrows():
    borrows = database.get_all_borrows()
    return render_template("allBorrows.j2", borrows=borrows)
