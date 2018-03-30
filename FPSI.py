from attacker import Attacker

class FPSI(Attacker):
	def __init__(self, car, network, attack_type):
		super().__init__(car, network, attack_type)

	def attack(self):
		print('FPSI -- forging a path using a single ID')
