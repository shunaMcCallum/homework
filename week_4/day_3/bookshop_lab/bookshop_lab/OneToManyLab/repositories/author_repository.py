from db.run_sql import run_sql
from models.authors import Author
from models.books import Book

# SAVE/CREATE METHOD
def save(author):
    sql = "INSERT INTO authors (first_name, last_name, age) VALUES (?, ?, ?) RETURNING *"
    values = [author.first_name, author.last_name, author.age]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author


# SELECT ALL METHOD
def select_all():
    authors = []
    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['first_name'], row['last_name'], row['age'], row['id'])
        authors.append(author)
    return authors

# SELECT ONE METHOD
def select_one(id):
    author = None
    sql = "SELECT * FROM authors where id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = Author(result['first_name'], result['last_name'], result['age'], result['id'])
    return author

# DELETE ALL METHOD
def delete_all():
    sql = "DELETE  FROM authors"
    run_sql(sql)


# DELETE ONE METHOD
def delete(id):
    sql = "DELETE  FROM authors WHERE id = ?"
    values = [id]
    run_sql(sql, values)


# UPDATE/EDIT METHOD
def update(author):
    sql = "UPDATE authors SET (first_name, last_name, age) = (?, ?, ?) WHERE id = ?"
    values = [author.first_name, author.last_name, author.age, author.id]
    run_sql(sql, values)