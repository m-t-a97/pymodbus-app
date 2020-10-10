import time

from gpiozero import DistanceSensor

class DistanceSensorController:
  def __init__(self, echo, trigger, modbus_client):
    self.sensor = DistanceSensor(echo, trigger)
    self.modbus_client = modbus_client

  def execute(self):
    while True:
      distance_calculated = self.sensor.distance * 100

      if distance_calculated <= 10:
        current_count = self.modbus_client.read_holding_registers(12, 1)[0] + 1
        self.modbus_client.write_single_register(12, current_count)
        print(f"Count: {current_count}")

      time.sleep(1)
