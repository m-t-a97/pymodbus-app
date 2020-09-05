# ------------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------------

from time import sleep

from pyModbusTCP.client import ModbusClient

# ------------------------------------------------------------------

# ------------------------------------------------------------------
# MAIN CODE
# ------------------------------------------------------------------

def main():
	try:
		client = ModbusClient("192.168.0.118", 10503)	
		print("Client open:", client.open())
		
		while True:
			print(client.read_holding_registers(0, 5))
			sleep(1)
			
	except Exception as e:
		client.close()
		print(e)
		
main()

# ------------------------------------------------------------------

