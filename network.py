class Network:
	def __init__(self, cars, attackers):
		self.cars = cars
		self.size = len(cars)
		self.attackers = attackers

	def __str__(self):
		return "\n".join([str(car) for car in self.cars])

	def step(self):
		for car in self.cars:
			car.step()
		print("ATTACKING")
		for attacker in self.attackers:
			attacker.attack()

	def report(self):
		for car in self.cars:
			print(car.report())

	def join_network(self, **kwargs):
		if 'car' in kwargs:
			self.cars.append(kwargs['car'])
		if 'attacker' in kwargs:
			self.attackers.append(kwargs['attacker'])
