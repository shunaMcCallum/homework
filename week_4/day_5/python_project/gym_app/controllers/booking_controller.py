from flask import Flask, render_template, request, redirect, Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository

bookings_blueprint = Blueprint("bookings", __name__)

# INDEX - SHOW ALL BOOKINGS
@bookings_blueprint.route("/bookings")
def bookings():
    route_name = "bookings"
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", route_name=route_name, bookings=bookings)

# ADD NEW BOOKING
@bookings_blueprint.route("/bookings/create")
def add_booking():
    route_name = "bookings"
    members = member_repository.select_all()
    workouts = workout_repository.select_all()
    return render_template("bookings/create.html", route_name=route_name, members=members, workouts=workouts)

# CREATE BOOKING
@bookings_blueprint.route("/bookings", methods=['POST'])
def create_booking():
    route_name = "bookings"
    member_id = request.form['member_id']
    workout_id = request.form['workout_id']

    member = member_repository.select(member_id)
    workout = workout_repository.select(workout_id)

    booking = Booking(member, workout)
    booking_repository.save(booking)
    return redirect("/bookings", route_name=route_name)

# DELETE BOOKING
@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_booking(id):
    route_name = "bookings"
    booking_repository.delete(id)
    return redirect("/bookings", route_name=route_name)