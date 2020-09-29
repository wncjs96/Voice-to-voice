import requests
import json
import speech_recognition as sr
import client

# Goal 1: Given text, use APIs to output virtual audio (client testing)
# Goal 2: Use speech_recognition to get the text
# Goal 3: Make GUI for voice to voice software
# Goal 4: programatically set the output audio device and let the user change it (for fun, use it as an input for a third party voice chat program)
## THE FOLLOWING IS DISCARDED AND BECAME OBSOLETE AS IT DOESNT MEET THE NEED
# web-api used: lovo-open (further details of lovo-open at https://api-doc.lovo.ai/#tag/conversion)
# Max length of text has to be <= 500 characters 
# Speaker_id is an enum var of the list of voices you can choose from.

# Private API key has to be hidden and not shown to the users of github and app inspectors
# e.g) outside src, root dir and edit .gitignore

def inst():
	response = client.post('hello world! this is for testing!', 1,1,1)

# a binary of an audio file will be sent as a response
		
	filename = 'assets/temp1.mp3'
	with open(filename, 'wb') as f:
		f.write(response.content)



def main():
	inst()

if __name__ == "__main__": main()
