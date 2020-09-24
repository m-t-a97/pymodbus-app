# ------------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------------

import time

from decouple import config
from pyModbusTCP.client import ModbusClient

# ------------------------------------------------------------------

# ------------------------------------------------------------------
# MAIN CODE
# ------------------------------------------------------------------

def main():
	try:
		HOST = config("HOST", default = "127.0.0.1")
		PORT = config("PORT", default = 502, cast = int)
		client = ModbusClient(HOST, PORT)
		print("Client open:", client.open())
		
		while True:
			print(client.read_holding_registers(0, 5))
			time.sleep(1)
			
	except Exception as e:
		client.close()
		print(e)
		
main()

# ------------------------------------------------------------------

