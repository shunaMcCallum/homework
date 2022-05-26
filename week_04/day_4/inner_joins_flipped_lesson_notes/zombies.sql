.headers ON
.mode column 

PRAGMA FOREIGN_KEYS = ON;

DROP TABLE bitings;
DROP TABLE zombies;
DROP TABLE victims;

CREATE TABLE zombies
(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR NOT NULL,
  type VARCHAR
);

CREATE TABLE victims
(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR NOT NULL,
  run_speed INT
);

CREATE TABLE bitings
(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  victim_id INTEGER NOT NULL,
  zombie_id INTEGER NOT NULL,
  infected_on DATE NOT NULL,
    FOREIGN KEY(victim_id)
      REFERENCES victims(id),
    FOREIGN KEY(zombie_id)
      REFERENCES zombies(id)
);

INSERT INTO victims (name, run_speed) VALUES ('Rick', 12);
INSERT INTO victims (name, run_speed) VALUES ('Maggie', 11);
INSERT INTO victims (name, run_speed) VALUES ('Michonne', 15);
INSERT INTO victims (name, run_speed) VALUES ('Glenn', 30);

INSERT INTO zombies (name, type) VALUES ('Romero', 'generic');
INSERT INTO zombies (name, type) VALUES ('Boyle', 'runner');
INSERT INTO zombies (name, type) VALUES ('Raimi', 'deadite');
INSERT INTO zombies (name, type) VALUES ('Newell', 'boomer');

INSERT INTO bitings (zombie_id, victim_id, infected_on) VALUES (1, 1, 'March 27 2018');
INSERT INTO bitings (zombie_id, victim_id, infected_on) VALUES (2, 2,'March 29 2018');
INSERT INTO bitings (zombie_id, victim_id, infected_on) VALUES (4, 3, 'March 30 2018');
INSERT INTO bitings (zombie_id, victim_id, infected_on) VALUES (1, 3, 'March 30 2018');