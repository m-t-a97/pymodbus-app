import time

from pyModbusTCP.server import DataBank

from ..readers.serial_reader import SerialReader 

class MicrobitController:
	def __init__(self, serial_port, modbus_client):
		self.serial_port = serial_port
		self.modbus_client = modbus_client
		
	def execute(self):
		try:
			serial_reader = SerialReader(self.serial_port)  
			
			while True:
				data_from_serial_port = serial_reader.read_serial_data()
				
				if data_from_serial_port != "":		
					split_parts = data_from_serial_port.strip().split(",")

					temperature = int(split_parts[0])
					lightLevel = int(split_parts[1])	
					
					self.modbus_client.write_multiple_registers(0, [temperature, lightLevel] )
					print(f"temperature: {temperature}, light level: {lightLevel}")
					
					time.sleep(1)						
				
		except Exception as e:
			print(e)
