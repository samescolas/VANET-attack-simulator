from car import Car
from network import Network
from random import randint
from attacker import Attacker

POS_MIN = 0
POS_MAX = 100

def rng_pos():
	return randint(POS_MIN, POS_MAX)

cars = [Car(rng_pos(), rng_pos(), rng_pos(), rng_pos()) for i in range(100)]
network = Network(cars)

print(network.step())
