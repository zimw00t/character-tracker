#init
import tkinter as tk
from random import randrange
import os

window = tk.Tk()

def clicked(name):
	print(name)

def keypress(event):
	if event.keysym == "Left":
		return
	elif event.keysym == "Right":
		return
	else:
		return

#window size settings
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
w = 800
h = 600
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.title("Character Tracker")
#window.geometry('%dx%d+%d+%d' % (w, h, x, y))
#window.resizable(width=False, height=False)

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

window.bind("<Left>", keypress)
window.bind("<Right>",keypress)
window.bind("<Return>",keypress)

stats = {
"mentalstats" : ["Intelligence", "Identity", "Corruption"],
"phystats" : ["Libido","Sensitivity","Age","Bladder","Bowels"],
"needs" : ["Arousal","Hunger","Thirst","Pee","Poo"],
}

#buttons and shit
sx = 0
for x in stats:
	sy = 0
	for y in stats[x]:
		frame = tk.Frame(window)
		frame.grid(row=sy, column=sx, padx=10, pady=10)
		label = tk.Label(frame,text=y)
		label.pack(side=tk.TOP)
		entry = tk.Entry(frame, width=10)
		entry.pack(side=tk.TOP)
		sy += 1
	sx += 1

def makeabutton(name):
	button = tk.Button(frame,text=name,command=lambda: clicked(name))
	button.pack(side=tk.TOP)

buttons = ["Poo","Pee","Cum"]

for x in range(3):
	frame = tk.Frame(window)
	frame.grid(row=6, column=x, padx=10, pady=10)
	makeabutton(buttons[x])

frame = tk.Frame(window)
frame.grid(row=7, column=1, padx=10, pady=10)
makeabutton("Advance")

#makes the window loop
window.mainloop()