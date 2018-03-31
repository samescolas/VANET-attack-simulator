from random import randint,random

from car import Car
from network import Network
from attacker import Attacker

from FPSI import FPSI
from FPMI import FPMI
from FRPMI import FRPMI
from FRPSI import FRPSI

from config import Config

from utils import *

conf = Config()

# create a random attacker using
# % vals in config.json
def random_attacker(network):
	n = random()
	c = Car.random()

	if n < conf.PCT_FRPMI:
		attacker = FRPMI(c, network)
	elif n < conf.PCT_FRPMI + conf.PCT_FRPSI:
		attacker = FRPSI(c, network)
	elif n < conf.PCT_FRPMI + conf.PCT_FRPSI + conf.PCT_FPSI:
		attacker = FPSI(c, network)
	else:
		attacker = FPMI(c, network)
	return attacker

# generate 80% normal cars
cars = [Car.random() for i in range(int(conf.PCT_NORMAL * conf.POP_SIZE))]

# create empty network
network = Network(cars, [])

# generate 20% attackers distributed according to config
attackers = [random_attacker(network) for i in range(int((1.0 - conf.PCT_NORMAL) * conf.POP_SIZE))]

# add cars to network
for c in cars:
	c.network = network

# add attackers to network
network.attackers = attackers

# define number of steps in simulation
steps = conf.STEPS

while steps != 0:
	print('STEPS REMAINING {}'.format(steps))
	# step propagates updates to all members of network
	network.step()
	# report current positions and statuses of all vehicles including
	# attackers and virtual cars
	network.report()
	steps -= 1
