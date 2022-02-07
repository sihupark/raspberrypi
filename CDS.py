# raspberrypi python3 CDS.py
```PYTHON
import time
import requests, json
from influxdb import InfluxDBClient as influxdb
import serial

import serial

port = '/dev/ttyACM0'
brate = 9600
cmd = 'temp'

seri = serial.Serial(port, baudrate = brate, timeout = None)
print(seri.name)

seri.write(cmd.encode())

try:
		while True:
				if seri.in_waiting !=0 :
						content = seri.readline()
						temp = int(content.decode())
						data = [{
								'measurement' : 'CDS',
								'tags':{
										'office':'1',
								},
								'fields':{
										'value': temp
								}
				}]
				else:
						print("serial read error")
				client = None
				try:
						print(data)
						client = influxdb('localhost', 8086, 'root', 'root', 'CDS')
				except Exception as e:
						print("Exception" + str(e))
				if client is not None:
						try:
								client.write_points(data)
								print(data)
						except Exception as e:
								print("Exception write" + str(e))
						finally:
								client.close()
				time.sleep(1)
except KeyboardInterrupt:
		print("Terminated by Keyboard")
finally:
		print("End of Program")
```
