from attacker import Attacker

class FPMI(Attacker):
	def __init__(self, car, network, attack_type):
		super().__init__(car, network, attack_type)

	def attack(self):
		print('FPMI -- forging paths using multiple IDs')
