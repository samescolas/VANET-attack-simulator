from attacker import Attacker

class FRPSI(Attacker):
	attack_type = 'FRPSI'

	def __init__(self, car, network):
		super().__init__(car, network, self.attack_type)

	def attack(self):
		print('FRPSI -- forging a random position using single ID')
