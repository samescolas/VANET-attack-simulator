from attacker import Attacker
from car import Car

# Forging Path using Single ID
class FPSI(Attacker):
	attack_type = 'FPSI'

	def __init__(self, car, network):
		super().__init__(car, network, self.attack_type)
		self.attack_type = 'FPSI'
		self.spoof_car = Car.random()
		self.spoof_car.type = 'virtual'
		self.spoof_car.attack_type = self.attack_type
		self.spoof_car.id = self.car.id
		self.spoof_car.network = network

	def attack(self):
		self.network.inject_point(self.spoof_car)
		self.spoof_car.step()
