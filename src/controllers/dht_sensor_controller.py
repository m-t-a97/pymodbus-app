import os
import sys
import time

from decouple import config
import Adafruit_DHT as dht

class DHTSensorController:
  def __init__(self, sensor_type, pin, modbus_client):
    self.sensor_type = sensor_type
    self.pin = pin
    self.modbus_client = modbus_client
  
  def execute(self):
    try:
      while True:
        humidity, temperature = dht.read_retry(self.sensor_type, self.pin)

        if humidity != None and temperature != None:
            self.modbus_client.write_single_register(10, int(humidity))
            self.modbus_client.write_single_register(11, int(temperature))
            print(f"Humidity: {humidity}, Temperature: {temperature}")
        else:
            print("Failed to read from device")

        time.sleep(1)

    except Exception as e:
        print(e)
        sys.exit()
