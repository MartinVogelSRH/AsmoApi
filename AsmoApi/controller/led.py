try:
    import RPi.GPIO as GPIO
    GPIOAvailable = true
except:
    GPIOAvailable = False

if GPIOAvailable:
    GPIO.setmode(GPIO.BCM)

    BLUE_PIN = 13;
    RED_PIN = 19;
    GREEN_PIN = 26;

    GPIO.setup(BLUE_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(RED_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(GREEN_PIN, GPIO.OUT, initial=GPIO.LOW)

def toogleAllOff():
    if GPIOAvailable:
        GPIO.output(BLUE_PIN, GPIO.LOW)
        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        return "Success"
    else:
        return "not running on a pi or RPi.GPIO library not installed"