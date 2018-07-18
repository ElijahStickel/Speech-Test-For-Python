# Speech Recognition with Google API
# By Elijah Camcam
import speech_recognition as sr
from gtts import gTTS
import pyglet
import time
import os

def microphone_init():
	r = sr.Recognizer() # This is to make the microphone recognize activity
	
	# This enables the Microphone to turn on
	with sr.Microphone() as source:
		print("Listening.....")
		audio = r.listen(source)
		print("Done")

		# This prosces trys to send google the audio recording
		try:
			print("A Voice has been heard")
			text = r.recognize_google(audio)# This makes your audio into a value for google to read
			print(text)
			audio_out(text)
		except Exception as e:
			print(str(e))
			# This is optional
			# You can use
			#except: 
			#    pass

def audio_out(text):
	file = gTTS(text = text, lang = 'en') # The text is text and the language is english
	filename = '/tmp/temp.mp3' # We are making an Temporary MP3 file 
	file.save(filename) # Temporarily saving the file for use

	music = pyglet.media.load(filename, streaming = False) # Alows us to play the encoded file
	#streaming = False makes sure that no sub prosceses are using it
	musci.play() # plays the audi

	time.sleep(music.duraation) # Makes the audio play within time
	os.remove(filename) # removes the temporary file

# Runs proscess once file is loaded
if __name__ == '__main__':
	microphone_init()