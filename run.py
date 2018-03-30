from random import randint,random

from car import Car
from network import Network
from attacker import Attacker

from FRPMI import FRPMI
from FRPSI import FRPSI
from FPMI import FPMI
from FPSI import FPSI

from config import Config

from utils import *

def rand_car(car_type='normal'):
	return Car(rand_x(), rand_y(), rand_v(), rand_v(), car_type)

def rand_attacker(network):
	n = random()
	c = rand_car('attacker')

	if n < 0.25:
		attacker = FRPMI(c, network)
	elif n < 0.5:
		attacker = FRPSI(c, network)
	elif n < 0.75:
		attacker = FPSI(c, network)
	else:
		attacker = FPMI(c, network)
	return attacker

conf = Config()

cars = [rand_car() for i in range(int(conf.PCT_NORMAL * conf.POP_SIZE))]
network = Network(cars, [])
attackers = [rand_attacker(network) for i in range(int((1.0 - conf.PCT_NORMAL) * conf.POP_SIZE))]

steps = conf.STEPS# - conf.STEPS

while steps != 0:
	network.step()
	network.report()
	print()
	print()
	steps -= 1

print('Completed')
