#!/usr/bin/python
import datetime
import sys
import RPi.GPIO as GPIO ## Import GPIO library
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
from logPrint import logPrint

#getting the input parms
argsLen = len(sys.argv)

if argsLen == 2:
  if sys.argv[1] == "on":
    #Turn ON
    print("Turning LED ON")
    GPIO.output(7,True)
  elif sys.argv[1] == "off":
    #Turn OFF
    print("Turning LED OFF")
    GPIO.output(7,False)
  else:
    print("this is broken")

# print('Hello', 'World', 2+3, file=open('/home/pi/file.txt', 'w'))
# sys.stdout = open('/home/pi/logfile', 'w')

# def logPrint(s):
#     now = datetime.datetime.now()
#     filename='/home/pi/log'+now.strftime('%Y-%m-%d')+'.txt'    
#     f=open(filename,'a')
#     f.write(now.strftime('%H:%M:%S')+' '+s+'\n')
#     # f.write(len(sys.argv))
      
#     f.close()

# logPrint('arg = ' + sys.argv[1])

logPrint('arg = ' + sys.argv[1] + 'lenght = ' + str(len(sys.argv)))
# logPrint(len(sys.argv))

