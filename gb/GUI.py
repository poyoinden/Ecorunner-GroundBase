from SensorData import SensorData
from GPS import GPS
from parseMessage import parseMessage
from readMessage import nextMessage
from addToGBDatabase import addToDatabase
from cleardb import cleardb
import sys
import re
import time
import boto.sqs
import numpy as np
from boto.sqs.message import Message
import MySQLdb
from writeDBToFile import writeDBToFile
from collections import deque
from Tkinter import *
from rpmToKMHDisplay import rpmToKMHDisplay
from datetime import datetime
import math
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

db = MySQLdb.connect("localhost","root","reverse","mydata")
cursor = db.cursor()

root = Tk()

# Set up variables for the GUI
var1 = StringVar()
var1.set('Throttle: ' + str(-1))
var2 = StringVar()
var2.set('RPM: ' + str(-1))
var3 = StringVar()
var3.set('KM/H: ' + str(-1))
var4 = StringVar()
var4.set('Current: ' + str(-1))

# Add labels (text) to the GUI
l1 = Label(root, textvariable = var1)
l1.config(font=("Courier", 50))
l1.pack()
l2 = Label(root, textvariable = var2)
l2.config(font=("Courier", 50))
l2.pack()
l3 = Label(root, textvariable = var3)
l3.config(font=("Courier", 50))
l3.pack()
l4 = Label(root, textvariable = var4)
l4.config(font=("Courier", 50))
l4.pack()

# Add a button for writing the log file to the GUI
B = Button(root, text ="Make log file", command = writeDBToFile)
B.config(font=("Courier", 25))
B.pack()

# Set up the graph variables for the GUI
LARGE_FONT= ("Verdana", 12)
style.use("ggplot")
f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

xList = deque(maxlen=25)
yList = deque(maxlen=25)

def animate(i, speed, f):
	xList.append(int(i))
	yList.append(speed)

	a.clear()
	a.plot(xList, yList)
	f.canvas.draw()

	

canvas = FigureCanvasTkAgg(f, root)
canvas.show()
canvas.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=True)
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

i = 0
while True:
	try: 
		message = nextMessage(receiveQueue)
		addToDatabase(message)

		if(isinstance(message, SensorData) and message.getSensorId() == "1"):
			var1.set('Throttle: ' + str(message.getData()))

		elif(isinstance(message, SensorData) and message.getSensorId() == "2"):
			var2.set('RPM: ' + str(message.getData()))
			speedKMH = rpmToKMHDisplay(message.getData())
			var3.set('KM/H: ' + str(speedKMH))
			speedKMH = np.random.random()
			animate(i, speedKMH, f)
			i += 1

		elif(isinstance(message, SensorData) and message.getSensorId() == "3"):
			var4.set('Current: ' + str(message.getData()))
		
		start = float(datetime.now().strftime('%S.%f')[:-3])
		speedKMH = np.random.random()
		#animate(i, speedKMH, f)
		i += 1
		root.update()
		end = float(datetime.now().strftime('%S.%f')[:-3])
		print end - start
		time.sleep(0.05)
	
	except KeyboardInterrupt:
		sys.exit
		print "Application closed"




