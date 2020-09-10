# ------------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------------
from time import sleep

from decouple import config
from pyModbusTCP.server import ModbusServer, DataBank

from serial_reader import SerialReader 

# ------------------------------------------------------------------

# ------------------------------------------------------------------
# MAIN CODE
# ------------------------------------------------------------------

def main():
	try:
		server = ModbusServer(config("HOST", default = "127.0.0.1"), config("PORT", default = 502, cast = int), no_block = True)
		server.start()
		print("Server is online...")
		
		serial_reader = SerialReader("/dev/ttyACM0")  
		
		while True:
			
			data_from_serial_port = serial_reader.read_serial_data()
			
			if data_from_serial_port != "":		
				
				split_parts = data_from_serial_port.strip().split(",")

				temperature = int(split_parts[0])
				lightLevel = int(split_parts[1])	
				
				DataBank.set_words(0, [temperature])
				DataBank.set_words(1, [lightLevel])
				print(f"temperature: {temperature}, light level: {lightLevel}")
				
				sleep(1)						
				
	except Exception as e:
		server.stop();
		print(e)
	
main()

# ------------------------------------------------------------------

