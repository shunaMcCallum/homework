from flask import Flask, render_template, request, redirect, Blueprint
from models.workout import Workout
import repositories.workout_repository as workout_repository

workouts_blueprint = Blueprint("workouts", __name__)

# INDEX - SHOW ALL WORKOUTS
@workouts_blueprint.route("/workouts")
def workouts():
    workouts = workout_repository.select_all()
    return render_template("workouts/index.html", workouts=workouts)

# SHOW ONE WORKOUT
@workouts_blueprint.route("/workouts/<id>")
def workout_show(id):
    workout = workout_repository.select(id)
    members = workout_repository.get_members(workout)
    return render_template("workouts/show.html", workout=workout, members=members)

# ADD NEW WORKOUT
@workouts_blueprint.route("/workouts/create")
def create_workout():
    return render_template("workouts/create.html")

# CREATE WORKOUT
@workouts_blueprint.route("/workouts", methods=['POST'])
def add_workout():
    name = request.form['name']
    date = request.form['date']
    description = request.form['description']
    duration = request.form['duration']

    workout = Workout(name, date, description, duration)
    workout_repository.save(workout)
    return redirect("/workouts")

# EDIT WORKOUT
@workouts_blueprint.route("/workouts/<id>/update")
def edit_workout(id):
    workout = workout_repository.select(id)
    return render_template("workouts/edit.html", workout=workout)

# UPDATE WORKOUT
@workouts_blueprint.route("/workouts/<id>", methods=['POST'])
def update_workout(id):
    name = request.form['name']
    date = request.form['date']
    description = request.form['description']
    duration = request.form['duration']

    workout = Workout(name, date, description, duration, id)
    workout_repository.update(workout)
    members = workout_repository.get_members(workout)
    return render_template("workouts/show.html", workout=workout, members=members)

# DELETE WORKOUT
@workouts_blueprint.route("/workouts/<id>/delete", methods=['POST'])
def delete_workout(id):
    workout_repository.delete(id)
    return redirect("/workouts")
