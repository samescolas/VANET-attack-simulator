class Attacker:
	types = ['FRPSI', 'FRPMI', 'FPSI', 'FPMI']
	def __init__(self, car, network, attack_type):
		self.car = car
		self.network = network
		self.attach_type = attack_type
