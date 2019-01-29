import RPi.GPIO as GPIO
import time #import time lib, allows sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

# Define the function named blink()
# def Blink(numTimes, speed):
#     for i in range(0,numTimes) #run loop numTimes
#         print "Iteration " + str(i+1) # print current loop
#         GPIO.output(7, True) # switch on pin 7
#         time.sleep(speed) #wait
#         GPIO.output(7, False)# switch off pin 7
#         time.sleep(speed) # wait
#     print "Done" # when loop is complete, print 'done'
#     GPIO.cleanup()
##Define a function named Blink()
def Blink(numTimes,speed):
  for i in range(0,numTimes):## Run loop numTimes
    print ("Iteration " + str(i+1)) ## Print current loop
    GPIO.output(7,True)## Switch on pin 7
    time.sleep(speed)## Wait
    GPIO.output(7,False)## Switch off pin 7
    time.sleep(speed)## Wait
  print ("Done") ## When loop is complete, print "Done"
  GPIO.cleanup()

#ask user for a total numbr of blink and the length of each blink
iterations = input("Enter total number of times to blink: ")
speed = input("Enter length of each blink(seconds): ")

#start Blink() function, convert user input from strings to numeric data
Blink(int(iterations), float(speed))