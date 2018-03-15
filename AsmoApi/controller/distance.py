try:
    import RPi.GPIO as GPIO
    GPIOAvailable = True
except:
    GPIOAvailable = False

if GPIOAvailable:
    GPIO.setmode(GPIO.BCM)

def getDistance():