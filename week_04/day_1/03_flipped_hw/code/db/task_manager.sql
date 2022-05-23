DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  description VARCHAR,
  assignee VARCHAR,
  duration INT,
  completed BOOLEAN DEFAULT FALSE
);

INSERT INTO tasks (description, assignee, duration) 
VALUES ('Walk Dog', 'Jack Jarvis', 60);

INSERT INTO tasks (description, assignee, duration) 
VALUES ('Feed Cat', 'Victor McDade', 5);