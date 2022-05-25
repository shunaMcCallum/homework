from db.run_sql import run_sql
from models.authors import Author
from models.books import Book
import repositories.author_repository as author_repository

# SAVE/CREATE METHOD
def save(book):
    sql = "INSERT INTO books (title, genre, author_id) VALUES (?, ?, ?) RETURNING *"
    values = [book.title, book.genre, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book


# SELECT ALL METHOD
def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select_one(row['author_id'])
        book = Book(row['title'], row['genre'], author, row['id'] )
        books.append(book)
    return books


# SELECT ONE METHOD
def select_one(id):
    book = None
    sql = "SELECT * FROM books WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository.select_one(result['author_id'])
        book = Book(result['title'], result['genre'], author, result['id'] )
    return book


# DELETE ALL METHOD
def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)


# DELETE ONE METHOD
def delete(id):
    sql = "DELETE  FROM books WHERE id = ?"
    values = [id]
    run_sql(sql, values)


# UPDATE/EDIT METHOD
def update(book):
    sql = "UPDATE books SET (title, genre, author_id) = (?, ?, ?) WHERE id = ?"
    values = [book.title, book.genre, book.author.id, book.id]
    run_sql(sql, values)
