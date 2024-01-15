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
    if event == 'toomess':
        messagebox.showinfo('Leaking Mess','That diaper is too full, you need a change.')
    if event == 'toowet':
        messagebox.showinfo('Leaking Pee','Your soggy diaper can\'t absorb any more. It starts to leak.')
    if event == 'eat':
        messagebox.showinfo('Hungry','You need to eat!')
    if event == 'drink':
        messagebox.showinfo('Thirsty','You need to drink!')
    if event == 'diaperwet':
        messagebox.showinfo('You had an accident!','You accidentally peed in you diaper.')
    if event == 'diapermess':
        messagebox.showinfo('You had an accident!','You accidentally pooped in you diaper.')
    if event == 'wet':
        messagebox.showinfo('You had an accident!','You accidentally peed.')
    if event == 'mess':
        messagebox.showinfo('You had an accident!','You accidentally pooped.')
    if event == 'cum':
        messagebox.showinfo('Cumming!','You were too aroused and came uncontrollably.')

def clicked(name):
    tu = int(turns.get())
    c = int(corr.get())
    w = int(wet.get())
    m = int(mess.get())
    l = int(lib.get())
    s = int(sens.get())
    ag = int(age.get())
    bl = int(bladder.get())
    bo = int(bowels.get())
    ar = int(arousal.get())
    h = int(hunger.get())
    th = int(thirst.get())
    pe = int(pee.get())
    po = int(poo.get())
    global secretpee
    global secretpoo
    global eaten
    global drunk
    global peeholding
    global pooholding
    arousalthresh = 100 - (l +int(((s*.4) * c/10)))
    peethresh = bl+int(bl*.2)
    poothresh = bo+int(bl*.2)
    sleeping = False
    if name == "Reset":
        resetbutton.focus()
        reentry(turnentry,0)
        diapered.set(False)
        y = 2
        for x in entries:
            reentry(x,defaultsave[y])
            y += 1
    else:
        if name == "Eat":
            h = h-(12+random.randint(0,3))
            if h < 0:
                h = 0
            reentry(entries[11],h)
            secretpoo += 12+random.randint(0,3)
            eaten = 2
        elif name == "Drink":
            th = th-(12+random.randint(0,3))
            if th < 0:
                th = 0
            reentry(entries[12],th)
            secretpee += 12+random.randint(0,3)
            drunk = 2
        elif name == "Poo":
            po = 0
            reentry(entries[14],po)
            weight = 0
            if diapered.get():
                m += 1
                if m > 5:
                    m = 5
                    textbox('toomess')
                reentry(entries[4],m)
                c += 3+random.randint(0,4)
                if c > 100:
                    c = 100
                reentry(entries[2],c)
                weight=10
            bo = bo+(((3*pooholding)-10)+random.randint(0,3))-weight
            if bo < 0:
                bo = 0
            reentry(entries[9],bo)
            if c > 50:
                ar += 5+random.randint(0,3)+weight
                reentry(entries[10],ar)
            pooholding = 0
        elif name == "Pee":
            pe = 0
            reentry(entries[13],pe)
            weight = 0
            if diapered.get():
                w += 1
                if w > 5:
                    w = 5
                    textbox('toowet')
                reentry(entries[3],w)
                c += 3+random.randint(0,4)
                if c > 100:
                    c = 100
                reentry(entries[2],c)
                weight=10
            bl = bl+(((3*peeholding)-10)+random.randint(0,3))-weight
            if bl < 0:
                bl = 0
            reentry(entries[8],bl)
            if c > 50:
                ar += 5+random.randint(0,3)+weight
                reentry(entries[10],ar)
            peeholding = 0
        elif name == "Diaper Change":
            diapered.set(True)
            w = 0
            m = 0
            reentry(entries[3],w)
            reentry(entries[4],m)
            if c > 50:
                ar += 5+random.randint(0,3)
                reentry(entries[10],ar)
        elif name == "Sexy Time":
            weight = int(l/5) + int((2*s)/5) + int(c/20)
            ar += 10+random.randint(0,7)+weight
            reentry(entries[10],ar)
        elif name == "Cum":
            if ar < arousalthresh*.75:
                c += 3+random.randint(0,4)
                if c > 100:
                    c = 100
                reentry(entries[2],c)
            ar = 0
            reentry(entries[10],ar)
            peethresh += 20
            poothresh += 20
        elif name == "Sleep":
            sleeping = True
        reentry(turnentry,tu+1)
        if not eaten > 0:
            h += 3+random.randint(0,2)
            if h > 100:
                h = 100
                textbox('eat')
            reentry(entries[11],h)
        if not drunk > 0:
            th += 3+random.randint(0,2)
            if th > 100:
                th = 100
                textbox('drink')
            reentry(entries[12],th)
        eaten -= 1
        drunk -= 1
        if eaten < 0:
            eaten = 0
        if drunk < 0:
            drunk = 0
        if pe < secretpee:
            pe += 6+random.randint(0,6)
            reentry(entries[13],pe)
        else:
            pe += 3+random.randint(0,2)
            reentry(entries[13],pe)
        if po < secretpoo:
            po += 6+random.randint(0,6)
            reentry(entries[14],po)
        else:
            po += 3+random.randint(0,2)
            reentry(entries[14],po)
        if not sleeping:
            ar += random.randint(0,3)+int(c/15)
            reentry(entries[10],ar)
        if pe > peethresh:
            roll = random.randint(0,pe - peethresh)
            if roll > (pe - peethresh)/2 + ag/5:
                pe = 0
                reentry(entries[13],pe)
                weight = 0
                if diapered.get():
                    textbox('diaperwet')
                    w += 1
                    if w > 5:
                        w = 5
                        textbox('toowet')
                    reentry(entries[3],w)
                    weight=10
                else:
                    textbox('wet')
                bl -= 10
                if bl < 0:
                    bl = 0
                reentry(entries[8],bl)
                c += 3+random.randint(0,4)+weight
                if c > 100:
                    c = 100
                reentry(entries[2],c)
                if c > 50:
                    ar += 5+random.randint(0,3)+weight
                    reentry(entries[10],ar)
                peeholding = 0
            else:
                peeholding += 1
        if po > poothresh:
            roll = random.randint(0,po - poothresh)
            if roll > (po - poothresh)/2 + ag/5:
                po = 0
                reentry(entries[14],po)
                weight = 0
                if diapered.get():
                    textbox('diapermess')
                    m += 1
                    if m > 5:
                        m = 5
                        textbox('toomess')
                    reentry(entries[4],m)
                    weight=10
                else:
                    textbox('mess')
                bo -= 10
                if bo < 0:
                    bo = 0
                reentry(entries[9],bo)
                c += 3+random.randint(0,4)+weight
                if c > 100:
                    c = 100
                reentry(entries[2],c)
                if c > 50:
                    ar += 5+random.randint(0,3)+weight
                    reentry(entries[10],ar)
                pooholding = 0
            else:
                pooholding += 1
        if ar > arousalthresh:
            roll = random.randint(0,ar - arousalthresh)
            if roll > (ar - arousalthresh)/2 + 5:
                ar = 0
                reentry(entries[10],ar)
                textbox('cum')
            
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
defaultsave=0,False,25,50,0,0,0,5,1,25,50,50,0,0,0,0,0,0,0,0,0,0,0

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