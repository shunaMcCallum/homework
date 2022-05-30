from db.run_sql import run_sql
from models.member import Member
from models.workout import Workout
from models.booking import Booking
import repositories.workout_repository as workout_repository

def save(member):
    
    sql = "INSERT INTO members(first_name, last_name, dob) VALUES (?, ?, ?) RETURNING id"
    values = [member.first_name, member.last_name, member.dob]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member


def sort_function(member):
    return member.last_name


def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['dob'], row['id'])
        members.append(member)
    members.sort(key=sort_function)
    return members


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['dob'], result['id'])
    return member


def delete_all():
    sql = "DELETE from members"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM members WHERE id = ?"
    values = [id]
    run_sql(sql, values)


def update(member):
    sql = "UPDATE members SET (first_name, last_name, dob) = (?, ?, ?) WHERE id = ?"
    values = [member.first_name, member.last_name, member.dob, member.id]
    run_sql(sql, values)


def get_workouts(member):
    workouts = []
    
    sql = "SELECT workouts.* FROM workouts INNER JOIN bookings ON workouts.id = workout_id WHERE member_id = ?"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        workout = Workout(row['name'], row['date'], row['description'], row['duration'], row['capacity'], row['id'])
        workouts.append(workout)
    return workouts

def get_bookings_member(member):
    bookings = []
    
    sql = "SELECT * from bookings WHERE member_id = ?"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        member1 = select(row['member_id'])
        workout = workout_repository.select(row['workout_id'])
        booking = Booking(member1, workout, row['id'])
        bookings.append(booking)
    return bookings