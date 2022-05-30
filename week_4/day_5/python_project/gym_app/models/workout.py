class Workout:

    def __init__(self, name, date, description, duration, capacity, capacity_filled = 0, id = None):
        self.name = name
        self.date = date
        self.description = description
        self.duration = duration
        self.capacity = capacity
        self.capacity_filled = capacity_filled
        self.id = id
