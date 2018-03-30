from attacker import Attacker
from car import Car

# Forging Path using Multiple IDs
class FPMI(Attacker):
	attack_type = 'FPMI'

	def __init__(self, car, network, num_spoofs=2):
		super().__init__(car, network, self.attack_type)
		self.attack_type = 'FPMI'
		self.spoof_cars = [Car.random() for i in range(num_spoofs)]
		for car in self.spoof_cars:
			car.type = 'virtual'
			car.attack_type = self.attack_type
			car.network = network

	def attack(self):
		for car in self.spoof_cars:
			self.network.inject_point(car)
			car.step()
