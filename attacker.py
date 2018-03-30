from utils import space_string

class Attacker:
	types = ['FRPSI', 'FRPMI', 'FPSI', 'FPMI']

	def __init__(self, car, network, attack_type):
		self.attack_type = attack_type
		self.setup_car(car, network)
		self.join_network(network)

	def setup_car(self, car, network):
		self.car = car
		self.car.type = 'attacker'
		self.car.join_network(network)
		self.car.attack_type = self.attack_type

	def __str__(self):
		return str(self.car)

	def join_network(self, network):
		self.network = network
		network.join_network(attacker=self)
