import serial
import time

#open the serial port
ser = serial.Serial('COM4', 9600, timeout=1)

#print to confirm serial port is open
if ser.isOpen():
    print(ser.name + ' is open.')

    list = []
    test1 = 'B'
    test2 = '255'
    test3 = '\r\n'
    ser.write(test1.encode())
    ser.write(test2.encode())
    ser.write(test3.encode())

    while len(list) < 3:
        c = ser.readline().decode()
        list.append(c)

    ser.close()
str(555)
print(list[0])
print(list[1])
print(list[2])