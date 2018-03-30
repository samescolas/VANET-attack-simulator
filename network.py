from config import Config
from random import shuffle

conf = Config()

class Network:
	
	# The network that contains the friendly
	# cars and the misbehaving attacker cars
	def __init__(self, normal_cars, attackers):
		self.normal_cars = normal_cars
		self.attackers = attackers
		self.injected_points = []
		self.occupied = {}
		for car in normal_cars:
			while self.position_taken(car.position):
				car.randomize()
			self.occupy(car.position)

	def __str__(self):
		return "\n".join([str(car) for car in self.normal_cars])

	def step(self):
		self.occupied = {}
		for car in self.normal_cars:
			car.step()
		for attacker in self.attackers:
			attacker.attack()

	def report(self):
		reports = []
		while len(self.injected_points) > 0:
			car = self.injected_points.pop(0)
			#print(car.report())
			reports.append(car.report())
		for attacker in self.attackers:
			#print(attacker.car.report())
			reports.append(attacker.car.report())
		for car in self.normal_cars:
			#print(car.report())
			reports.append(car.report())
		shuffle(reports)
		print('\n'.join(reports))

	def inject_point(self, car):
		self.injected_points.append(car)
		self.occupied[car.position] = True

	def occupy(self, pos):
		self.occupied[pos] = True
	
	def position_taken(self, pos):
		return pos in self.occupied
