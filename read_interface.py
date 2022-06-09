

class reader(object):
	range : tuple
	curr : int
	read_fn : None
	file : None

	def __init__(self, min : int, max : int) -> None:
		self.range = (min, max)
		self.curr = 0
		# self.file = open('nums.txt', 'w')
		# for i in range(44):
		#     self.file.write(f'{i}\n')
		# self.file.close()

		self.file = open('nums.txt', 'r')

	def min(self) -> int:
		return self.range[0]

	def max(self) -> int:
		return self.range[1]

	def read(self) -> int:
		rd = self.file.readline()
		if rd:
			self.curr = int(rd)
		else:
			self.curr = self.max()//2
		return self.curr
	
	def inrange(self, rang : int) -> int:
		return int((self.curr / self.max()) * rang)

