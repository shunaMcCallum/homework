.headers ON
.mode column

PRAGMA FOREIGN_KEYS = ON;

DROP TABLE IF EXISTS bitings;
DROP TABLE IF EXISTS humans;
DROP TABLE IF EXISTS zombies;
DROP TABLE IF EXISTS zombie_types;

CREATE TABLE humans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR
);

CREATE TABLE zombie_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR
);

CREATE TABLE zombies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    zombie_type_id INTEGER NOT NULL,
        FOREIGN KEY (zombie_type_id) 
            REFERENCES zombie_types(id)
);

CREATE TABLE bitings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    zombie_id INTEGER NOT NULL, 
    human_id INTEGER NOT NULL,   
        FOREIGN KEY (zombie_id)
            REFERENCES zombies(id),
        FOREIGN KEY(human_id) 
            REFERENCES humans(id)
);
