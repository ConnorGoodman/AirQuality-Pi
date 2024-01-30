import serial, time
import mh_z19
from Adafruit_IO import Client

#set adafruit key here
adafruit_key = 'key'

#set adafruit username here
adafruit_username = 'username'

aio = Client(adafruit_username, adafruit_key)
ser = serial.Serial('/dev/ttyUSB0')

while True:
    try:
        data = []
        for index in range (0, 10):
            datum = ser.read()
            data.append(datum)
            
        pmtwofive = int.from_bytes(b''.join(data[2:4]), byteorder='little')/10
        aio.send('air-quality-pm-two-five', pmtwofive)
        print('pm2.5', pmtwofive)
        pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little')/10
        aio.send('air-quality-pm-ten', pmten)
        print('pm10', pmten) 
    except :
        print("Error reading pm")
        
    try:
        cO2_measurement = mh_z19.read_from_pwm()['co2']
        print(cO2_measurement)
        aio.send('co2', cO2_measurement)
        print('sending co2 to adafruit')
        
    except:
        print("Error reading cO2")
    time.sleep(30)



