# ------------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------------

import os
from time import sleep

from decouple import config
from pyModbusTCP.client import ModbusClient

# ------------------------------------------------------------------

# ------------------------------------------------------------------
# MAIN CODE
# ------------------------------------------------------------------

def main():
	try:
		client = ModbusClient(config("HOST", default = "127.0.0.1"), config("PORT", default = 502, cast = int))
		print("Client open:", client.open())
		
		while True:
			print(client.read_holding_registers(0, 5))
			sleep(1)
			
	except Exception as e:
		client.close()
		print(e)
		
main()

# ------------------------------------------------------------------

