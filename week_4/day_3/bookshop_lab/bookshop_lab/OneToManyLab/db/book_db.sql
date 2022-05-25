PRAGMA FOREIGN_KEYS = ON;

DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS books;

CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR,
    last_name VARCHAR,
    age INTEGER
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR,
    genre VARCHAR,
    author_id INTEGER NOT NULL,
        FOREIGN KEY (author_id)
            REFERENCES authors (id)
);