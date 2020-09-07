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
			data_read_as_bytes = self.serial.readline()
			data_converted_from_bytes_to_string = self.convert_bytes_to_string(data_read_as_bytes)	
			return self.remove_spaced_characters_from_serial_data(data_converted_from_bytes_to_string)		
			
		except Exception as e:
			print(e)
		
		return ""

	def convert_bytes_to_string(self, bytes):
		data_to_string = str(bytes.decode("utf-8"))
		return data_to_string
		
	def remove_spaced_characters_from_serial_data(self, data):
		return data.replace("\r\n", "")
		
	def get_serial_port(self):
		return self.serial

