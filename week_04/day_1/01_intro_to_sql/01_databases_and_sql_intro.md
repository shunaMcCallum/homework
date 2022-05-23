# Databases and SQL Introduction

### Objectives

 - Understand what a database is
 - Explain what SQL is
 - Know how to use CRUD
 - Know how to create relationships

## Intro

Last week we were building websites where we could enter data and that data was sent from the browser to our controllers running on a server. Our controllers could use that data which was sent from the browswer, but what if the program running our controller had to be restarted e.g. if the machine it was running on crashed - we would lose all our data. Could you imagine if we were running an e-commerce website and we lost all the data regarding our stock, orders, customers etc - that would not be nice :-( 

Wouldn't it be great, therefore, if there was some way we could store the data which our web application needs (e.g. the details entered by a customer) in such a way that, if we needed to restart our server then we can easily get it all back. This is where databases come in. 

## What is a database?

A database is just somewhere for us to store our data. There are many different shapes and sizes of database. SQL is a language which is often used to query these databases and that's what we will be learning today.

## What do we do with databases

What do we store in databases?
> Get the students to make some suggestions

> Ensure you write the "CRUD" operations on the board under each other as the class suggest them, to read the acronym off vertically. Later, we will align these with the SQL commands written next to them.

 What sorts of manipulations do we make to data in databases?

 - Create (we can't do anything unless we can put data in)
 - Read (once it's in there, we need to get it out)
 - Update (if it needs to change, we need to be able to change it)
 - Delete (we'll need to be able to remove data from our database)

We refer to these four operations as "CRUD". This is important since you will come across it later when we begin web programming

> As you work through the sql commands, tick these off.

## What is SQL?

"SQL" stands for "Structured Query Language" (pronounced either as "ess-queue-ell" or "sequel"). In the same way that we use Python to talk to the computer, we can use SQL to talk to a database.

## SQLite

SQL is just a language - we need an engine to run it on. In the same way that Python is just a language, that runs on an "interpreter" - our Python robot we spoke about before.

SQLite is an in-memory database system that we will be using on the course. It is small and comes pre-installed on our Macbooks.

To check that SQLite is installed, we can type this.

```bash
# terminal
which sqlite3
```

```bash
# terminal
sqlite3
```

To quit the sqlite3 terminal

```sql
-- sqlite3 terminal
.quit
```

## Structure

In SQL, a database is a collection of "tables". A table is a collection of "columns" and "rows".

A table describes the type of item that we want to store. A column represents some information we might find interesting about that item. A row is the physical data we want to save.

> Draw this on the board

For example, we might have a `zoo` database with a table called `animals`. The `animals` table might have the columns `name`, `age` and `species`. The `animals` table would then have rows of data like:

| `name` | `age` | `species` |
| --- | --- | --- |
| Leo | 12 | Lion |
| Tony | 8 | Tiger |

Note: a column is sometimes referred to as a field, but they mean the exact same thing.

## Data Types

So before we run off and create lots of shiny tables, we need to talk about datatypes. You'll be glad to hear they roughly match up to what we have already seen in Python. There are many data types we can use in SQL - the most common we will be using are:

* VARCHAR -  text (string)
* INTEGER - numerical data (integer)
* BOOLEAN - true/false data (trueclass, falseclass, booleans)

# Creating tables

By convention, we will name our database tables as the plural of the thing we are creating. So rows of animal data would be stored in a table called Animals. Sheep would be stored in a table called... well, sheep.

Let's make a table that's going to store data about Star Wars characters. A character might have the following attributes:

- name
- darkside (true / false)
- age

> Get the students to think about what types these columns will be.

Before we create a table, we will drop it so that we can run our script multiple times. SQLite won't let you create a table that already exists.

```bash
# terminal
touch star_wars.sql
```

We can use the following template every time we create a new database table:

```sql
DROP TABLE table_name;

CREATE TABLE table_name (
  column_name1 DATA_TYPE,
  column_name2 DATA_TYPE,
  column_name3 DATA_TYPE
)

```

So, in our case, it would look like this:

```sql
-- star_wars.sql
DROP TABLE characters;

CREATE TABLE characters (
  name VARCHAR,
  darkside BOOLEAN,
  age INTEGER
);
```

- What is our table called?
- What are the names of our columns?
- What are the size constraints?

There is a special command that we can run from the terminal to run our SQL scripts on our SQLite database.

```bash
# terminal
sqlite3 star_wars.db < star_wars.sql
```

As we are using SQLite3, this will create file for our database, called `star_wars.db` in our working directory.

> With other database engines, e.g. Postgresql, you need to have created the database before running any scripts on it.

We will write all of our statements in the one file and comment them out, so you can keep the story of what we are working through.


## Creating (-C-rud)

> Remember to tick off the CRUD items on the board

We're going to start with the C in CRUD but first let's learn the SQL statement that you'll probably use most of all.

```sql
-- star_wars.sql
SELECT * FROM characters;
```

> You may want to comment out select statements as you go, so only the latest one is shown, or just keep moving the select down the script as we go.

This says "get everything from the characters table." The `*` means 'all the fields'.

To "create" records in SQL, we use the `INSERT` clause.

We are going to make a lot of use of the Atom shortcuts `cmd` + `shift` + `d` to duplicate a line as well as `cmd` + `/` to comment a line.

The template for creating entries is the following:

```sql
INSERT INTO table_name (column_name1, column_name2) VALUES (value1, value2);
```

Let's create some characters!

```sql
-- star_wars.sql
-- REMEMBER SEMI COLONS!
-- We're going for prequel-era Star Wars here
INSERT INTO characters (name, darkside, age) VALUES ('Obi-Wan Kenobi', false,  27);
INSERT INTO characters (name, darkside, age) VALUES ('Anakin Skywalker', false, 19);
INSERT INTO characters (name, darkside, age) VALUES ('Darth Maul', true, 32);

SELECT * FROM characters;
```

```bash
# terminal
sqlite3 star_wars.db < star_wars.sql
```

We need to be careful with quotation marks in SQL - we should always use single quotes. Single quotes behave in the normal way we'd expect - defining text. Double quotes are reserved for system operations. Try not to worry too much about this, just remember to use single quotes when dealing with data.

> Sqlite3 has no real boolean value. True is stored as '1' and False is stored as '0'

If we ever need to use a quotation mark or apostrophe in our inserted text, we need to escape it with a backslash or use two of them.

We use the convention uppercase for SQL keywords and lowercase for our own terms. It's not mandatory but it makes it easier to read.

## Formatting

The output from running the command is:

```
Obi-Wan Kenobi|0|27
Anakin Skywalker|0|19
Darth Maul|1|32
```

Wouldn't it be nice to have the column headings so we can see the column names and have them spaced out evenly. We can do this by adding the following two lines at the top of the

```sql
--star_wars.sql

.headers ON -- ADDED
.mode column -- ADDED

DROP TABLE characters;
```

> If you wish to use a GUI to look at your database you can download and install a program called DB Browser for SQLite from [here](https://sqlitebrowser.org/dl/)

## Inserting nulls

What would happen if we do this?

```sql
-- star_wars.sql
INSERT INTO characters (name, darkside) VALUES ('Yoda', false);
```

```sql
-- star_wars.sql
SELECT * FROM characters
```

```bash
# terminal
sqlite3 star_wars.db < star_wars.sql
```

Notice that the value for age is blank, as we have not given it a value. Any values which are not passed in are set to null.

## Selecting (c-R-ud)

This is the R is CRUD.

We have been "reading" records with the `SELECT` clause.

```sql
-- star_wars.sql
SELECT * FROM characters;
```

The star is saying that we want all the fields returned, if we said:

```sql
-- star_wars.sql
SELECT name FROM characters;
```

...it would only list the names.

We can also use `SELECT` to count how many rows we have

```sql
-- star_wars.sql
SELECT COUNT(*) FROM characters;
```

# Updating (cr-U-d)

This is the U in CRUD.

We use the `UPDATE` clause to change the values in existing records.

Template:
```sql
UPDATE table_name SET column_name1 = new_value1;
```

Let's update the darkside column to true!

```sql
-- star_wars.sql
UPDATE characters SET darkside = true;
```

```bash
# terminal
sqlite3 star_wars.db < star_wars.sql
```

This has updated all our records (3 of them)... what if we only want certain records to update?

We can use a `WHERE` clause to achieve this.

```sql
-- star_wars.sql
UPDATE characters SET darkside = true WHERE name = 'Anakin Skywalker';
```

```bash
# terminal
sqlite3 star_wars.db < star_wars.sql
```

We can even update more than one field at a time! This, however, uses a different syntax. When we select multiple columns to update, we have to put them in brackets, and we have to do the same when we give it the values we want to use. Remember, just like with Insert, order matters!

Template:

```sql
UPDATE table_name SET (column_name1, column_name2) = (new_value1, new_value2) WHERE column_name = target_value;
```

Let's update Anakin according to Star Wars lore!

```sql
-- Change the line you just wrote:
UPDATE characters SET (name, darkside) = ('Darth Vader', true) WHERE name = 'Anakin Skywalker';
```

```bash
# terminal
sqlite3 star_wars.db < star_wars.sql
```

> [TASK:]
- Add a new character "Luke Skywalker" with age 17 and darkside set to false.
- Update "Obi-Wan Kenobi" to be age 65

```sql
-- star_wars.sql
INSERT INTO characters (name, darkside, age) VALUES ('Luke Skywalker', false, 17);
UPDATE characters SET age = 65 WHERE name = 'Obi-Wan Kenobi';
```


# Deleting (cru-D-)

This is the D in CRUD.

To delete records we use the `DELETE` clause. But **be careful**, there's no undo! When a record is deleted from a DB it's gone for ever. "Undelete" in the database world is "restore from last night's backup" (if there *was* a backup...)

Template:
```sql
DELETE FROM table_name WHERE column_name = target_value;
```

**SPOILERS** Let's delete Darth Maul

```sql
-- star_wars.sql
DELETE FROM characters WHERE name = 'Darth Maul';
SELECT * FROM characters;
```

**WARNING**: If you don't specify the row(s) with a WHERE clause, it will delete *everything* from that table!

```sql
DELETE FROM characters; -- DELETES EVERYTHING FROM CHARACTERS
```

```bash
# terminal
sqlite3 star_wars.db < star_wars.sql
```

[Task:] Add a character and then delete it

# Uniquely identifying rows

What happens if we had several characters with the same data in every field? It's unlikely but it could happen.

```sql
-- star_wars.sql

INSERT INTO characters (name, darkside, age) VALUES ('Stormtrooper', true, 25);
INSERT INTO characters (name, darkside, age) VALUES ('Stormtrooper', true, 25);
INSERT INTO characters (name, darkside, age) VALUES ('Stormtrooper', true, 25);
INSERT INTO characters (name, darkside, age) VALUES ('Stormtrooper', true, 25);
INSERT INTO characters (name, darkside, age) VALUES ('Stormtrooper', true, 25);
```

```bash
# terminal
sqlite3 star_wars.db < star_wars.sql
```

So it's a Stormtrooper's birthday today! But how can we uniquely identify him in the database to update his age?

We can't. We have no way of uniquely identifying this row, and any query we try to execute will update all the Stormtroopers.

Oops.

What we need is some way of uniquely identifying each row in the table. We do this my setting aside a column which will have a unique value for each row in the table. This column is know as the **primary key**.

The answer to this is to add a column to every table when we create it. That column will contain a number, which will be unique for each row in the database, and ideally is managed by the database itself, so we don't need to worry about adding it when we insert new records.
 

## Primary Keys

We are going to add an `id` column to our `characters` table which will be the primary key for the table. So that SQLite knows that this column is the primary key then we add `PRIMARY KEY` after the type of the column when creating our table.

A primary key is a column that uniquely defines a record. A primary key column cannot contain a NULL value. A table can have only one primary key. So we are explicitly saying that we want our ID field to be our main identifier for the rows in the table.

When thinking of what type we want to use as our primary key, we want it to be something unique. It makes sense to use `INTEGER` for this as we can give each row a unique number for its `id`. But how do we make sure that the number is always unique? It would be great if there was some way we could get the database to generate a unique number automatically, so that we don't have to worry about what the `id` should be when adding a new row. It would make sense to start at `1` for the `id` of the first row, `2` for the second, and so on. SQLite has an `AUTOINCREMENT` property which we can apply to a column. This means that, when creating a row, we let SQLite generate the value for that column, and it will increment by 1 each time - great!

Note that different database engines handle this in different ways.

Let's update our characters to add the `id` column. It will be of type `INTEGER`, will be the `PRIMARY KEY` and will be `AUTOINCREMENT`ed.

```sql
-- star_wars.sql

CREATE TABLE characters (
  id INTEGER PRIMARY KEY AUTOINCREMENT, -- ADDED
  name VARCHAR(255),
  darkside BOOLEAN,
  age INT
);
```

If we run our script now we should see something cool. Each of our entries magically has a unique id, and we didn't need to do anything to manage it.

Now we have an easier time differentiating between our Stormtroopers!

Let's update one of them to be a bit older than 25!

```sql
UPDATE characters SET age = 29 WHERE id = 9;
```

Our next step is figuring out how to add lightsabers to our characters!
