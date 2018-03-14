import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

BLUE_PIN = 13;
RED_PIN = 19;
GREEN_PIN = 26;

GPIO.setup(BLUE_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GREEN_PIN, GPIO.OUT, initial=GPIO.LOW)

def toogleAllOff():
    GPIO.output(BLUE_PIN, GPIO.LOW)
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    return "Hallo"