from tkinter import *
import random
import serial
import time

def readSerial(*commands):

    #Open serial port
    #ser = serial.Serial('/dev/tty.usbmodem1412', 9600, timeout=1) Python
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

    for i in commands:
        ser.write(i.encode())
        time.sleep(.05)

    #Declare variables
    list = []

    #Write output to list
    while True:
        c = ser.readline().decode()
        if len(c) == 0:
            break
        list.append(c)

    #Print output
    for i in list:
        print(i)

    #Close serial port
    ser.close()

    return list

def setBrightness():

    #Create serial port commands
    test1 = 'B'
    test2 = str(d1.get())
    test3 = '\r\n'

    #Declare variables
    int = readSerial(test1, test2, test3)
    brightnessEntry = StringVar()

    #Set and update display values
    Entry(w, textvariable=brightnessEntry, width=6).grid(row=3, column=3, pady=2)
    brightnessEntry.set(int[-1])

    return

def setTemperature():

    #Create serial port commands
    test1 = 'T'
    test2 = str(d3.get())
    test3 = '\r\n'

    #Declare variables
    int = readSerial(test1, test2, test3)
    temperatureEntry = StringVar()

    #Set and update display values
    Entry(w, textvariable=temperatureEntry, width=6).grid(row=5, column=3, pady=2)
    temperatureEntry.set(int[-2])

    return

def setDigipot():

    #Create serial port commands
    test1 = 'D'
    test2 = str(d6.get())
    test3 = '\r\n'

    #Declare variables
    list = readSerial(test1, test2, test3)
    voltageEntry = StringVar()
    deltaEntry = StringVar()
    failEntry = StringVar()

    #Check if digipot setup failed
    if len(list[-6]) == 9:
        failEntry.set(list[-6])
    else:
        failEntry.set('Success')

    #Set and update display values
    Entry(w, textvariable=voltageEntry, width=6).grid(row=8, column=3, pady=2)
    voltageEntry.set(list[-4])
    Entry(w, textvariable=deltaEntry, width=6).grid(row=9, column=3, pady=2)
    deltaEntry.set(list[-2])
    Entry(w, textvariable=failEntry, width=6).grid(row=9, column=1, pady=2)

    return

def getVoltage():

    #Create serial port commands
    test1 = 'V'
    test2 = '\r\n'

    #Declare variables
    list = readSerial(test1, test2)
    brightnessEntry = StringVar()
    backlightTemp = StringVar()
    backlightBIT = StringVar()
    vRef = StringVar()

    #Set and update display values
    Entry(w, textvariable=brightnessEntry, width=6).grid(row=4, column=3, pady=2)
    brightnessEntry.set(list[1])
    Entry(w, textvariable=backlightTemp, width=6).grid(row=5, column=3, pady=2)
    backlightTemp.set(list[3])
    Entry(w, textvariable=backlightBIT, width=6).grid(row=6, column=3, pady=2)
    backlightBIT.set(list[5])
    Entry(w, textvariable=vRef, width=5).grid(row=7, column=3, pady=2)
    vRef.set(list[7])

    return

def getOptimumTemp():
    return

def Quit():
    w.destroy()

def openCanvas():

    #Creates new tkinter window and canvas
    root = Toplevel()
    width, height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (width, height))
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()

    #Function that changes image on click
    def click(event):
        global imageNum
        canvas.create_image(0, 0, image=imageList[imageNum])
        imageNum += 1
        if imageNum == 6:
            imageNum = 0
            root.destroy()

    #Bind command to canvas
    canvas.bind("<Button-1>", click)

    root.mainloop()
    return

w = Tk()

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
d6 = Entry(w, width=5)
d6.grid(row=8, column=0, pady=2)
d7 = Entry(w, width=5)
d7.grid(row=9, column=0, pady=2)

#Creates list of push buttons
Button(w, text="Set Temp", command=setTemperature).grid(row=5, column=1, padx=2, pady=2)
Button(w, text="Set Brightness", command=setBrightness).grid(row=3, column=1, padx=2, pady=2)
Button(w, text="Set DigiPot", command=setDigipot).grid(row=8, column=1, padx=2, pady=2)
Button(w, text="Find Optimum Temp", command=getOptimumTemp).grid(row=10, column=1, padx=2, pady=2)
Button(w, text="Image Test", command=openCanvas).grid(row=10, column=2, padx=2, pady=2)
Button(w, text="Exit", command=Quit).grid(row=10, column=3, padx=2, pady=2)
Button(w, text="Find Voltage", command=getVoltage).grid(row=10, column=0, padx=2, pady=2)

#Creates list of labels
Label(w, text="Brightness").grid(column=2, row=3, pady=2)
Label(w, text="Brightness (V) ").grid(column=2, row=4, pady=2)
Label(w, text="Backlight Temperature (25-70 Deg C)").grid(column=2, row=5, pady=2)
Label(w, text="Backlight BIT").grid(column=2, row=6, pady=2)
Label(w, text="5vRef").grid(column=2, row=7, pady=2)
Label(w, text="DigiPot Voltage (0.0 - 5.0)").grid(column=2, row=8, pady=2)
Label(w, text="DigiPot Delta (0.0 - 5.0)").grid(column=2, row=9, pady=2)

#Creates list of images
image1 = PhotoImage(file="/Users/maxwell/Downloads/ImageTest/Red.gif")
image2 = PhotoImage(file="/Users/maxwell/Downloads/ImageTest/Blue.gif")
image3 = PhotoImage(file="/Users/maxwell/Downloads/ImageTest/Green.gif")
image4 = PhotoImage(file="/Users/maxwell/Downloads/ImageTest/Vert.gif")
image5 = PhotoImage(file="/Users/maxwell/Downloads/ImageTest/Hori.gif")
image6 = PhotoImage(file="/Users/maxwell/Downloads/ImageTest/Grid.gif")
imageList = [image1, image2, image3, image4, image5, image6]
imageNum = 0

w.mainloop()
