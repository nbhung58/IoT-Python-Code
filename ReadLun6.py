import minimalmodbus, serial, time

LU6 = minimalmodbus.Instrument('/dev/ttyUSB0', 6)  # port name, slave address (in decimal)
LU6.serial.port                     # this is the serial port name
LU6.serial.baudrate = 9600        # Baud
LU6.serial.bytesize = 8
LU6.serial.parity   = serial.PARITY_NONE
LU6.serial.stopbits = 1
LU6.serial.timeout  = 5         # seconds
LU6.address                        # this is the slave address number
LU6.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
LU6.clear_buffers_before_each_transaction = True

errorcounter = 0
x6 = 0.0

def ReadLun6(x6):
    try:
        x6 = round(LU6.read_float(0, 4) ,4)
        return x6
    except Exception as error:
        print ("[!] Exception occurred: ", error)

#while (True):
#    print(ReadLun6(x6))
 #   time.sleep(1)
    
    


