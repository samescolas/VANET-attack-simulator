import pprint
import json
import os

class Config:
	def __init__(self):
		if os.path.isfile('./config.json'):
			with open('./config.json', 'r') as fd:
				c = json.loads(fd.read())
				fd.close()
		else:
			c = {}
		self.STEPS = c['STEPS'] if 'STEPS' in c else 10
		self.X_MIN = c['X_MIN'] if 'X_MIN' in c else 0
		self.X_MAX = c['X_MAX'] if 'X_MAX' in c else 100
		self.Y_MIN = c['Y_MIN'] if 'Y_MIN' in c else 0
		self.Y_MAX = c['Y_MAX'] if 'Y_MAX' in c else 100
		self.V_MIN = c['V_MIN'] if 'V_MIN' in c else 0
		self.V_MAX = c['V_MAX'] if 'V_MAX' in c else 10
		self.PCT_FRPMI = c['PCT_FRPMI'] if 'PCT_FRPMI' in c else 0.25
		self.PCT_FRPSI = c['PCT_FRPSI'] if 'PCT_FRPSI' in c else 0.25
		self.PCT_FPMI = c['PCT_FPMI'] if 'PCT_FPMI' in c else 0.25
		self.PCT_FPSI = c['PCT_FPSI'] if 'PCT_FPSI' in c else 0.25
		self.PCT_NORMAL = c['PCT_NORMAL'] if 'PCT_NORMAL' in c else 0.8
		self.POP_SIZE = c['POP_SIZE'] if 'POP_SIZE' in c else 100
		self.DATA_FILE = c['DATA_FILE'] if 'DATA_FILE' in c else 'data.csv'
