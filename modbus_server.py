# ------------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------------
from time import sleep

from pyModbusTCP.server import ModbusServer, DataBank

from serial_reader import SerialReader 

# ------------------------------------------------------------------

# ------------------------------------------------------------------
# MAIN CODE
# ------------------------------------------------------------------

def main():
	try:
		server = ModbusServer("192.168.0.118", 10503, no_block = True)
		server.start()
		print("Server is online...")
		
		serial_reader = SerialReader("/dev/ttyACM0")  
		
		previous_temperature = 0
		
		state = [0]
		
		while True:
			data_from_serial_port = serial_reader.read_serial_data()
			
			if data_from_serial_port != "":
				current_temperature = int(data_from_serial_port)
				
				if current_temperature != previous_temperature:
					previous_temperature = current_temperature

					DataBank.set_words(0, [current_temperature])
							
					if not state == DataBank.get_words(0):
						state = DataBank.get_words(0)
						print("value: " + str(state))
						sleep(1)
				
	except Exception as e:
		server.stop();
		print(e)
	
main()

# ------------------------------------------------------------------

