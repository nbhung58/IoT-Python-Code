import minimalmodbus, serial, time

LU4 = minimalmodbus.Instrument('/dev/ttyUSB0', 4)  # port name, slave address (in decimal)
LU4.serial.port                     # this is the serial port name
LU4.serial.baudrate = 9600        # Baud
LU4.serial.bytesize = 8
LU4.serial.parity   = serial.PARITY_NONE
LU4.serial.stopbits = 1
LU4.serial.timeout  = 5         # seconds
LU4.address                        # this is the slave address number
LU4.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
LU4.clear_buffers_before_each_transaction = True

errorcounter = 0
x4 = 0.0

def ReadLun4(x4):
    try:
        x4 = round(LU4.read_float(0, 4) ,4)
        return x4
    except Exception as error:
        print ("[!] Exception occurred: ", error)

#while (True):
 #   print(ReadLun4(x4))
  #  time.sleep(1)
    
    
    

