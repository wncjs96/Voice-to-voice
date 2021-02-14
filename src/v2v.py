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

def recognition(r, lang):
	with sr.Microphone() as source:
		print('Listening')

		#r.pause_threshold = 0.7
		# TODO: or pause hearing tongue clicking sound / button control?
		audio = r.listen(source)	
	try:
		print('Recognizing')
		query = r.recognize_google(audio, language=lang)
		#query = r.recognize_google(audio, language='en-in')
		#Korean Setup
		#query = r.recognize_google(audio, language='ko-kr')
		#Japanese Setup
		#query = r.recognize_google(audio, language='ja-jp')
	except Exception as e:
		print("EXCEPTION!!")
		return ""
	return query

def inst(text, prefix, count, voice):
	# a binary of an audio file will be sent as a response	
	# TODO: take more param values to set up properly
	print("Voice = " + voice)
	response = client.post(text, voice,1,1)
	# check if response = 200 success
	if (response.status_code != 200) :
		#TODO: in GUI.py, retrieving value -1 should engage an error message
		print("response = " + str(response))
		return -1
	filename = prefix + str(count) +'.wav'
	with open('assets/' + filename, 'wb') as f:
		f.write(response.content)
	return 'assets/' + filename

def voices():
	# get a list of voices available for v2v, return type: string of json
	response = client.get_voices()
	# check if response = 200 success
	if (response.status_code != 200):
		#TODO: in GUI.py, retrieving value -1 should engage an error message
		return -1
	print("Following is the response: \n\n" + str(response.text.split(',')) + "\n\n")
	return response.text.split(',')

def audio_play(filename):
	lock.acquire()
	print(filename)
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
	regex2 = re.compile('pemp(\d)*\.(.)*')	
	for root,dirs,files in os.walk(curr):
		for file in files:
			if regex.match(file) or regex2.match(file):
				os.unlink('assets\\' + file)
	return

def listening(r, count, lang, voice): 
	text = recognition(r, lang)
	filename = inst(text,'pemp', count, voice)
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
