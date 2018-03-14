try:
    import RPi.GPIO as GPIO
    import PicoBorgRev
    GPIOAvailable = True
except:
    GPIOAvailable = False

if GPIOAvailable:
    PBR1 = PicoBorgRev.PicoBorgRev()
    PBR1.init()

def setMotors (motor1speed, motor2speed):
    if GPIOAvailable:
        PBR1.SetMotor1(motor1speed)
        PBR1.SetMotor2(motor2speed)
        return "Success"
    else:
        print("not running on a pi. Motor 1 would have been set to: " + motor1speed + " Motor 2 would have been set to: " + motor2speed)
        return "not running on a pi. Motor 1 would have been set to: " + motor1speed + " Motor 2 would have been set to: " + motor2speed