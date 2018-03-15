try:
    import RPi.GPIO as GPIO
    import time
    GPIOAvailable = True
except:
    GPIOAvailable = False

if GPIOAvailable:
    GPIO.setmode(GPIO.BCM)
    TRIG_PIN = 21
    ECHO_PIN = 20
    GPIO.setup(TRIG_PIN,GPIO.OUT)
    GPIO.setup(ECHO_PIN,GPIO.IN)


def getDistance():
    if GPIOAvailable:
        GPIO.output(TRIG_PIN, False)                 #Set TRIG as LOW
        time.sleep(2)                            #Delay of 2 seconds

        GPIO.output(TRIG_PIN, True)                  #Set TRIG as HIGH
        time.sleep(0.00001)                      #Delay of 0.00001 seconds
        GPIO.output(TRIG_PIN, False)                 #Set TRIG as LOW

        while GPIO.input(ECHO_PIN)==0:               #Check whether the ECHO is LOW
            pulse_start = time.time()              #Saves the last known time of LOW pulse

        while GPIO.input(ECHO_PIN)==1:               #Check whether the ECHO is HIGH
            pulse_end = time.time()                #Saves the last known time of HIGH pulse 

        pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

        distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
        distance = round(distance, 2)            #Round to two decimal points

        if distance > 2 and distance < 400:      #Check whether the distance is within range
            return str(distance - 0.5) + " cm"  #Print distance with 0.5 cm calibration
        else:
            return "Out Of Range"                   #display out of range
    else:
        return "Not running on a pi or RPi.GPIO library not installed"