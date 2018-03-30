from attacker import Attacker

class FRPSI(Attacker):
	def __init__(self, car, network, attack_type):
		super().__init__(car, network, attack_type)

	def attack(self):
		print('FRPSI -- forging a random position using single ID')
