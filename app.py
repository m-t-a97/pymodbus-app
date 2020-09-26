import os

from decouple import config
 
from src.servers.modbus_server_wrapper import ModbusServerWrapper
from src.controllers import MicrobitController, MotorController
from src.clients.modbus_client_wrapper import ModbusClientWrapper

def main():
	host = os.getenv("IP", "127.0.0.1")
	port = config("PORT", default = 502, cast = int)
	
	# microbit_serial_port = "/dev/ttyACM0"
	# micobit_modbus_server = ModbusServerWrapper().create_server(host, port)
	# microbit_controller = MicrobitController(microbit_serial_port, micobit_modbus_server)
	# microbit_controller.read_and_write_data()
	
	motor_modbus_server = ModbusServerWrapper().create_server(host, port)
	motor_modbus_server.start()

	motor_modbus_client = ModbusClientWrapper(host, port)
	motor_modbus_client.open()

	motor_controller = MotorController(18, motor_modbus_server, motor_modbus_client)
	motor_controller.run_servo()

	motor_modbus_server.stop()
	motor_modbus_client.close()

main()
