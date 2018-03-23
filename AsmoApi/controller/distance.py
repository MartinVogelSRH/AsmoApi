import controller.motor
import time
import threading
try:
    import RPi.GPIO as GPIO
    GPIOAvailable = True
except:
    GPIOAvailable = False

if GPIOAvailable:
    GPIO.setmode(GPIO.BCM)
    TRIG_PIN = 21
    ECHO_PIN = 20
    GPIO.setup(TRIG_PIN,GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ECHO_PIN,GPIO.IN)

class DistanceController(object):

    """description of class"""
    thread = None  # background thread that reads the distance from the sensor
    currentDist = None  # current distance is stored here by background thread
    last_access = 0  # time of last client access to the camera

    def initialize(self):
        if DistanceController.thread is None:
            # start background frame thread
            DistanceController.thread = threading.Thread(target=self._thread)
            DistanceController.thread.start()

            # wait until frames start to be available
            while self.currentDist is None:
                time.sleep(0)

    def getDistance(self):
        DistanceController.last_access = time.time()
        self.initialize()
        return self.currentDist
    @classmethod
    def _thread(cls):
        if GPIOAvailable:
            motor1speed , motor2speed = controller.motor.getMotors()
            while (time.time() - cls.last_access < 10) or (motor1speed != 0) or (motor2speed != 0) :
                print ('motor1: ' + str(motor1speed) + ' motor2: ' + str(motor2speed) + ' reding dist..')
                GPIO.output(TRIG_PIN, False)                 #Set TRIG as LOW
                time.sleep(2)                            #Delay of 2 seconds

                GPIO.output(TRIG_PIN, True)                  #Set TRIG as HIGH
                time.sleep(0.00001)                      #Delay of 0.00001 seconds
                GPIO.output(TRIG_PIN, False)                 #Set TRIG as LOW
                abort = False
                starttime = time.time()
                while GPIO.input(ECHO_PIN)==0 and abort==False:   #Check whether the ECHO is LOW
                    pulse_start = time.time()                  #Saves the last known time of LOW pulse
                    if (time.time() - starttime) > 0.1:
                        abort = True   
        
                pulse_end = time.time()
                while GPIO.input(ECHO_PIN)==1 and abort==False:               #Check whether the ECHO is HIGH
                    pulse_end = time.time()                  #Saves the last known time of HIGH pulse 
                    if (time.time() - pulse_start) > 0.1:
                        abort = True             

                pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

                distance = pulse_duration * 17150        #Multiply pulse duration by 17150 (speed of sound in air / 2) to get distance
                distance = round(distance, 2)            #Round to two decimal points
        
                if abort:
                    cls.currentDist = 'No Sensor available or out of Range. Reading Aborted'
                elif distance > 2 and distance < 400:      #Check whether the distance is within range
                    if distance < 4:
                        controller.motor.setMotors(0,0)
                    cls.currentDist = str(distance - 0.5) + " cm"  #Print distance with 0.5 cm calibration
                else:
                    cls.currentDist = "Out Of Range"                   #display out of range
        else:
            cls.currentDist = "Not running on a pi or RPi.GPIO library not installed"