from attacker import Attacker

class FRPMI(Attacker):
	def __init__(self, car, network, attack_type):
		super().__init__(car, network, attack_type)

	def attack(self):
		print('FRPMI -- forging a random position using multiple IDs')