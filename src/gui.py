from tkinter import *
import v2v
from threading import Thread

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
	count2 = 0
	state = True
	stateOnTop = True
	
	# initializer, constructor
	def __init__(self):
		self.root = Tk()
		self.root.overrideredirect(1)
		
		#title
		self.root.title('V2V@io')
		#ico 
		self.root.iconbitmap('D:/V2V/Voice-to-voice/src/assets/v2v.ico')
		#preset
		self.root.attributes('-topmost', True)
		#geometry
		self.root.geometry(f"+{500}+{500}")
		
		# drag and move
		self.grip = Label(self.root, bitmap="gray25", bg='#495261')
		self.grip.pack(side="top", fill="both")
		self.preset = Label(self.root, text="ICONS", bg='#495261', fg='#ffffff')
		self.preset.pack(side="left", fill="both", expand=True)
		
		self.grip.bind("<ButtonPress-1>", self.start_move)
		self.grip.bind("<ButtonRelease-1>", self.stop_move)
		self.grip.bind("<B1-Motion>", self.do_move)

		self.frame = Frame(self.root, width=480, height=850, borderwidth=10, relief=RAISED)
		self.frame.configure(background='#505c70')
		self.frame.pack_propagate(False)
		self.frame.pack()
		self.bQuit = Button(self.frame, text="Quit",command=self.root.quit)

		self.bSubmit = Button(self.frame, text="Submit", command=lambda: self.submit(self.entry.get(), str(VOICES.index(var.get()))))

		# create a listen button TODO: use two static images to represent on and off states
		self.bListen = Button(self.frame, text="Listen", command=lambda: self.listenButton(self.state, self.r, str(var2.get()), str(VOICES.index(var.get()))))
		self.bStop = Button(self.frame, text="STOP", command=lambda: self.stopListening())
		self.bClear = Button(self.frame, text="Clear", command=self.clear)
		self.bOnTop = Button(self.frame, text="OnTop", command=lambda: self.OnTop(self.stateOnTop))
		
		#text
		text=Label(self.frame, text="TYPE BELOW FOR V2V SERVICE")
		#entry
		self.entry=Entry(self.frame, width=50)
		# <Return> bind to self.submit(self.entry.get())
		self.entry.bind('<Return>', lambda x=None: self.submit(self.entry.get(), str(VOICES.index(var.get()))))

		#Enum setup
		# TODO: must retrieve the list of voices from the api server 
		
		
		VOICES= v2v.voices()
		#language setup
		var = StringVar(self.frame)
		var.set(VOICES[0])
		opt=OptionMenu(self.frame, var, *VOICES)
		
		LANGUAGES= ['ko-kr', 'en-in', 'ja-jp']
		#language setup
		var2 = StringVar(self.frame)
		var2.set(LANGUAGES[0])
		opt2=OptionMenu(self.frame, var2, *LANGUAGES)

		#TODO: bar for volume change
		#TODO: bar for speed change

		#TODO: grid setup
		text.grid(row=0, column=0, columnspan=10)
		self.entry.grid(row=1, column=0, columnspan=10)
		self.bSubmit.grid(row=1, column=10)
		Label(self.frame, text="Voice Pack").grid(row=2, column=6)
		opt.grid(row=2, column=9, columnspan=2)
		Label(self.frame, text="Voice Recognition Language").grid(row=3, column=6)
		opt2.grid(row=3, column=9, columnspan=2)
		self.bListen.grid(row=4, column=0)
		self.bStop.grid(row=4,column=1)
		self.bClear.grid(row=4, column=2)
		self.bOnTop.grid(row=4, column=3)
		self.bQuit.grid(row=4,column=4)
		

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
	

	def submit(self, text, voice): 
		#TODO: have it so that it sends it to the base source	
		print("text = " + text + " voice = " + voice)
		v2v.audio_play(v2v.inst(text,'temp', self.count, voice))
		self.count = self.count + 1
		# self.count mod 10 as limit
		if (self.count == 9):	
			self.clear()
		return
	
	def listenButton(self, state, r, lang, voice):
		#state being passed in as either on or off
		self.bListen['state'] = DISABLED
		print("listening on-")
		#th1 = Thread(target=self.root.after, args=(100, lambda:self.listen(state,r,lang,voice)))
		th1 = Thread(target=self.listen, args=(state, r, lang, voice))
		th1.start()
		return

	def listen(self, state, r, lang, voice):
		#disable after being clicked
		v2v.listening(r, self.count2, lang, voice)
		self.count2 = self.count2 + 1
		if (self.count2 == 9):
			self.clear()
		self.bListen['state'] = NORMAL	
		return

	def stopListening(self):
		self.bListen['state'] = NORMAL
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
