import requests
import json
import speech_recognition as sr
import client
import pygame
import time

# Goal 1: Given text, use APIs to output virtual audio (client testing)
# Goal 2: Use speech_recognition to get the text
# Goal 3: Make GUI for voice to voice software
# Goal 4: programatically set the output audio device and let the user change it (for fun, use it as an input for a third party voice chat program)

def recognition():
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		print('Listening')

		r.pause_threshold = 0.7
		# TODO: or pause hearing tongue clicking sound
		audio = r.listen(source)	
	try:
		print('Recognizing')
		query = r.recognize_google(audio, language='en-in')
	except Exception as e:
		print(e)
		return "None"
	return query

def inst(text):
	# a binary of an audio file will be sent as a response	
	# TODO: take more param values to set up properly
	response = client.post(text, 1,1,1)
	filename = 'assets/temp1.mp3'
	with open(filename, 'wb') as f:
		f.write(response.content)
	
	return filename

def audio_play(filename):
	pygame.mixer.music.load(filename)
	pygame.mixer.music.play(1)
	while (pygame.mixer.get_busy()==False):
		time.sleep(500)	

def main():
	#initialize pygame
	pygame.mixer.init()

	text = recognition()
	filename = inst(text)
	audio_play(filename)
		

if __name__ == "__main__": main()
