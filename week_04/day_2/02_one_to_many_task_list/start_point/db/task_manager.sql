DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  description VARCHAR,
  assignee VARCHAR,
  duration INT,
  completed BOOLEAN
);