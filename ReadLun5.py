import minimalmodbus, serial, time

LU5 = minimalmodbus.Instrument('/dev/ttyUSB0', 5)  # port name, slave address (in decimal)
LU5.serial.port                     # this is the serial port name
LU5.serial.baudrate = 9600        # Baud
LU5.serial.bytesize = 8
LU5.serial.parity   = serial.PARITY_NONE
LU5.serial.stopbits = 1
LU5.serial.timeout  = 5         # seconds
LU5.address                        # this is the slave address number
LU5.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
LU5.clear_buffers_before_each_transaction = True

errorcounter = 0
x5 = 0.0

def ReadLun5(x5):
    try:
        x5 = round(LU5.read_float(0, 4) ,4)
        return x5
    except Exception as error:
        print ("[!] Exception occurred: ", error)

#print(ReadLun5(x5))

#while (True):
 #   print(ReadLun5(x5))
  #  time.sleep(1)
    