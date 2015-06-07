from gtts import gTTS
import pyglet

tmp = r"tmp.mp3"

class speech:

	def __init__(self):
		self.language = 'en'

	def speak(self, phrase):
		tts = gTTS(text=phrase, lang=self.language)
		tts.save("tmp.mp3")
		music = pyglet.media.load(tmp)
		music.play()