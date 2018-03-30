class Coord:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __str__(self):
		return '({}, {})'.format(self.x, self.y)

	def __len__(self):
		return len(str(self.x)) + len(str(self.y)) + 4

	def report(self):
		return '{},{}'.format(self.x, self.y)
