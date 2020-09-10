# ------------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------------

import serial

# ------------------------------------------------------------------

class SerialReader:
	
	def __init__(self, port):	
		self.port = port
		self.baudrate = 115200
		self.timeout = 1
		self.serial = serial.Serial(port = self.port, baudrate = self.baudrate, timeout = self.timeout)
	
	def read_serial_data(self):
		try:
			data_as_bytes = self.serial.readline()
			data_decoded_as_string = data_as_bytes.decode("UTF-8")
			data_decoded_as_string.replace("\r", "")
			return data_decoded_as_string
			
		except Exception as e:
			print(e)
		
		return ""
		
	def get_serial_port(self):
		return self.serial

