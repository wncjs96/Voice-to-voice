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
import mmap

# Goal 1: Given text, use APIs to output virtual audio (client testing)
# Goal 2: Use speech_recognition to get the text
# Goal 3: Make GUI for voice to voice software
# Goal 4: programatically set the output audio device and let the user change it (for fun, use it as an input for a third party voice chat program)

def recognition(r):
	with sr.Microphone() as source:
		print('Listening')

		#r.pause_threshold = 0.7
		# TODO: or pause hearing tongue clicking sound / button control?
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

def inst(text, count):
	# a binary of an audio file will be sent as a response	
	# TODO: take more param values to set up properly
	response = client.post(text, 1,1,1)
	filename = 'temp' + str(count) +'.wav'
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
	lock.release()

def def_init():
	#you can change+ mp3 rate, pass it as an argument of mixer.init()
	pygame.mixer.init()
	return sr.Recognizer()

def clearfiles():
	pygame.mixer.music.load('assets/test.wav')
	curr = str(pathlib.Path().absolute()) + '\\assets'
	
	regex = re.compile('temp(\d)*\.(.)*')
	
	for root,dirs,files in os.walk(curr):
		for file in files:
			if regex.match(file):
				os.unlink('assets\\' + file)
	return

def listening(r): 
	text = recognition(r)
	filename = inst(text)
	audio_play(filename)
	
lock = threading.Lock()

def main():

	#TODO: GUI textbox to type, drodown to decide the settings, , GREEN/RED BUTTON
	#ui = gui.App()
	#ui.root.mainloop()

	#initialize pygame
	#r = def_init()

	#count = 0
	
	#TODO: make sure the recognition starts when bListen is clicked
	#listening(r)

	return

if __name__ == "__main__": main()
