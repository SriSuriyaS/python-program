# importing whole module
from tkinter import *
from tkinter.ttk import *

# importing strftime function to
# retrieve system's time
from time import strftime

from datetime import date

# creating tkinter window
root = Tk()
root.title('Clock')

# This function is used to
# display time on the label
def date_time():
	#string = strftime('%H:%M:%S %p')
	string = strftime('%I:%M:%S %p')
	today = date.today()
	lbl.config(text = string)
	lbl1.config(text = today)
	lbl.after(34, date_time)

# Styling the label widget so that clock
# will look more attractive
lbl = Label(root,font = ('lusida', 50, 'bold'),
			background = 'white',
			foreground = 'black')
lbl1 = Label(root, font = ('lusida', 30, 'bold'),
			background = 'white',
			foreground = 'black')


# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor = 'center')
lbl1.pack(anchor = 'center')


date_time()
##

root.mainloop()
