from flask import Flask, render_template, request, redirect
from repositories import book_repository, author_repository
from models.books import Book

from flask import Blueprint

books_blueprint = Blueprint("books", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/books'
@books_blueprint.route("/books")
def tasks():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)


# NEW
# GET '/books/new'
@books_blueprint.route("/books/new", methods=['GET'])
def new_book():
    author = author_repository.select_all()
    return render_template("books/new.html", authors = author)


# CREATE
# POST '/books'
@books_blueprint.route("/books", methods=['POST'])
def create_book():
    title = request.form['title']
    genre = request.form['genre']
    author_id = request.form['author_id']
    
    author = author_repository.select_one(author_id)
    book = Book(title, genre, author)

    book_repository.save(book)
    return redirect('/books')

# SHOW
# GET '/books/<id>'
@books_blueprint.route("/books/<id>", methods=['GET'])
def show_book(id):
    book = book_repository.select_one(id)
    return render_template("/books/show.html", book=book)


# EDIT
# GET '/books/<id>/edit'
@books_blueprint.route("/books/<id>/edit", methods=['GET'])
def edit_book(id):
    book = book_repository.select_one(id)
    authors = author_repository.select_all()
    return render_template("books/edit.html", book=book, all_authors=authors)


# UPDATE
# PUT '/books/<id>'
@books_blueprint.route("/books/<id>", methods=['POST'])
def update_book(id):
    title = request.form['title']
    genre = request.form['genre']
    author_id = request.form['author_id']
    
    author = author_repository.select(author_id)
    book = Book(title, genre, author, id)

    book_repository.update(book)
    return redirect ("/books")

# DELETE
# DELETE '/books/<id>'
@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect ("/books")