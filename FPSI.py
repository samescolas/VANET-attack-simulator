from attacker import Attacker

class FPSI(Attacker):
	attack_type = 'FPSI'

	def __init__(self, car, network):
		super().__init__(car, network, self.attack_type)
		self.attack_type = 'FPSI'

	def attack(self):
		print('FPSI -- forging a path using a single ID')
