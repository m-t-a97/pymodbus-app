import time

from gpiozero import DistanceSensor

class DistanceSensorController:
  def __init__(self, echo, trigger, modbus_client):
    self.sensor = DistanceSensor(echo, trigger)
    self.modbus_client = modbus_client
    self.count = self.modbus_client.read_holding_registers(12, 1)[0]

  def execute(self):
    if self.count == None:
      self.count = 0

    while True:
      distance_calculated = self.sensor.distance * 100

      if distance_calculated <= 10:
        self.count = self.count + 1
        self.modbus_client.write_single_register(12, self.count)
        print(f"Count: {self.count}")

      time.sleep(1)
