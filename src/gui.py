from tkinter import *
import v2v

# GUI 
# dropdown to pick a voice
# dropdown for speed
# drag bar for volume
# textbox to type, senses the enter key 
# On and Off button
# minimize to system tray
# new border that can move the app window

# background color: 

class App():
	# class var
	r = v2v.def_init()
	count = 0
	# TODO: temp state
	state = True
	stateOnTop = False

	# initializer, constructor
	def __init__(self):
		self.root = Tk()
		self.root.overrideredirect(1)
		
		#title
		self.root.title('V2V@io')
		#ico 
		self.root.iconbitmap('D:/V2V/Voice-to-voice/src/assets/v2v.ico')
		
		# drag and move
		self.label = Label(self.root, text="click to drag")
		self.grip = Label(self.root, bitmap="gray25")
		self.grip.pack(side="left", fill="y")
		self.label.pack(side="right", fill="both", expand=True)
		
		self.grip.bind("<ButtonPress-1>", self.start_move)
		self.grip.bind("<ButtonRelease-1>", self.stop_move)
		self.grip.bind("<B1-Motion>", self.do_move)

		self.frame = Frame(self.root, width=480, height=850, borderwidth=10, relief=RAISED)
		self.frame.configure(background='#505c70')
		self.frame.pack_propagate(False)
		self.frame.pack()
		self.bQuit = Button(self.frame, text="Quit",command=self.root.quit)

		self.bSubmit = Button(self.frame, text="Submit", command=lambda: self.submit(self.entry.get()))

		# create a listen button TODO: use two static images to represent on and off states
		self.bListen = Button(self.frame, text="Listen", command=lambda: self.listen(self.state, self.r))
		self.bClear = Button(self.frame, text="Clear", command=self.clear)
		self.bOnTop = Button(self.frame, text="OnTop", command=lambda: self.OnTop(self.stateOnTop))
		
		#text
		text=Label(self.frame, text="type below the text to be read out loud")
		#entry
		self.entry=Entry(self.frame, width=50)
		# <Return> bind to self.submit(self.entry.get())
		self.entry.bind('<Return>', lambda x=None: self.submit(self.entry.get()))
		#Enum setup
		OPTIONS	= ["text", "speaker_id", "volume", "speed"]
		#dropdown of 4: enum OPTIONS={text, speaker_id, volume, speed}
		var = StringVar(self.frame)
		var.set(OPTIONS[0])
		opt=OptionMenu(self.frame, *OPTIONS)

		#TODO: grid setup
		text.grid(row=0, column=0, columnspan=2)
		self.entry.grid(row=1, column=0, columnspan = 3)
		opt.grid(row=0, column=2)
		self.bSubmit.grid(row=1, column=4)
		self.bQuit.grid(row=2,column=0)
		self.bListen.grid(row=3, column=0)
		self.bClear.grid(row=4, column=0)
		self.bOnTop.grid(row=5, column=0)

	# instance methods
	def start_move(self, event):
		self.root.x = event.x
		self.root.y = event.y

	def stop_move(self, event):
		self.root.x = None
		self.root.y = None

	def do_move(self, event):
		deltax = event.x - self.root.x
		deltay = event.y - self.root.y
		x = self.root.winfo_x() + deltax
		y = self.root.winfo_y() + deltay
		self.root.geometry(f"+{x}+{y}")
	
	def submit(self, text): 
		#TODO: have it so that it sends it to the base source	
		print(text)
		v2v.audio_play(v2v.inst(text, self.count))
		self.count = self.count + 1
		# self.count mod 10 as limit
		if (self.count == 9):	
			self.clear()
		return

	def listen(self, state, r):
		#state being passed in as either on or off
		print("listening on-")
		#disable after being clicked 
		if (state == True) : 
			self.bListen['state'] = DISABLED
		else :
			self.bListen['state'] = NORMAL
	
		v2v.listening(r)
		return

	def OnTop(self, stateOnTop):
		if (stateOnTop == False) :
			self.root.attributes('-topmost', True)
		else :
			self.root.attributes('-topmost', False)	
		self.stateOnTop = not self.stateOnTop
		print("On Top state: "+str(self.stateOnTop))	
		return
	
	def clear(self):
		# reset count to 0
		self.count = 0
		v2v.clearfiles()
		print("Clear Completed! count = " + str(self.count))
		return

	# test case
	def __output__():
		print(text.get())
		return 
def main():
	#TODO: remove test cases when imported
	app = App()
	app.root.mainloop()
	
				
	
	return

if __name__ == "__main__": main()
