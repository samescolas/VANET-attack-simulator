from random import randint
from config import Config

conf = Config()

def rand_x():
	return randint(conf.X_MIN, conf.X_MAX)

def rand_y():
	return randint(conf.Y_MIN, conf.Y_MAX)

def rand_v():
	return randint(conf.V_MIN, conf.V_MAX)
