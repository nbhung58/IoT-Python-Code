import minimalmodbus, serial, time

LU3 = minimalmodbus.Instrument('/dev/ttyUSB0', 3)  # port name, slave address (in decimal)
LU3.serial.port                     # this is the serial port name
LU3.serial.baudrate = 9600        # Baud
LU3.serial.bytesize = 8
LU3.serial.parity   = serial.PARITY_NONE
LU3.serial.stopbits = 1
LU3.serial.timeout  = 5         # seconds
LU3.address                        # this is the slave address number
LU3.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
LU3.clear_buffers_before_each_transaction = True

errorcounter = 0
x3 = 0.0

def ReadLun3(x3):
    try:
        x3 = round(LU3.read_float(0, 4) ,4)
        return x3
    except Exception as error:
        print ("[!] Exception occurred: ", error)

#while (True):
#    print(ReadLun3(x3))
 #   time.sleep(1)
    
