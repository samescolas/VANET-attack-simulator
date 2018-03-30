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

def rand_car():
	return Car(rand_x(), rand_y(), rand_v(), rand_v())

def rand_attacker():
	n = random()
	c = rand_car()
	c.type = 'attacker'

	if n < 0.25:
		c.attack_type = 'FRPMI'
		attacker = FRPMI()
	elif n < 0.5:
		c.attack_type = 'FRPSI'
		attacker = FRPSI()
	elif n < 0.75:
		c.attack_type = 'FPSI'
		attacker = FPSI()
	else:
		c.attack_type = 'FPMI'
		attacker = FPMI()
	return attacker

conf = Config()

cars = [rand_car() for i in range(int(conf.PCT_NORMAL * conf.POP_SIZE))]
attackers = [rand_attacker() for i in range(int(1 - conf.PCT_NORMAL * conf.POP_SIZE))]
network = Network(cars, attackers)

steps = conf.STEPS

while steps != 0:
	network.step()
	network.report()
	print()
	print()
	steps -= 1

print('Completed')
