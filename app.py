import os
from threading import Thread 

from decouple import config
 
from src.servers.modbus_server_wrapper import ModbusServerWrapper
from src.clients.modbus_client_wrapper import ModbusClientWrapper
from src.controllers import MicrobitController, LedController, DHTSensorController, DistanceSensorController

host = os.getenv("IP", "127.0.0.1")
port = config("PORT", default = 502, cast = int)
modbus_server = ModbusServerWrapper().create_server(host, port)

def main():
	try:
		modbus_server.start()
		create_and_run_thread(run_microbit)
		#create_and_run_thread(run_led)
		#create_and_run_thread(run_sensor)
		#create_and_run_thread(run_distance_sensor)
	except Exception as e:
		modbus_server.stop()
		print(e) 

def create_and_run_thread(target_function):
		thread = Thread(target = target_function)
		thread.start()

def run_microbit():
	try:
		modbus_client = create_and_get_new_modbus_client()
		microbit_serial_port = "/dev/ttyACM0"
		microbit_controller = MicrobitController(microbit_serial_port, modbus_client)
		microbit_controller.execute()
	except Exception as e:
		modbus_client.close()
		print(e)

def run_led():
	try:
		modbus_client = create_and_get_new_modbus_client()
		led_controller = LedController(modbus_client, 12, 25)
		led_controller.execute()
	except Exception as e:
		modbus_client.close()
		print(e)

def run_sensor():
	try:
		modbus_client = create_and_get_new_modbus_client()
		sensor_controller = DHTSensorController(sensor_type = 11, pin = 4, modbus_client = modbus_client)
		sensor_controller.execute()
	except Exception as e:
		modbus_client.close()
		print(e)

def run_distance_sensor():
	try:
		modbus_client = create_and_get_new_modbus_client()
		distance_sensor_controller = DistanceSensorController(echo = 24, trigger = 23, modbus_client = modbus_client)
		distance_sensor_controller.execute()
	except Exception as e:
		modbus_client.close()
		print(e)

def create_and_get_new_modbus_client():
	modbus_client = ModbusClientWrapper(host, port)
	modbus_client.open()
	return modbus_client

main()
