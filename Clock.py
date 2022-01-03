#Program to display present time
#This is done by using tkinter module

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Clock')

def time():
	#string = strftime('%H:%M:%S %p')
	string = strftime('%I:%M:%S %p')
	lbl.config(text = string)
	lbl.after(1000, time)

lbl = Label(root, font = ('lusida', 50, 'bold'),background = 'blue',foreground = 'white')

lbl.pack(anchor = 'center')
time()

mainloop()
