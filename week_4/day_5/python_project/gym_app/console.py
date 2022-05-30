import pdb
import datetime
from models.member import Member
from models.workout import Workout
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
member_repository.delete_all()
workout_repository.delete_all()

member1 = Member("Frasier", "Crane", datetime.datetime(1960, 10, 10))
member_repository.save(member1)
member2 = Member("Niles", "Crane", datetime.datetime(1963, 7, 7))
member_repository.save(member2)

workout1 = Workout("Spin Class", datetime.datetime(2022, 6, 6), "Spin class", 60, 12)
workout_repository.save(workout1)
workout2 = Workout("Boxing Class", datetime.date(2022, 9, 6), "Boxing class", 45, 20)
workout_repository.save(workout2)

booking1 = Booking(member1, workout1)
booking_repository.save(booking1)
booking2 = Booking(member2, workout2)
booking_repository.save(booking2)
booking3 = Booking (member1, workout2)
booking_repository.save(booking3)
booking4 = Booking(member2, workout1)
booking_repository.save(booking4)

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

#  Testing show one member
# member = member_repository.select(41)
# print(member.__dict__)

# Testing workouts save and select
# workouts = workout_repository.select_all()
# for workout in workouts:
#     print(workout.__dict__)

# Testing workout capacities update and print
workout = workout_repository.select(1)
print(workout.__dict__)

workout2 = workout_repository.select(2)
print(workout2.__dict__)

# Testing workouts delete
# workout_repository.delete(5)

# Testing workouts update
# workout1.name = "HIIT Workout"
# workout_repository.update(workout1)

# workouts = workout_repository.select_all()
# for workout in workouts:
#     print(workout.__dict__)

# Testing bookings save and select
# bookings = booking_repository.select_all()
# for booking in bookings:
#     print(booking.__dict__)

# Testing bookings delete
# booking_repository.delete(14)

# bookings = booking_repository.select_all()
# for booking in bookings:
#     print(booking.__dict__)

# Testing select one member's workouts
# member_workouts = member_repository.get_workouts(member1)
# for workout in member_workouts:
#     print(workout.__dict__)

# Testing select one workout's members
# workout_members = workout_repository.get_members(workout1)
# for member in workout_members:
#     print(member.__dict__)



pdb.set_trace()