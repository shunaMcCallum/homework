from flask import Flask, render_template, request, redirect, Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

#  INDEX - SHOW ALL MEMBERS
@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)

# SHOW ONE MEMBER
@members_blueprint.route("/members/<id>")
def member_show(id):
    member = member_repository.select(id)
    workouts = member_repository.get_workouts(member)
    return render_template("members/show.html", member=member, workouts=workouts)

# ADD NEW MEMBER
@members_blueprint.route("/members/create")
def add_member():
    return render_template("members/create.html")

# CREATE MEMBER
@members_blueprint.route("/members", methods=['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']

    member = Member(first_name, last_name, dob)
    member_repository.save(member)
    return redirect("/members")

# EDIT MEMBER
@members_blueprint.route("/members/<id>/update")
def edit_member(id):
    member = member_repository.select(id)
    return render_template("/members/edit.html", member=member)

# UPDATE MEMBER
@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']

    member = Member(first_name, last_name, dob, id)
    member_repository.update(member)
    workouts = member_repository.get_workouts(member)
    return render_template("members/show.html", member=member, workouts=workouts)

# DELETE MEMBER
@members_blueprint.route("/members/<id>/delete", methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")
