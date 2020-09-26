import time

from gpiozero import Servo

class MotorController:
	def __init__(self, servo_pin, modbus_server, modbus_client):
		self.servo_pin = servo_pin
		self.servo = Servo(servo_pin)
		self.modbus_server = modbus_server
		self.modbus_client = modbus_client

	def run_servo(self):
		if self.servo_pin == None:
			print("You must specify the pin that controls the servo on the device...")
			return
		
		try:
			while True:	
				self.write_data_and_wait(-1)
				self.write_data_and_wait(-0.5)
				self.write_data_and_wait(0)
				self.write_data_and_wait(0.5)
				self.write_data_and_wait(1)
			
		except Exception as e:
			print(e)

		finally:
			print(self.modbus_client.write_single_coil(0, False))
			
	def write_data_and_wait(self, servo_value, wait_time = 1):
		self.servo.value = servo_value
		print(f"Servo value: {servo_value}")

		if self.modbus_client.client.is_open():
			is_write_successful = self.modbus_client.write_single_coil(0, True)
			print(f"Successfully written: {is_write_successful}")
			coils = self.modbus_client.read_coils(0, 1)
			print(coils)
		
		time.sleep(wait_time)
