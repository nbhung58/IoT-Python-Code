# importing libraries
from ReadGX1 import *
from datetime import datetime
import serial
import paho.mqtt.client as paho
import os
import socket
import ssl
import string
import json
import random
import os
#from ReadLun1to7 import *
from ReadLun1 import *
from ReadLun3 import *
from ReadLun4 import *
from ReadLun5 import *
from ReadLun6 import *
from time import *


#sleep(180)
x1= x2 =x3= x4= x5= x6 = x7= 0.0
errorcounter = 0

GX1ValX = GX1ValY = GX1Xtemp =  GX1Ytemp = 0 
GX2ValX = GX2ValY = GX2Xtemp =  GX2Ytemp = 0  #create instance for sensor value
x = y = 0.0 #Lun value
id_GX1 = "GX1"
id_GX2 = "GX2"
n = 0

connflag = False

 
def on_connect(client, userdata, flags, rc):                # func for making connection
    global connflag
    print ("Connected to AWS")
    connflag = True
    print("Connection returned result: " + str(rc) )
 
def on_message(client, userdata, msg):                      # Func for Sending msg
    print(msg.topic+" "+str(msg.payload))
    
#def get_random_string(length):
#    letters = string.ascii_lowercase
#    result_str = ''.join(random.choice(letters) for i in range(length))
#    print("Random string of length", length, "is:", result_str)
#    return result_str
    
def getMAC(interface='eth0'):
  # Return the MAC address of the specified interface
  try:
    str = open('/sys/class/net/%s/address' %interface).read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17]
def getEthName():
  # Get name of the Ethernet interface
  try:
    for root,dirs,files in os.walk('/sys/class/net'):
      for dir in dirs:
        if dir[:3]=='enx' or dir[:3]=='eth':
          interface=dir
  except:
    interface="None"
  return interface
 
#def on_log(client, userdata, level, buf):
#    print(msg.topic+" "+str(msg.payload))
 
mqttc = paho.Client()                                       # mqttc object
mqttc.on_connect = on_connect                               # assign on_connect func
mqttc.on_message = on_message                               # assign on_message func
#mqttc.on_log = on_log

#### Change following parameters #### 
awshost = "a3fvnahpf1jsfb-ats.iot.ap-southeast-1.amazonaws.com"      # Endpoint
awsport = 8883                                              # Port no.   
clientId = "IotHueThing_Client"                                     # Thing_Name
thingName = "IotHueThing_Client"                                    # Thing_Name
caPath = "/home/pi/Iot-hue/AmazonRootCA1.pem"                                      # Root_CA_Certificate_Name
certPath = "/home/pi/Iot-hue/8ae349a6288edd5b9193d0005e2ca7a119e6df65085030c8aab7fca35edddfd0-certificate.pem.crt"                            # <Thing_Name>.cert.pem
keyPath = "/home/pi/Iot-hue/8ae349a6288edd5b9193d0005e2ca7a119e6df65085030c8aab7fca35edddfd0-private.pem.key"                          # <Thing_Name>.private.key
 
mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  # pass parameters
 
mqttc.connect(awshost, awsport, keepalive=60)               # connect to aws server
 
mqttc.loop_start()                                          # Start the loop

while (True):
    try:
      a = cmdGX1(GX1ValX, GX1ValY, GX1Xtemp, GX1Ytemp) #Get value GX1
      a1 = round(a[1] + 15,4)
      b = cmdGX2(GX2ValX, GX2ValY, GX2Xtemp, GX2Ytemp) #Get value GX2
      b1 = b[0] 
      b2 = b[1]
      b3 = round(b1 + 1.9, 4)
      b4 = round(b2 + 15, 4)
      #c = ReadLunId5(x5, y5)
      #d = ReadLunId6(x6, y6)
      e1 = random.random()
      e = 836.423 - round(1-e1,4)
      #k = ReadLun2(x2)
      f = ReadLun3(x3)
      g = ReadLun4(x4)
      h = ReadLun5(x5)
      j = ReadLun6(x6)
      #m = ReadLun7(x7)
      now = datetime.now()
      timestamp = datetime.timestamp(now)
      #now1 = now.strftime("%H:%M:%S")
      id = "NodeHue"
      
      if connflag == True:
          #ethName=getEthName()
          #ethMAC=getMAC(ethName)
          #macIdStr = ethMAC
          paylodmsg0="{"
          paylodmsg1 = "\"id\" :\""
          paylodmsg2 = "\", \"X1\":"
          paylodmsg3 = ", \"Y1\":"
          paylodmsg4 = ", \"X2\":"
          paylodmsg5 = ", \"Y2\":"
          paylodmsg6 = ", \"LU1\":"
          paylodmsg7 = ", \"LU3\":"
          paylodmsg8 = ", \"LU4\":"
          paylodmsg9 = ", \"LU5\":"
          paylodmsg10 = ", \"LU6\":"
          paylodmsg11 = "}"
          #paylodmsg12 =  "}"
          paylodmsg ="{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}".format(paylodmsg0, paylodmsg1,id, 
                      paylodmsg2, a[0], #GX1-X 
                      paylodmsg3, a1,#+ 15, #GX1-Y
                      paylodmsg4, b3,#+ 1.9, #GX2-X
                      paylodmsg5, b4,#+ 15, #GX2-Y
                      paylodmsg6, e, #LU1-X
                      paylodmsg7, f, #LU3-X
                      paylodmsg8, g, #LU4-X
                      paylodmsg9, h, #LU5-X
                      paylodmsg10, j, #LU6-X                                                                           
                      paylodmsg11,)# #paylodmsg8, #timestamp, paylodmsg9,
                      #paylodmsg12)
          paylodmsg = json.dumps(paylodmsg) 
          paylodmsg_json = json.loads(paylodmsg)       
          mqttc.publish("ElectronicsInnovation", paylodmsg_json , qos=1)        # topic: temperature # Publishing Temperature values
          print("msg sent: ElectronicsInnovation" ) # Print sent temperature msg on console
          print(paylodmsg_json)
          n = n + 1
      #else if n >27:
       #   os.system('shutdown -s')
      else:
          print("waiting for connection...")
      sleep(5)
      
    except Exception as error:
        print ("[!] Exception occurred: ", error)
        sleep(1)

