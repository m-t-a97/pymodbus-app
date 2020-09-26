import time

from pyModbusTCP.server import DataBank

from ..readers.serial_reader import SerialReader 

class MicrobitController:
	def __init__(self, serial_port, modbus_server):
		self.serial_port = serial_port
		self.modbus_server = modbus_server
		
	def read_and_write_data(self):
		try:
			self.modbus_server.start()
			
			serial_reader = SerialReader(self.serial_port)  
			
			while True:
				data_from_serial_port = serial_reader.read_serial_data()
				
				if data_from_serial_port != "":		
					split_parts = data_from_serial_port.strip().split(",")

					temperature = int(split_parts[0])
					lightLevel = int(split_parts[1])	
					
					DataBank.set_words(0, [temperature])
					DataBank.set_words(1, [lightLevel])
					print(f"temperature: {temperature}, light level: {lightLevel}")
					
					time.sleep(1)						
				
		except Exception as e:
			self.modbus_server.stop()
			print(e)
