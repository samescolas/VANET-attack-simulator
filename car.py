from coord import Coord
import itertools
import time
import random
from utils import *

class Car:
	# Incrementing id to uniquely identify car
	id_generator = itertools.count(1)

	def random():
		return Car(rand_x(), rand_y(), rand_z(), rand_z())

	# Instead of GPS positioning we will use a 2d grid
	#	x - 'horizontal' position
	#	y - 'vertical' position
	#	vx - 'horizontal' velocity (negative is 'left')
	#	vy - 'vertical' velocity (negative is 'down')
	def __init__(self, x, y, vx, vy, car_type='normal', attack_type=None):
		self.id = next(self.id_generator)
		self.status = 'normal'
		self.position = Coord(x, y)
		self.speed = Coord(vx, vy)
		self.type = car_type
		self.attack_type = attack_type

	def join_network(self, n):
		self.network = n
		n.join_network(self)

	def step(self):
		self.position.x += self.speed.x
		self.position.y += self.speed.y
		self.speed.x *= random.random()
		self.speed.y *= random.random()
		if 0 < self.speed.x < 0.1:
			self.speed.x -= rand_v()
		elif -0.1 < self.speed.x < 0:
			self.speed.x += rand_v()
		if 0 < self.speed.y < 0.1:
			self.speed.y -= rand_v()
		elif -0.1 < self.speed.y < 0:
			self.speed.y += rand_v()

	def __str__(self):
		def space_string(string, spaces):
			return '{}{}'.format(string, ' '*(spaces - len(string)))
			
		return '{}{}{}'.format(space_string(str(self.position), 15), space_string(str(self.id), 10), self.status)

	def report(self):
		return '{},{},{},{}'.format(self.id,
									str(time.time()).split('.')[0],
									str(self.position.report()),
									str(self.speed.report()))
