from time import sleep

from pyModbusTCP.client import ModbusClient

def main():
	try:
		client = ModbusClient("192.168.0.118", 10503)
		print("Client open:", client.open())
		
		client.write_single_register(1, 100)
		client.write_single_register(2, 200)
		client.write_single_register(3, 300)
		client.write_single_register(4, 400)
		print(client.read_holding_registers(0, 5))
			
	except Exception as e:
		client.close()
		print(e)
		
main()
