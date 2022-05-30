from db.run_sql import run_sql
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository

def save(booking):
    sql = "INSERT INTO bookings (member_id, workout_id) VALUES (?, ?) RETURNING id"
    values = [booking.member.id, booking.workout.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']

    workout_repository.update_capacity_filled(booking.workout)

    return booking

def select(id):
    booking = None
    sql = "SELECT * FROM bookings where id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        booking = Booking(result['member_id'], result['workout_id'], result['id'])
    return booking

def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        workout = workout_repository.select(row['workout_id'])
        booking = Booking(member, workout, row['id'])
        bookings.append(booking)
    return bookings


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


def get_workout(id):
    booking = select(id)
    workout = workout_repository.select(booking.workout)
    return workout


def delete(id):
    workout = get_workout(id)
    workout_repository.reduce_capacity_filled(workout)

    sql = "DELETE FROM bookings WHERE id = ?"
    values = [id]
    run_sql(sql, values)



