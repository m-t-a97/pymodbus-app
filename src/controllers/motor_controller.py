import time

from gpiozero import Servo

class MotorController:
	def __init__(self, servo_pin, modbus_client):
		self.servo_pin = servo_pin
		self.servo = Servo(servo_pin)
		self.modbus_client = modbus_client

	def run_servo(self):
		try:
			while True:	
				self.write_data_and_wait(-1)
				self.write_data_and_wait(-0.5)
				self.write_data_and_wait(0)
				self.write_data_and_wait(0.5)
				self.write_data_and_wait(1)
				
		except Exception as e:
			self.toggle_coil_value(False)
			print(e)
			
	def write_data_and_wait(self, servo_value, wait_time = 1):
		self.servo.value = servo_value

		if self.modbus_client.is_open():
			self.toggle_coil_value(self.servo.is_active)
			coils = self.modbus_client.read_coils(0, 1)
			print(f"Coils: {coils}")
		else:
			self.toggle_coil_value(False)
		
		time.sleep(wait_time)

	def toggle_coil_value(self, is_positive):
		if is_positive:
			self.modbus_client.write_single_coil(0, True)  
		else: 
			self.modbus_client.write_single_coil(0, False)
