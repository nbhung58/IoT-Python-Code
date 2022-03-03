import minimalmodbus, serial
from time import *

LU1 = minimalmodbus.Instrument('/dev/ttyUSB0', 1)  # port name, slave address (in decimal)
LU1.serial.port                     # this is the serial port name
LU1.serial.baudrate = 9600        # Baud
LU1.serial.bytesize = 8
LU1.serial.parity   = serial.PARITY_NONE
LU1.serial.stopbits = 1
LU1.serial.timeout  = 5         # seconds
LU1.address                        # this is the slave address number
LU1.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
LU1.clear_buffers_before_each_transaction = True

errorcounter = 0
x1 = 0.0

def ReadLun1(x1):
    try:
        x1 = round(LU1.read_float(0, 4) ,4)
        return x1
    except Exception as error:
        print ("[!] Exception occurred: ", error)
        sleep(1)

#while (True)
#print(ReadLun1(x1))

    


    