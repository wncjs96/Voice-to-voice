import requests
##
##	Given a string, send a post request to the server to download the output file of the audio
##

def post(text, speaker_id, volume, speed): 

## THE FOLLOWING IS DISCARDED AND BECAME OBSOLETE AS IT DOESNT MEET THE NEED
# web-api used: lovo-open (further details of lovo-open at https://api-doc.lovo.ai/#tag/conversion)
# Max length of text has to be <= 500 characters 
# Speaker_id is an enum var of the list of voices you can choose from.

# Private API key has to be hidden and not shown to the users of github and app inspectors
# e.g) outside src, root dir and edit .gitignore

	# Can use a different API
	url = 'http://127.0.0.1:5000/api/conversion' 
	data = {
		"text": text,
		"speaker_id": speaker_id,
		"volume": volume,
		"speed": speed
	}
	headers = {
		'Content-Type': 'application/json; charset=utf-8'
	}

	print(data)
	print("data type: " + type(data).__name__)
	
	response = requests.post(url, headers=headers, json=data)

	return response

#	# outfile in form of temp1.mp3 ... temp 100.mp3
#	filename = 'assets/temp1.mp3'
#	with open(filename, 'wb') as f:
#		f.write(response.content)

#TODO: get list of voices
def get_voices():
	url = 'http://127.0.0.1:5000/api/voices'
	headers = {
		'Content-Type': 'application/json; charset=utf-8'
	}	

	response = requests.get(url, headers=headers)
	return response

def main():
	client_post()

if __name__ == "__main__": main()
