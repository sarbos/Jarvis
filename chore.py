from datetime import datetime, date, time, timedelta

class chore:

	def __init__(self, short_name, description, person, time):
		self.name = short_name
		self.description = description
		self.person = person
		self.time = time

	def set_time(self, time):
		self.time = time

	def due(self):
		check_time = time.localtime()
		if check_time.weekday() == self.time.weekday():
			return True
