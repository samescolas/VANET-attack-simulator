from attacker import Attacker
from car import Car

# Forging Random Posititions using Multiple IDs
class FRPMI(Attacker):
	attack_type = 'FRPMI'

	def __init__(self, car, network, num_spoofs=2):
		super().__init__(car, network, self.attack_type)
		self.spoofs = [Car.random() for i in range(num_spoofs)]
		for s in self.spoofs:
			s.type = 'virtual'
			s.attack_type = self.attack_type
			s.network = network

	def attack(self):
		check = set()
		for i,s in enumerate(self.spoofs):
			while len(check) < i:
				s.randomize()
				check.add((s.position.x, s.position.y))
			self.network.inject_point(s)
