import time
from person import person
from gtts import gTTS
import pyglet
from speech import speech

dude1 = person("dude", "one", "5555555555")
dude2 = person("dude", "two", "5555555555")
people = [dude1, dude2]

tmp = r"tmp.mp3"

talk = speech()

while True:
	if time.localtime().tm_sec == 0:
		print(time.asctime())
		print(people[0].fname)
		talk.speak(people[0].fname)
		music = pyglet.media.load(tmp)
		music.play()
		time.sleep(1)
