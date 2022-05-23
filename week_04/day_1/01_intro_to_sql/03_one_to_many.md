## Modeling a one to many relationship

Let's create a table to store the lightsabers of our characters.

Lightsabers will have

* hilt_metal
* colour

We will worry about the owner later

> Ask the students to determine what type these columns will be.

Let's add a new table at the top of our file and comment out the queries we wrote earlier.

```sql
-- star_wars.sql
DROP TABLE lightsabers; -- Above DROP TABLE characters
-- Just below CREATE TABLE characters
CREATE TABLE lightsabers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  colour VARCHAR,
  hilt_metal VARCHAR 
);
```

```zsh
# terminal
sqlite3 star_wars.db < star_wars.sql
```


```sql
-- star_wars.sql
INSERT INTO lightsabers (colour, hilt_metal) VALUES ('green', 'palladium');
INSERT INTO lightsabers (colour, hilt_metal) VALUES ('red', 'gold');

SELECT * FROM lightsabers;
```

```zsh
# terminal
sqlite3 star_wars.db < star_wars.sql
```

```sql
# sqlite3 terminal
SELECT * FROM lightsabers;
```

[Task:] Add a lightsaber

# Constraints

We can add "constraints" to our table definition, which will validate the data we try to enter against some basic rules.

* A lightsaber must have a colour and a hilt metal

```sql
-- star_wars.sql
CREATE TABLE lightsabers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  colour VARCHAR NOT NULL,
  hilt_metal VARCHAR NOT NULL
);
```

```zsh
# terminal
sqlite3 star_wars.db < star_wars.sql
```

Let's try to insert some invalid data.

```sql
# star_wars.sql
INSERT INTO lightsabers (colour) VALUES ('red');
```

```zsh
# terminal
sqlite3 star_wars.db < star_wars.sql
```


## Foreign Keys

The last thing we want to do is to reflect the relationship between our characters and our lightsaber!

We can now use this primary key as an identifier in another table. When we do this we refer to it as a 'foreign key'. It's simply a primary key from another table.

> draw this on the board (one to many)

```sql
-- star_wars.sql
CREATE TABLE lightsabers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  colour VARCHAR NOT NULL,
  hilt_metal VARCHAR NOT NULL,
  character_id INTEGER NOT NULL,
      FOREIGN KEY (character_id)
         REFERENCES characters (id) 
);
```


> Note we add our foreign key info after all the columns in the table have been added. This means that the column being used for the foreign key might not be the one just before the foreign key information. E.g. we could have used the following:
> ```sql
-- star_wars.sql
CREATE TABLE lightsabers (
  id SERIAL PRIMARY KEY,
  colour VARCHAR(255) NOT NULL,
  character_id INTEGER NOT NULL,
  hilt_metal VARCHAR(255) NOT NULL,
       FOREIGN KEY (character_id)
         REFERENCES characters (id) 
);
>```

We can see that the `characters` table has a primary key, `id`,  and the `lightsabers` table now has a `references character(id)`` statement. Our `character_id`` is a reference to the primary key in the `characters` table.

Foreign keys are generally named according to the convention "table_name_singular_id", unless another name makes more 'sense' (but it would always have `_id` to indicate it's a foreign key).

Now, before we do anything else - what happens if we change the order of the drops and run this again? Because lightsabers now depends on characters, if we want to delete the character table we must remove any tables that depend on it's primary keys.

Otherwise we'd end up with a whole bunch of zombie references to it. Let's fix that up and put it back in the correct sequence.

If we inspect our newly created rows, we can see the ids of the characters. Let's use these to modify the creation of the lightsabers.

```sql
-- star_wars.sql
SELECT * FROM characters; --find the ids - depending on who got deleted 1 should be gone...

-- Now update the 2 previous lightsabers, by adding the character_id to them

INSERT INTO lightsabers (colour, character_id, hilt_metal) VALUES ('green', 2, 'palladium');

INSERT INTO lightsabers (colour, character_id, hilt_metal) VALUES ('red', 3, 'gold');
```

```zsh
# terminal
sqlite3 star_wars.db < star_wars.sql
```

What happens if we try to add a lightsaber with a character id that doesn't exist?

```sql
-- star_wars.sql
INSERT INTO lightsabers (colour, character_id, hilt_metal) VALUES ('red', 1138, 'gold');
```

It lets us do it - what??? This is because SQLite, by default, does not enforce that the foreign key should be a valid value by default. We can enforce it by adding a SQLite3 pragma to our code:

```sql
-- star_wars.sql
.headers ON
.mode column

PRAGMA FOREIGN_KEYS = ON; -- ADDED

DROP TABLE lightsabers;
DROP TABLE characters;
```

> The PRAGMA statement is an SQL extension specific to SQLite and used to change the operation SQLite. See more at https://www.sqlite.org/pragma.html

Now when we run our code, we get an error, as we might expect:

```
Error: near line 47: FOREIGN KEY constraint failed
```

> Note this line number may be different, depending on your SQL file 

SQLite expects that the `character_id` field of `lightsabers` will contain an `INT` which `REFERENCES` the primary key of another table - the `id` column of `characters`. This `character_id` column therefore contains a **foreign key**.

When we try to `INSERT INTO lightsabers` some data, including a `INT` that _doesn't_ correspond to any `id` field in `characters`, we get an error. The constraint of a foreign key is that its value must also exist somewhere in the column of the other table, and `1138` is not an `id` of any character. We have violated the foreign key constraint, which is what the error tells us.

## Conclusion

This is what we call a One to Many relationship. Each lightsaber has ONE owner (`character`). A Character can have MANY `lightsabers`, as different rows in the lightsaber table can have the same `character_id`.

As a final step, lets add one more lightsaber to Anakin/Darth Vader, then lets find all lightsabers that he has!

```sql
INSERT INTO lightsabers (colour, character_id, hilt_metal) VALUES ('red', 2, 'titanium');

SELECT * FROM lightsabers WHERE character_id = 2;
```
