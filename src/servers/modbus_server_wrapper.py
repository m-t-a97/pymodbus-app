from pyModbusTCP.server import ModbusServer

class ModbusServerWrapper:
	def create_server(self, host, port):
		print(f"HOST: {host}, PORT: {port}")
		return ModbusServer(host, port, no_block = True)
