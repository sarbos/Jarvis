import time
from person import person
from gtts import gTTS
from speech import speech
from datetime import datetime, date, time, timedelta
from chore import chore
import time

import pymongo
from pymongo import MongoClient
client = MongoClient()

db = client.jarvis_db
people_collection = db.people
chore_collection = db.chores

people = []
chores = []

for p in people_collection.find():
	people.append(person(p["fname"], p["sname"], p["phone"]))
	print(people[-1])

for c in chore_collection.find():
	chores.append(chore(c["name"], c["description"], c["person"], c["time"]))
	print(chores[-1])

dude1 = person("James", "Test", "5555555")
dude2 = person("Jessica", "Test", "5555555")

talk = speech()

trash = chore("Trash", "Take out the trash", dude1)
trash.set_time(datetime.now()+ timedelta(seconds = 15))

dishes = chore("Dishes", "Do the Dishes", dude2)
dishes.set_time(datetime.now()+ timedelta(seconds = 5))
print(dishes.time)

chores = [trash, dishes]

while True:

	#chore loop
	for c in chores:
		if (c.time - datetime.now()).seconds < 1:
			talk.speak(c.person.fname + ", " + c.description)
			time.sleep(1)
	
