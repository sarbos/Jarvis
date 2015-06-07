from gtts import gTTS


class speech:

	def __init__(self):
		self.language = 'en'

	def speak(self, phrase):
		tts = gTTS(text=phrase, lang=self.language)
		tts.save("tmp.mp3")