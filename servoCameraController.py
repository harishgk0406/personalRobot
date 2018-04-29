import RPi.GPIO as GPIO

import time
"""
servo control usinf pi
NUNUG 
"""
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)

frequencyHertz=50 
"""control signal """
pwm = GPIO.PWM(11,frequencyHertz)

leftTurnNeg90 = 0.75
rightTurnPos90 = 2.50

middlePos = (rightTurnPos90 - leftTurnNeg90) / 2 + leftTurnNeg90
#formula 
msPerCycle = 1000/frequencyHertz

for i in range(3):
    
    for position in positionList:
        dutyCyclePercentage = position * 100 / msPerCycle
        
        print ("Position: "+str(position))
        #
        print ("Duty Cycle: "+str(dutyCyclePercentage) +"%")
        print ("")
        pwm.start(dutyCyclePercentage)
        time.sleep(.5)
        
        
pwm.stop()

GPIO.cleanup()

