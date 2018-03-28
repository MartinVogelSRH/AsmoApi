import controller.settings as settings
try:
    import RPi.GPIO as GPIO
    GPIOAvailable = True
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

def toggleAllOff():
    if GPIOAvailable:
        GPIO.output(BLUE_PIN, GPIO.LOW)
        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        return "Success"
    else:
        return "Not running on a pi or RPi.GPIO library not installed"

def toggleColor(color = None):
    if GPIOAvailable:
        if color == 'red':
            GPIO.output(RED_PIN, not GPIO.input(RED_PIN))
            return "Success"
        elif color == 'green':
            GPIO.output(GREEN_PIN, not GPIO.input(GREEN_PIN))
            return "Success"
        elif color == 'blue':
            GPIO.output(BLUE_PIN, not GPIO.input(BLUE_PIN))
            return "Success"
        else:
            return "Please choose red, green or blue."
    else:
        return "not running on a pi or RPi.GPIO library not installed color: " + color