#init
import tkinter as tk
from tkinter import messagebox
import random
import os

window = tk.Tk()

def reentry(name, new):
	name.delete(0,'end')
	name.insert(0, new)

def textbox(event):
	if event == 'mess':
		messagebox.showinfo('mess','you pooped yourself too much') #todo

def clicked(name):
	tu = turns.get()
	c = corr.get()
	w = wet.get()
	m = mess.get()
	l = lib.get()
	s = sens.get()
	ag = age.get()
	bl = bladder.get()
	bo = bowels.get()
	ar = arousal.get()
	h = hunger.get()
	t = thirst.get()
	pe = pee.get()
	po = poo.get()
	global secretpee
	global secretpoo
	global eaten
	global drunk
	global peeholding
	global pooholding
	sleeping = False
	if name == "Reset":
		resetbutton.focus()
		turnentry.delete(0,'end')
		turnentry.insert(0,0)
		diapered.set(False)
		y = 2
		for x in entries:
			reentry(x,defaultsave[y])
			y += 1
	elif name == "Eat":
		h = h-(12+random.randint(0,3))
		if h < 0:
			h = 0
		reentry(entries[11],h)
		secretpoo += 12+random.randint(0,3)
		eaten = 2
	elif name == "Drink":
		t = t-(12+random.randint(0,3))
		if t < 0:
			t = 0
		reentry(entries[12],t)
		secretpee += 12+random.randint(0,3)
		drunk = 2
	elif name == "Poo":
		reentry(entries[14],0)
		weight=0
		if diapered.get():
			m += 1
			if m > 5:
				m = 5
				textbox('mess') #todo
			reentry(entries[4],m)
			c += 5+random.randint(0,2)
			if c > 100:
				c = 100
			reentry(entries[2],c)
			weight=10
		bo = bo+(((3*pooholding)-10)+random.randint(0,3))-weight
		if bo < 0:
			bo = 0
		reentry(entries[9],bo)
		if c > 50:
			ar += 5+random.randint(0,5)+weight
			reentry(entries[10],ar)
		pooholding = 0
	elif name == "Pee":
		reentry(entries[13],0)
		weight=0
		if diapered.get():
			w += 1
			if w > 5:
				w = 5
				textbox('mess') #todo
			reentry(entries[4],m)
			c += 5+random.randint(0,2)
			if c > 100:
				c = 100
			reentry(entries[2],c)
			weight=10
		bl = bl+(((3*peeholding)-10)+random.randint(0,3))-weight
		if bl < 0:
			bl = 0
		reentry(entries[9],bl)
		if c > 50:
			ar += 5+random.randint(0,5)+weight
			reentry(entries[10],ar)
		peeholding = 0
	elif name == "Sleep":
		sleeping = True
	elif name == "Cum":
		old = int(sens.get())
		reentry(entries[6],old+1)
	elif name == "Sexy Time":
		old = int(age.get())
		reentry(entries[7],old+1)
	elif name == "Diaper Change":
		old = int(bladder.get())
		reentry(entries[8],old+1)
	#stuff that happens ever turn goes here

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

stats = {
"first" : ["Intelligence", "Identity", "Corruption", "Wettness", "Messiness"],
"second" : ["Libido","Sensitivity","Age","Bladder","Bowels"],
"third" : ["Arousal","Hunger","Thirst","Pee","Poo"],
}

#load previous state
defaultsave=0,False,25,50,0,0,0,5,1,25,100,100,0,0,0,0,0,0,0,0,0,0,0

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
inte = tk.StringVar()
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
secretpee = 0
secretpoo = 0
eaten = 0
drunk = 0
peeholding = 0
pooholding = 0

listvars = [turns,diapered,inte,ident,corr,wet,mess,lib,sens,age,bladder,bowels,arousal,hunger,thirst,pee,poo]

def saveonexit(turns,diapered,inte,ident,corr,wet,mess,lib,sens,age,bladder,bowels,arousal,hunger,thirst,pee,poo,secretpee,secretpoo,eaten,drunk,peeholding,pooholding):
	exitsave = [turns.get(),diapered.get(),inte.get(),ident.get(),corr.get(),wet.get(),mess.get(),lib.get(),sens.get(),age.get(),bladder.get(),bowels.get(),arousal.get(),hunger.get(),thirst.get(),pee.get(),poo.get(),secretpee,secretpoo,eaten,drunk]
	exitstring = ','.join(str(e) for e in exitsave)
	f = open('data.sav', 'w')
	f.write(exitstring)
	f.close()
	window.destroy()

#create the interface

def makeabutton(name):
	button = tk.Button(frame,text=name,command=lambda: clicked(name))
	button.pack(side=tk.TOP)
	return(button)

def makealabel(name):
	label = tk.Label(frame,text=name)
	label.pack(side=tk.TOP)
	return(label)

def makeanentry(texvar,insert):
	entry = tk.Entry(frame, width=10, textvariable=texvar)
	entry.insert(0,insert)
	entry.pack(side=tk.TOP)
	return(entry)

frame = tk.Frame(window)
frame.grid(row=0,column=0,padx=10,pady=10)
turnlabel = makealabel("Turns")
turnentry = makeanentry(turns,save[0])
turnentry.focus()
frame = tk.Frame(window)
frame.grid(row=1,column=0,padx=10,pady=10)
check = tk.Checkbutton(frame, text='Diapered',variable=diapered, onvalue=True, offvalue=False)
diapered.set(save[1])
check.pack()

sx = 0
stotal = 2
labels = []
entries = []
for x in stats:
	sy = 2
	for y in stats[x]:
		frame = tk.Frame(window)
		frame.grid(row=sy, column=sx, padx=10, pady=10)
		label = makealabel(y)
		entry = makeanentry(listvars[stotal],save[stotal])
		sy += 1
		stotal += 1
		labels.append(label)
		entries.append(entry)
	sx += 1

buttons = ["Drink","Pee","Diaper Change","Eat","Poo","Sexy Time","Wait","Sleep","Cum"]

ntotal = 0
classbuttons = []
for x in range(3):
	for y in range(3):
		frame = tk.Frame(window)
		frame.grid(row=y+7, column=x, padx=10, pady=10)
		button = makeabutton(buttons[ntotal])
		ntotal += 1
		classbuttons.append(button)

frame = tk.Frame(window)
frame.grid(row=10, column=1, padx=10, pady=10)
resetbutton = makeabutton("Reset")

#on exit call
window.protocol("WM_DELETE_WINDOW",lambda: saveonexit(turns,diapered,inte,ident,corr,wet,mess,lib,sens,age,bladder,bowels,arousal,hunger,thirst,pee,poo,secretpee,secretpoo,eaten,drunk,peeholding,pooholding))
#makes the window loop
window.mainloop()