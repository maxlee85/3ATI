import tkinter
from tkinter import *
import serial
import time

def setBrightness():
    #Open serial port
    ser = serial.Serial('COM4', 9600, timeout=1)
    print('Running setBrightness')
    #Declare variables
    list = []
    test1 = 'B'
    test2 = str(d1.get())
    test3 = '\r\n'

    #Issue commands to serial port
    ser.write(test1.encode())
    ser.write(test2.encode())
    ser.write(test3.encode())

    #Write output to list
    while len(list) < 3:
        c = ser.readline().decode()
        list.append(c)

    #Close serial port
    ser.close()
    print(list[2])
    print('Running showBrightness')
    return list[2]

def showBrightness():
    int = setBrightness()
    print(int)
    label = tkinter.Label(w, text=int, width=5).grid(row=3, column=3, padx=1, pady=1)
    return

def getVoltage():
    return

def getOptimumTemp():
    return

def setTemperature():
    return

def setVoltage():
    return

def setDigipot():
    return

def Quit():
    w.destroy()

w = Tk()

#Creates list of push buttons
Button(w, text="Set Temp", command=setTemperature).grid(row=1, column=0, padx=2, pady=2)
Button(w, text="Set Brightness", command=showBrightness).grid(row=1, column=1, padx=2, pady=2)
Button(w, text="Set DigiPot", command=setDigipot).grid(row=1, column=2, padx=2, pady=2)
Button(w, text="Find Optimum Temp", command=getOptimumTemp).grid(row=9, column=1, padx=2, pady=2)
Button(w, text="Exit", command=Quit).grid(row=9, column=2, padx=2, pady=2)
Button(w, text="Set All", command=getOptimumTemp).grid(row=9, column=0, padx=2, pady=2)

#Creates quit button
#Button(w, text='Quit', command=w.quit).grid(row=10, sticky=W, pady=4)

#Creates list of labels
Label(w, text="Brightness").grid(column=1, row=3)
Label(w, text="Backlight Temperature (25-70 Deg C)").grid(column=1, row=4)
Label(w, text="Backlight BIT").grid(column=1, row=5)
Label(w, text="5vRef").grid(column=1, row=6)
Label(w, text="DigiPot Voltage (0.0 - 5.0)").grid(column=1, row=7)

#Creates list of labels being displayed and for user entry
d1 = Entry(w, width=5)
d1.grid(row=3, column=0, pady=2)
d2 = Entry(w, width=5)
d2.grid(row=4, column=0, pady=2)
d3 = Entry(w, width=5)
d3.grid(row=5, column=0, pady=2)
d4 = Entry(w, width=5)
d4.grid(row=6, column=0, pady=2)
d5 = Entry(w, width=5)
d5.grid(row=7, column=0, pady=2)

w.mainloop()