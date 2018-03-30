from attacker import Attacker

class FPMI(Attacker):
	attack_type = 'FPMI'

	def __init__(self, car, network):
		super().__init__(car, network, self.attack_type)
		self.attack_type = 'FPMI'

	def attack(self):
		print('FPMI -- forging paths using multiple IDs')
