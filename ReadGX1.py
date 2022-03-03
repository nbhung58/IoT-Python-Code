import minimalmodbus, serial, time

GX1 = minimalmodbus.Instrument('/dev/ttyUSB0', 8)  # port name, slave address (in decimal)
GX1.serial.port                     # this is the serial port name
GX1.serial.baudrate = 9600         # Baud
GX1.serial.bytesize = 8
GX1.serial.parity   = serial.PARITY_NONE
GX1.serial.stopbits = 1
GX1.serial.timeout  = 0.2         # seconds
GX1.address                         # this is the slave address number
GX1.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
GX1.clear_buffers_before_each_transaction = True

ValX = ValY = Xtemp =  Ytemp = 0
ValX2 = ValY2 = Xtemp2 =  Ytemp2 = 0
GX2 = minimalmodbus.Instrument('/dev/ttyUSB0', 9) 

def cmdGX1(ValX, ValY, Xtemp, Ytemp):
    n1 = GX1.read_register(2,0)
    m1 = GX1.read_register(4,0)
    Xaxis = GX1.read_register(3, 4)  # Registernumber, number of decimals
    Yaxis = GX1.read_register(5, 4) # Registernumber, number of decimals
    Xtemp = GX1.read_register(6,2) #Read value X axis
    Ytemp = GX1.read_register(7,2) #Read value Y axis
    g = 6.5535

    #Function call Xaxis
    def case1x(Xaxis): #65533
        Xaxis = (Xaxis - 3*g)
        Xaxis = round(Xaxis,4)
        return Xaxis

    def case2x(Xaxis): #65534
        Xaxis = Xaxis - 2*g  
        Xaxis = round(Xaxis,4)
        return Xaxis

    def case3x(Xaxis): #65535
        Xaxis = Xaxis - g
        Xaxis = round(Xaxis,4)
        return Xaxis

    def case4x(Xaxis): #0
        Xaxis = round(Xaxis,4)
        return Xaxis

    def case5x(Xaxis): #1
        Xaxis = Xaxis + g
        Xaxis = round(Xaxis,4)
        return Xaxis

    def case6x(Xaxis): #2
        Xaxis = Xaxis + 2*g
        Xaxis = round(Xaxis,4)
        return Xaxis
    #Function call Yaxis
    def case1y(Yaxis): #65533
        Yaxis = Yaxis - 3*g 
        Yaxis = round(Yaxis,4)
        return Yaxis

    def case2y(Yaxis): #65534
        Yaxis = Yaxis - 2*g  
        Yaxis = round(Yaxis,4)
        return Yaxis

    def case3y(Yaxis): #65535
        Yaxis = Yaxis - g
        Yaxis = round(Yaxis,4)
        return Yaxis

    def case4y(Yaxis): #0
        Yaxis = round(Yaxis,4)
        return Yaxis

    def case5y(Yaxis): #1
        Yaxis = Yaxis + g
        Yaxis = round(Yaxis,4)
        return Yaxis

    def case6y(Yaxis): #2
        Yaxis = Yaxis + 2*g
        Yaxis = round(Yaxis,4)
        return Yaxis

    def GX1XAxis(n1):
            switcher={
                    65533:case1x(Xaxis),
                    65534:case2x(Xaxis),
                    65535:case3x(Xaxis),
                    0:case4x(Xaxis),
                    1:case5x(Xaxis),
                    2:case6x(Xaxis)
                }
            return switcher.get(n1, "nothing")
    def GX1Yaxis(m1):
            switcher={
                    65533:case1y(Yaxis),
                    65534:case2y(Yaxis),
                    65535:case3y(Yaxis),
                    0:case4y(Yaxis),
                    1:case5y(Yaxis),
                    2:case6y(Yaxis)
                }
            return switcher.get(m1, "nothing")

    ValX = GX1XAxis(n1)
    ValY = GX1Yaxis(m1)
    Xtemp = Xtemp
    Ytemp = Ytemp
    return ValX, ValY, Xtemp, Ytemp #Return value X, Y axis and temperatyure axis X, Y

