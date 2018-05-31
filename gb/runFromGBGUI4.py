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
import tkMessageBox

# Connect to the queue server
conn = boto.sqs.connect_to_region("eu-west-2", aws_access_key_id = "AKIAJAR3NWUEFXUP2DUA", aws_secret_access_key = "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")
receiveQueue = conn.get_queue('Eco2GB')

# Clear the database before running
cleardb()

# Set up the tkinter root and handle exit window event
root = Tk()

def onClose():
	if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
		writeDBToFile()
		root.destroy()

root.protocol("WM_DELETE_WINDOW", onClose)


# Set up variables for the GUI
var1 = StringVar()
var1.set('Throttle: ' + str(-1))
var2 = StringVar()
var2.set('RPM: ' + str(-1))
var3 = StringVar()
var3.set('KM/H: ' + str(-1))
var4 = StringVar()
var4.set('Current 1: ' + str(-1))
var5 = StringVar()
var5.set('Current 2: ' + str(-1))

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
l5 = Label(root, textvariable = var5)
l5.config(font=("Courier", 50))
l5.pack()

# Add a button for writing the log file to the GUI
B = Button(root, text ="Make log file", command = writeDBToFile)
B.config(font=("Courier", 25))
B.pack()

# Set up the graph variables for the GUI
#LARGE_FONT= ("Verdana", 12)
#style.use("ggplot")
#f = Figure(figsize=(20,20), dpi=100)
#a = f.add_subplot(111)
#a.set_title('My Plot Title')

#xList = deque(maxlen=50)
#yList = deque(maxlen=50)

#def animate(i, speed, f):
	#xList.append(i)
	#yList.append(speed)
	#a.clear()
	#a.plot(xList, yList)

	#start = float(datetime.now().strftime('%S.%f')[:-3])
	#f.canvas.draw()
	#f.canvas.flush_events()
	#end = float(datetime.now().strftime('%S.%f')[:-3])
	#print end - start


#canvas = FigureCanvasTkAgg(f, root)
#canvas.show()
#canvas.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=True)
#canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

throttle, rpm, current, voltage = 0, 0, 0, 0
latestvalues = {'throttle':throttle,'rpm':rpm,'current':current,'voltage':voltage,'GPS':(0,0,0,0)}

def retreiveData():
	while True: 
		message = nextMessage(receiveQueue)
		if(isinstance(message, SensorData) and message.getSensorId() == "1"): latestvalues['throttle'] 	= message.getData()
		elif(isinstance(message, SensorData) and message.getSensorId() == "2"): latestvalues['rpm'] 	= message.getData()
		elif(isinstance(message, SensorData) and message.getSensorId() == "3"): latestvalues['current'] 	= message.getData()
		elif(isinstance(message, SensorData) and message.getSensorId() == "4"): latestvalues['voltage'] 	= message.getData()
		elif(isinstance(message, GPS)): latestvalues['GPS'] = (message.getLongtitude(), message.getLattitude(), 0, message.getTimestamp())
		else: pass
		addToDatabase(message)

def GUI():
	while True:
		if(isinstance(message, SensorData) and message.getSensorId() == "1"): 	var1.set('Throttle: ' + str(message.getData()))
		elif(isinstance(message, SensorData) and message.getSensorId() == "2"):
			var2.set('RPM: ' + str(message.getData()))
			speedKMH = rpmToKMHDisplay(message.getData())
			var3.set('KM/H: ' + str(speedKMH))
		elif(isinstance(message, SensorData) and message.getSensorId() == "3"): var4.set('Current 1: ' + str(message.getData()))
		elif(isinstance(message, SensorData) and message.getSensorId() == "4"):	var5.set('Current 2: ' + str(message.getData()))
		root.update()

retreiveData()




if __name__ == '__main__':
	manager = Manager()

	d = 






#	while True:
#		if(isinstance(message, SensorData) and message.getSensorId() == "1"):
#			var1.set('Throttle: ' + str(message.getData()))
#	
#		elif(isinstance(message, SensorData) and message.getSensorId() == "2"):
#			var2.set('RPM: ' + str(message.getData()))
#			speedKMH = rpmToKMHDisplay(message.getData())
#			var3.set('KM/H: ' + str(speedKMH))
#
##		elif(isinstance(message, SensorData) and message.getSensorId() == "3"):
#			var4.set('Current 1: ' + str(message.getData()))
#	
##		elif(isinstance(message, SensorData) and message.getSensorId() == "4"):
#			var5.set('Current 2: ' + str(message.getData()))
#
#		root.update()	
#		time.sleep(0.02)




