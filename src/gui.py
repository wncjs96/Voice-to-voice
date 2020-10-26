from tkinter import *

# GUI 
# dropdown to pick a voice
# dropdown for speed
# drag bar for volume
# textbox to type, senses the enter key 
# On and Off button
# minimize to system tray
# new border that can move the app window

# background color: 

root = Tk()
root.title('V2V')
root.geometry('500x400+10+10')
root.configure(background='black')
lbl = Label(root, text="name")
lbl.grid(row=0, column=0)
txt = Entry(root)
txt.grid(row=0, column=1)
btn = Button(root, text="ok", width=15)
btn.grid(row=1, column=1)
root.mainloop()

