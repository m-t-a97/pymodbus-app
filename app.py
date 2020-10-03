import os
from threading import Thread 

from decouple import config
 
from src.servers.modbus_server_wrapper import ModbusServerWrapper
from src.clients.modbus_client_wrapper import ModbusClientWrapper
from src.controllers import MicrobitController, LedController, DHTSensorController, DistanceSensorController

host = os.getenv("IP", "127.0.0.1")
port = config("PORT", default = 502, cast = int)
modbus_server = ModbusServerWrapper().create_server(host, port)

microbit_modbus_client = ModbusClientWrapper(host, port)
led_modbus_client = ModbusClientWrapper(host, port)
sensor_modbus_client = ModbusClientWrapper(host, port)
distance_sensor_modbus_client = ModbusClientWrapper(host, port)

def main():
	try:
		modbus_server.start()

		microbit_modbus_client.open()
		led_modbus_client.open()
		sensor_modbus_client.open()
		distance_sensor_modbus_client.open()

		microbit_thread = Thread(target = run_microbit)
		microbit_thread.start()
		
		led_thread = Thread(target = run_led)
		led_thread.start()

		sensor_thread = Thread(target = run_sensor)
		sensor_thread.start()

		distance_sensor_thread = Thread(target = run_distance_sensor)
		distance_sensor_thread.start()

	except Exception as e:
		modbus_server.stop()
		microbit_modbus_client.close()
		led_modbus_client.close()
		sensor_thread.close()
		distance_sensor_thread.close()
		print(e) 

def run_microbit():
	microbit_serial_port = "/dev/ttyACM0"
	microbit_controller = MicrobitController(microbit_serial_port, microbit_modbus_client)
	microbit_controller.execute()

def run_led():
	led_controller = LedController(led_modbus_client, 12, 25)
	led_controller.execute()

def run_sensor():
	sensor_controller = DHTSensorController(sensor_type = 11, pin = 4, modbus_client = sensor_modbus_client)
	sensor_controller.execute()

def run_distance_sensor():
	distance_sensor_controller = DistanceSensorController(echo = 24, trigger = 23, modbus_client = distance_sensor_modbus_client)
	distance_sensor_controller.execute()

main()
