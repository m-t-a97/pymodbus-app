from gpiozero import LED, Button
from signal import pause

class LedController:
  def __init__(self, modbus_client, led_pin, button_pin):
    self.modbus_client = modbus_client
    self.led = LED(led_pin)
    self.button = Button(button_pin)
    self.is_led_on = False

  def execute(self):
    self.button.when_activated = self.toggle_led
    pause()

  def toggle_led(self):
    self.is_led_on = not self.is_led_on
    print(f"LED is on: {self.is_led_on}")
    self.modbus_client.write_single_coil(0, self.is_led_on)  

    if self.is_led_on:
      self.led.on()
    else:
      self.led.off()


