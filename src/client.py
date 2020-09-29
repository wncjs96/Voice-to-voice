import requests

##
##	Given a string, send a post request to the server to download the output file of the audio
##

def post(text, speaker_id, volume, speed): 
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

	# outfile in form of temp1.mp3 ... temp 100.mp3
	filename = 'assets/temp1.mp3'
	with open(filename, 'wb') as f:
		f.write(response.content)

def main():
	client_post()

if __name__ == "__main__": main()
