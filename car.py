from coord import Coord
import itertools
import time
import random
from utils import *
from config import Config

conf = Config()

class Car:
	# Incrementing id to uniquely identify car
	id_generator = itertools.count(1)

	def random():
		return Car(rand_x(), rand_y(), rand_v(), rand_v())

	# Instead of GPS positioning we will use a 2d grid
	######################################################
	#	x			-	'horizontal' position
	#	y			-	'vertical' position
	#	vx			-	'horizontal' velocity (negative is 'left')
	#	vy			-	'vertical' velocity (negative is 'down')
	#	car_type	-	normal, attacker, or virtual (attacker spoofed)
	#	attack_type	-	FRMSI,FRPMI,FPSI,FPMI (see classes for more detail)
	######################################################

	def __init__(self, x, y, vx, vy, car_type='normal', attack_type=None):
		self.id = next(self.id_generator)
		self.position = Coord(x, y)
		self.speed = Coord(vx, vy)
		self.type = car_type
		self.generate_xpath()
		self.generate_ypath()
		self.attack_type = attack_type
		self.network = None

	def join_network(self, n):
		self.network = n
		n.join_network(car=self)

	def randomize(self):
		self.position.x = rand_x()
		self.position.y = rand_y()
		self.speed.x = rand_v()
		self.speed.y = rand_v()

	def step(self):
		self.stepx()
		self.stepy()
		if self.network.position_taken(self.position):
			# go back to where you came from
			self.position.x -= self.speed.x
			self.position.y -= self.speed.y
			# update path to positioni self back where you were
			# going last time. Think stop sign
			self.xpath = [self.position.x] + self.xpath
			self.ypath = [self.position.y] + self.ypath

	def stepy(self):
		if self.ypath == None or len(self.ypath) == 0:
			if int(self.speed.y) == 0:
				self.speed.y = rand_v() - (conf.V_MAX / 2)
			self.ypath = self.generate_ypath()
		else:
			self.y = self.ypath.pop(0)
	def stepx(self):
		if self.xpath == None or len(self.xpath) == 0:
			if int(self.speed.x) == 0:
				self.speed.x = rand_v() - (conf.V_MAX / 2)
			self.xpath = self.generate_xpath()
		else:
			self.x = self.xpath.pop(0)

	def generate_xpath(self):
		self.xpath = [self.position.x + (i * self.speed.x) for i in range(10)]

	def generate_ypath(self):
		self.ypath = [self.position.y + (i * self.speed.y) for i in range(10)]

	def __str__(self):	
		return '{}{}{}{}'.format(space_string(str(self.position), 15),
								 space_string(str(self.id), 10),
								 space_string(self.type, 20),
								 self.attack_type if not not self.attack_type else '')

	def report(self):
		return '{},{},{},{},{},{}'.format(self.id,
									str(time.time()).split('.')[0],
									str(self.position.report()),
									str(self.speed.report()),
									self.type,
									self.attack_type)
