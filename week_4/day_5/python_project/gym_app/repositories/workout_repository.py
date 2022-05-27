from db.run_sql import run_sql
from models.workout import Workout

def save(workout):
    sql = "INSERT INTO workouts (name, date, description, duration) VALUES (?, ?, ?, ?) RETURNING id"
    values = [workout.name, workout.date, workout.description, workout.duration]
    results = run_sql(sql, values)
    workout.id = results[0]['id']
    return workout

def select_all():
    workouts = []
    sql = "SELECT * FROM workouts"
    results = run_sql(sql)
    
    for row in results:
        workout = Workout(row['name'], row['date'], row['description'], row['duration'], row['id'])
        workouts.append(workout)
    return workouts

def select(id):
    workout = None
    sql = "SELECT * FROM workouts where id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        workout = Workout(result['name'], result['date'], result['description'], result['duration'], result['id'])
    return workout

def delete_all():
    sql = "DELETE from workouts"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM workouts where id = ?"
    values = [id]
    run_sql(sql, values)

def update(workout):
    sql = "UPDATE workouts SET (name, date, description, duration) = (?, ?, ?, ?) WHERE id = ?"
    values = [workout.name, workout.date, workout.description, workout.duration, workout.id]
    run_sql(sql, values)