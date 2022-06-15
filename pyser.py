from curses import baudrate
from socket import timeout
from time import sleep
import serial

ser = serial.Serial(port="COM3", baudrate=9600, 
	bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE)

while True:
	rcv = ser.readline()
	txt = rcv.decode('Ascii')
	arr = txt.split(',')
	print(int(arr[0]), int(arr[1]))

ser.close()

