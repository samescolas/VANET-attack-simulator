from attacker import Attacker

class FRPMI(Attacker):
	attack_type = 'FRPMI'

	def __init__(self, car, network):
		super().__init__(car, network, self.attack_type)

	def attack(self):
		print('FRPMI -- forging a random position using multiple IDs')
