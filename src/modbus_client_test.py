from time import sleep

from decouple import config
from pyModbusTCP.client import ModbusClient

def main():
	try:
		client = ModbusClient(config("HOST", default = "127.0.0.1"), config("PORT", default = 502, cast = int))
		print("Client open:", client.open())
		
		client.write_single_register(2, 100)
		client.write_single_register(3, 200)
		client.write_single_register(4, 300)
		client.write_single_register(5, 400)
		print(client.read_holding_registers(0, 5))
			
	except Exception as e:
		client.close()
		print(e)
		
main()