def cmdGX2(ValX2, ValY2, Xtemp2, Ytemp2):
    n2 = GX2.read_register(2,0)
    m2 = GX2.read_register(4,0)
    Xaxis2 = GX2.read_register(3, 4)  # Registernumber, number of decimals
    Yaxis2 = GX2.read_register(5, 4) # Registernumber, number of decimals
    Xtemp2 = GX2.read_register(6,2) #Read value X axis
    Ytemp2 = GX2.read_register(7,2) #Read value Y axis
    g = 6.5535

    #Function call Xaxis
    def case1x(Xaxis2): #65533
        Xaxis2 = (Xaxis2 - 3*g)
        Xaxis2 = round(Xaxis2,4)
        return Xaxis2

    def case2x(Xaxis2): #65534
        Xaxis2 = Xaxis2 - 2*g  
        Xaxis2 = round(Xaxis2,4)
        return Xaxis2

    def case3x(Xaxis2): #65535
        Xaxis2 = Xaxis2 - g
        Xaxis2 = round(Xaxis2,4)
        return Xaxis2

    def case4x(Xaxis2): #0
        Xaxis2 = round(Xaxis2,4)
        return Xaxis2

    def case5x(Xaxis2): #1
        Xaxis2 = Xaxis2 + g
        Xaxis2 = round(Xaxis2,4)
        return Xaxis2

    def case6x(Xaxis2): #2
        Xaxis2 = Xaxis2 + 2*g
        Xaxis2 = round(Xaxis2,4)
        return Xaxis2
    #Function call Yaxis2
    def case1y(Yaxis2): #65533
        Yaxis2 = Yaxis2 - 3*g 
        Yaxis2 = round(Yaxis2,4)
        return Yaxis2

    def case2y(Yaxis2): #65534
        Yaxis2 = Yaxis2 - 2*g  
        Yaxis2 = round(Yaxis2,4)
        return Yaxis2

    def case3y(Yaxis2): #65535
        Yaxis2 = Yaxis2 - g
        Yaxis2 = round(Yaxis2,4)
        return Yaxis2

    def case4y(Yaxis2): #0
        Yaxis2 = round(Yaxis2,4)
        return Yaxis2

    def case5y(Yaxis2): #1
        Yaxis2 = Yaxis2 + g
        Yaxis2 = round(Yaxis2,4)
        return Yaxis2

    def case6y(Yaxis2): #2
        Yaxis2 = Yaxis2 + 2*g
        Yaxis2 = round(Yaxis2,4)
        return Yaxis2

    def GX2XAxis(n2):
            switcher={
                    65533:case1x(Xaxis2),
                    65534:case2x(Xaxis2),
                    65535:case3x(Xaxis2),
                    0:case4x(Xaxis2),
                    1:case5x(Xaxis2),
                    2:case6x(Xaxis2)
                }
            return switcher.get(n2, "nothing")
    def GX2Yaxis(m2):
            switcher={
                    65533:case1y(Yaxis2),
                    65534:case2y(Yaxis2),
                    65535:case3y(Yaxis2),
                    0:case4y(Yaxis2),
                    1:case5y(Yaxis2),
                    2:case6y(Yaxis2)
                }
            return switcher.get(m2, "nothing")
    ValX2 = GX2XAxis(n2)
    ValY2 = GX2Yaxis(m2)
    Xtemp2 = Xtemp2
    Ytemp2 = Ytemp2
    return ValX2, ValY2, Xtemp2, Ytemp2 #Return value X, Y axis and temperatyure axis X, Y

#errorcounter = 0
#while (True):
#    try:
#        a = cmdGX1(ValX, ValY, Xtemp, Ytemp)
#        b = cmdGX2(ValX2, ValY2, Xtemp2, Ytemp2)
#        print("Gia tri goc xoay 1: ",a[0], a[1], a[2], a[3])
 #       print("Gia tri goc xoay 2: ",b[0], b[1], b[2], b[3])
 #       time.sleep(1)
 #   except Exception as error:
 #       print ("[!] Exception occurred: ", error)
  #      time.sleep(1)
    
