from db.run_sql import run_sql
from models.workout import Workout
from models.member import Member

def save(workout):
    sql = "INSERT INTO workouts (name, date, description, duration, capacity) VALUES (?, ?, ?, ?, ?) RETURNING id"
    values = [workout.name, workout.date, workout.description, workout.duration, workout.capacity]
    results = run_sql(sql, values)
    workout.id = results[0]['id']
    return workout


def sort_fuction(workout):
    return workout.date


def select_all():
    workouts = []
    sql = "SELECT * FROM workouts"
    results = run_sql(sql)
    for row in results:
        workout = Workout(row['name'], row['date'], row['description'], row['duration'], row['capacity'], row['capacity_filled'], row['id'])
        workouts.append(workout)
    workouts.sort(key=sort_fuction)
    return workouts


def select(id):
    workout = None
    sql = "SELECT * FROM workouts where id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        workout = Workout(result['name'], result['date'], result['description'], result['duration'], result['capacity'], result['capacity_filled'], result['id'])
    return workout


def delete_all():
    sql = "DELETE from workouts"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM workouts where id = ?"
    values = [id]
    run_sql(sql, values)


def update(workout):
    sql = "UPDATE workouts SET (name, date, description, duration, capacity, capacity_filled) = (?, ?, ?, ?, ?, ?) WHERE id = ?"
    values = [workout.name, workout.date, workout.description, workout.duration, workout.capacity, workout.capacity_filled, workout.id]
    run_sql(sql, values)

def get_members(workout):
    members = []
    
    sql = "SELECT members.* from members INNER JOIN bookings ON members.id = bookings.member_id WHERE workout_id = ?"
    values = [workout.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['dob'], row['id'])
        members.append(member)
    return members

def update_capacity_filled(workout):
    workout.capacity_filled += 1

    sql = "UPDATE workouts SET (capacity_filled) = (?) WHERE id = ?"
    values = [workout.capacity_filled, workout.id]
    run_sql(sql, values)


