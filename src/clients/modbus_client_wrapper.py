import time

from pyModbusTCP.client import ModbusClient

from ..models.daos.modbus_dao import ModbusDao

class ModbusClientWrapper(ModbusDao):
	def __init__(self, host, port):
		self.client = ModbusClient(host, port)

	def open(self):
		self.client.open()
		print(f"A client opened: {self.client.is_open()}")

	def close(self):
		self.client.close()
	
	def write_single_coil(self, address, value):
		return self.client.write_single_coil(address, value)
		
	def write_multiple_coils(self, address, value):
	  return self.client.write_multiple_coils(address, value)

	def write_single_register(self, address, value):
		return self.client.write_single_register(address, value)
	
	def write_multiple_registers(self, address, value):
	  return self.client.write_multiple_registers(address, value)
	
	def read_coils(self, address, value):
	  return self.client.read_coils(address, value)
	
	def read_discrete_inputs(self, address, value):
	  return self.client.read_discrete_inputs(address, value)
	
	def read_input_registers(self, address, value):
	  return self.client.read_input_registers(address, value)
	
	def read_holding_registers(self, address, value):
	  return self.client.read_holding_registers(address, value)
		