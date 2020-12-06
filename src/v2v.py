import requests
import json
import speech_recognition as sr
import client
import pygame
import time
import threading
import pathlib
import re
import os

# Goal 1: Given text, use APIs to output virtual audio (client testing)
# Goal 2: Use speech_recognition to get the text
# Goal 3: Make GUI for voice to voice software
# Goal 4: programatically set the output audio device and let the user change it (for fun, use it as an input for a third party voice chat program)

def recognition(r):
	with sr.Microphone() as source:
		print('Listening')

		#r.pause_threshold = 0.7
		# TODO: or pause hearing tongue clicking sound
		audio = r.listen(source)	
	try:
		print('Recognizing')
		#query = r.recognize_google(audio, language='en-in')
		#Korean Setup
		query = r.recognize_google(audio, language='ko-kr')
	except Exception as e:
		print("EXCEPTION!!")
		return "None"
	return query

def inst(text):
	# a binary of an audio file will be sent as a response	
	# TODO: take more param values to set up properly
	response = client.post(text, 1,1,1)
	filename = 'temp1.wav'
	#dir_path = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
	#file_path = dir_path + '/assets/' + filename
	#Îprint(dir_path)
	#print(file_path)
	with open('assets/' + filename, 'wb') as f:
		f.write(response.content)
	return 'assets/' + filename

def audio_play(filename):
	lock.acquire()
	pygame.mixer.music.load(filename)
	pygame.mixer.music.play(0)
	while pygame.mixer.music.get_busy() == True:
		continue
	pygame.mixer.music.stop()
	pygame.mixer.quit()
	lock.release()

def def_init():
	#you can change+ mp3 rate, pass it as an argument of mixer.init()
	pygame.mixer.init()
	return sr.Recognizer()

def clearfiles():
	curr = str(pathlib.Path().absolute()) + '\\assets'
	
	regex = re.compile('temp(\d)*\.(.)*')
	
	for root,dirs,files in os.walk(curr):
		for file in files:
			if regex.match(file):
				os.unlink('assets/' + file)

	
lock = threading.Lock()
def main():

	#TODO: GUI textbox to type, drodown to decide the settings, , GREEN/RED BUTTON
	#initialize pygame
	r = def_init()

	count = 0
	
	text = recognition(r)
	filename = inst(text)
	audio_play(filename)

	return

if __name__ == "__main__": main()
