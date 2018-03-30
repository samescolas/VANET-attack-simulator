from utils import space_string
from random import random
from car import Car

class Attacker:
	types = ['FRPSI', 'FRPMI', 'FPSI', 'FPMI']

	def __init__(self, car, network, attack_type):
		self.attack_type = attack_type
		self.car = car
		self.car.type = 'attacker'
		self.car.network = network
		self.car.attack_type = self.attack_type
		self.network = network

	def __str__(self):
		return str(self.car)

	def step(self):
		self.attack()
