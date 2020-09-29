import os
from threading import Thread 

from decouple import config
 
from src.servers.modbus_server_wrapper import ModbusServerWrapper
from src.clients.modbus_client_wrapper import ModbusClientWrapper
from src.controllers import MicrobitController, LedController

host = os.getenv("IP", "127.0.0.1")
port = config("PORT", default = 502, cast = int)
modbus_server = ModbusServerWrapper().create_server(host, port)
microbit_modbus_client = ModbusClientWrapper(host, port)
led_modbus_client = ModbusClientWrapper(host, port)

def main():
	try:
		modbus_server.start()
		microbit_modbus_client.open()
		led_modbus_client.open()

		microbit_thread = Thread(target = run_microbit)
		microbit_thread.start()
		
		led_thread = Thread(target = run_led)
		led_thread.start()

	except Exception as e:
		modbus_server.stop()
		microbit_modbus_client.close()
		led_modbus_client.close()
		print(e) 

def run_microbit():
	microbit_serial_port = "/dev/ttyACM0"
	microbit_controller = MicrobitController(microbit_serial_port, microbit_modbus_client)
	microbit_controller.read_and_write_data()

def run_led():
	led_controller = LedController(led_modbus_client, 12, 25)
	led_controller.run_led()

main()
