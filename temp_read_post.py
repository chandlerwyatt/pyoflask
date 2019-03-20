from time import sleep
import requests

def gettemp(id):
	mytemp = ''
	filename = 'w1_slave'
	f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
	line = f.readline() # read first line
	crc = line.rsplit(' ', 1)
	crc = crc[1].replace('\n', '')
	if crc == 'YES':
		line = f.readline() # read second line
		mytemp = line.rsplit('t=', 1)
		mytemp = int(mytemp[1])
	else:
		mytemp = None
	f.close()

	return mytemp


if __name__ == '__main__':

	ip = '192.168.1.150'
	flask_server = "http://{}:5000/temp".format(ip)	
	#flask_server = f"http://{ip}:5000/temp"
	id = '28-03159779ade1'

	while True:
		temp_c = gettemp(id)
		if temp_c is not None:
			print("Temp : " + '{:.3f}'.format(temp_c/1000))
			print("Posting {} to flask server API".format(temp_c))
			requests.post(flask_server, data=str(temp_c))
		else:
			print("CRC failed for temperature sensor!")
		sleep(1)
