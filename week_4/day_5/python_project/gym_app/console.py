import pdb
import datetime
from models.member import Member
from models.workout import Workout
from models.booking import Booking

# IMPORT REPOSITORIES HERE
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository

# RUN DELETE METHODS HERE
member_repository.delete_all()
workout_repository.delete_all()

# CREATE DUMMY DATA AND TESTS HERE
# member1 = Member("Frasier", "Crane", datetime.datetime(1960, 10, 10))
# member_repository.save(member1)
# member2 = Member("Niles", "Crane", datetime.datetime(1963, 7, 7))
# member_repository.save(member2)

workout1 = Workout("Spin Class", datetime.datetime(2022, 6, 6), "Spin class", 60)
workout_repository.save(workout1)
workout2 = Workout("Boxing Class", datetime.date(2022, 9, 6), "Boxing class", 45)
workout_repository.save(workout2)

# Testing members save and select
# members = member_repository.select_all()
# for member in members:
#     print(member.__dict__)

# Testing members delete
# member_repository.delete(10)

# Testing members update
# member1.first_name = "Daphne"
# member_repository.update(member1)

# members = member_repository.select_all()
# for member in members:
#     print(member.__dict__)

# Testing workouts save and select
# workouts = workout_repository.select_all()
# for workout in workouts:
#     print(workout.__dict__)

# Testing workouts delete
# workout_repository.delete(5)

# Testing wokrouts update
# workout1.name = "HIIT Workout"
# workout_repository.update(workout1)

# workouts = workout_repository.select_all()
# for workout in workouts:
#     print(workout.__dict__)

pdb.set_trace()