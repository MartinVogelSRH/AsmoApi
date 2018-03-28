import controller.settings as settings
try:
    import Adafruit_DHT
    GPIOAvailable = True
except:
    GPIOAvailable = False

if GPIOAvailable:
    DHT_PIN = 4 

def getTemperature():
    if GPIOAvailable:
        reading = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT_PIN)
        return reading['temperature']
    else:
        return "This is not a pi or the Adafrut_DHT library is not available"

def getHumidity():
    if GPIOAvailable:
        reading = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT_PIN)
        return reading['humidity']
    else:
        return "This is not a pi or the Adafrut_DHT library is not available"

def getTempAndHum():
    if GPIOAvailable:
        reading = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT_PIN)
        return reading
    else:
        return "This is not a pi or the Adafrut_DHT library is not available"