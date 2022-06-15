import serial

adc1 = 0
adc2 = 0

class reader(object):
	min : int
	max : int
	readlist : list
	port : serial.Serial

	def __init__(self, min:int, max:int) -> None:
		self.min = min
		self.max = max
		self.readlist = [0, 0]
		self.port = serial.Serial(port="COM3", baudrate=9600, bytesize=8, 
			timeout=1, stopbits=serial.STOPBITS_ONE)

	def readtxt(self) -> bytes:
		# global adc1
		# global adc2
		# adc1 %= 255
		# adc2 %= 255
		# adc1 += 1
		# adc2 += 1
		# return f'{adc1},{adc2}'
		# return "0,255"
		return self.port.readline().decode('Ascii')

	def loadvals(self) -> None:
		rcv = self.port.readline()
		txt = rcv.decode('Ascii')
		vals = txt.split(',')
		self.readlist[0] = int(vals[0])
		self.readlist[1] = int(vals[1])

	def getrd(self, id : int) -> int :
		return self.readlist[id]

	def poll(self) -> list:
		self.loadvals()
		return self.readlist

	def inrange(self, id : int, maxrange : int) -> int:
		return int((self.getrd(id) / self.max) * (maxrange - 1))
