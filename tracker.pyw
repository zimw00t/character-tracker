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
window.bind("<Up>",keypress)
window.bind("<Down>",keypress)
window.bind("<Return>",keypress)

stats = {
"first" : ["Intelligence", "Identity", "Corruption", "Wettness", "Messiness"],
"second" : ["Libido","Sensitivity","Age","Bladder","Bowels"],
"third" : ["Arousal","Hunger","Thirst","Pee","Poo"],
}

#load previous state
defaultsave=0,False,25,50,0,0,0,5,1,25,100,100,0,0,0,0,0

try:
	f = open('data.sav', 'r')
	save = f.read().split(',')
	f.close()
except:
	with open("data.sav", 'w') as fp:
		fp.write(str(defaultsave))
		save = defaultsave

turns = tk.StringVar()
diapered = tk.BooleanVar()
int = tk.StringVar()
ident = tk.StringVar()
corr =  tk.StringVar()
wet = tk.StringVar()
mess = tk.StringVar()
lib =  tk.StringVar()
sens =  tk.StringVar()
age = tk.StringVar()
bladder = tk.StringVar()
bowels = tk.StringVar()
arousal = tk.StringVar()
hunger = tk.StringVar()
thirst = tk.StringVar()
pee = tk.StringVar()
poo = tk.StringVar()

listvars = [turns,diapered,int,ident,corr,wet,mess,lib,sens,age,bladder,bowels,arousal,hunger,thirst,pee,poo]

def saveonexit(turns,diapered,int,ident,corr,wet,mess,lib,sens,age,bladder,bowels,arousal,hunger,thirst,pee,poo):
	exitsave = [turns.get(),diapered.get(),int.get(),ident.get(),corr.get(),wet.get(),mess.get(),lib.get(),sens.get(),age.get(),bladder.get(),bowels.get(),arousal.get(),hunger.get(),thirst.get(),pee.get(),poo.get()]
	exitstring = ','.join(str(e) for e in exitsave)
	f = open('data.sav', 'w')
	f.write(exitstring)
	f.close()
	window.destroy()

#create the interface

def makeabutton(name):
	button = tk.Button(frame,text=name,command=lambda: clicked(name))
	button.pack(side=tk.TOP)

def makealabel(name):
	label = tk.Label(frame,text=name)
	label.pack(side=tk.TOP)

def makeanentry(texvar,insert):
	entry = tk.Entry(frame, width=10, textvariable=texvar)
	entry.insert(0,insert)
	entry.pack(side=tk.TOP)

frame = tk.Frame(window)
frame.grid(row=0,column=0,padx=10,pady=10)
makealabel("Turns")
makeanentry(turns,save[0])
frame = tk.Frame(window)
frame.grid(row=1,column=0,padx=10,pady=10)
check = tk.Checkbutton(frame, text='Diapered',variable=diapered, onvalue=True, offvalue=False)
diapered.set(save[1])
check.pack()

sx = 0
stotal = 2
for x in stats:
	sy = 2
	for y in stats[x]:
		frame = tk.Frame(window)
		frame.grid(row=sy, column=sx, padx=10, pady=10)
		makealabel(y)
		makeanentry(listvars[stotal],save[stotal])
		sy += 1
		stotal += 1
	sx += 1

buttons = ["Drink","Pee","Diaper Change","Eat","Poo","Sexy Time","Move","Wait","Cum"]

ntotal = 0
for x in range(3):
	for y in range(3):
		frame = tk.Frame(window)
		frame.grid(row=y+7, column=x, padx=10, pady=10)
		makeabutton(buttons[ntotal])
		ntotal += 1

frame = tk.Frame(window)
frame.grid(row=10, column=1, padx=10, pady=10)
makeabutton("Reset")

#on exit call
window.protocol("WM_DELETE_WINDOW",lambda: saveonexit(turns,diapered,int,ident,corr,wet,mess,lib,sens,age,bladder,bowels,arousal,hunger,thirst,pee,poo))
#makes the window loop
window.mainloop()
