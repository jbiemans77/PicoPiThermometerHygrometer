'''
Using DHT.py from
https://how2electronics.com/interfacing-dht11-temperature-humidity-sensor-with-raspberry-pi-pico/

Using RGB1602.py drivers from
https://www.waveshare.com/wiki/LCD1602_RGB_Module
'''

from machine import Pin, I2C
import utime as time
from dht import DHT11, InvalidChecksum
import RGB1602
import math
import Reptile
from DisplayScreen import DisplayScreenDetails

# Hardware Variables
SCREEN_WIDTH = 16
SCREEN_HEIGHT = 2
LCD=RGB1602.RGB1602(SCREEN_WIDTH,SCREEN_HEIGHT)
SENSOR_PIN = 28

# Display Variables
GOOD_COLOR = [0,255,0]
WARN_COLOR = [255,209,0]
ALARM_COLOR = [255,0,0]

WARNING_THRESHOLD = 5
ALARM_THRESHOLD = 10

SCREEN_REFRESH_DELAY = 5


def main():
    # Sensor Setup
    boaSensorPin = 28
    boaSensor = CreateSensor(boaSensorPin)
    
    # Species Setup
    boaDetails = Reptile.ReptileDetails("Boa", 27, 30)
    
    while True:
        DisplayInfo(boaDetails)
        PauseDisplayForRefreshDelay()
        
        DisplayScreen("TEMPERATURE", boaSensor, boaDetails)
        PauseDisplayForRefreshDelay()
        
        DisplayScreen("HUMIDITY", boaSensor, boaDetails)
        PauseDisplayForRefreshDelay()
        
        # Additional sensors could be added to the system by creating new sensor pins, sensors
        # Example: beardedDragonSensorPin = 27
        #          beardedDragonSensor = CreateSensor(beardedDragonSensorPin)
        #          beardedDragonbaskingSensorPin = 26
        #          beardedDragonBaskingSensor = CreateSensor(beardedDragonbaskingSensorPin)
        
        # If the extra sensors are connected to the enclosures of different species, you can create
        # different ReptileDetails for those species to get the specific ideal tempratures.
        # Example: beardedDragonDetails = Reptile.ReptileDetails("beardedDragon", 27, 65)
        #          beardedDragonBaskingDetails = Reptile.ReptileDetails("beardedDragon", 34, 65)
        
        # Future implimentation could be added to control mist machine or basking lamp
        # depending on warning levels.  Or send an SMS or email letting you know if the alert if you have the PicoW
        
        
def CreateSensor(sensorPin):
    pin = Pin(sensorPin, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    
    return sensor


def DisplayInfo(speciesDetails):
    SetRBGColorToInfo()
    line1, line2 = str(speciesDetails).split(";")
    OutputToLCD(line1, line2)
    
    
def SetRBGColorToInfo():
    LCD.setRGB(255,255,255)
    
    
def OutputToLCD(line1, line2):
    LCD.clear()
   
    LCD.setCursor(0, 0)
    LCD.printout(line1)
  
    LCD.setCursor(0, 1)
    LCD.printout(line2)
    
    
def DisplayScreen(displayScreenType, sensor, speciesDetails):
    displayScreenDetails = CreateDisplayScreenDetails(displayScreenType, sensor, speciesDetails)
    
    warningLevel = GetWarningLevel(displayScreenDetails)
    SetRBGColorToWarningLevel(warningLevel)
    
    line1, line2 = CreateLinesToOutputToLCD(displayScreenDetails)
    OutputToLCD(line1, line2)
    
 
def CreateDisplayScreenDetails(displayScreen, sensor, speciesDetails):
    if displayScreen == "TEMPERATURE":
        current = sensor.temperature
        ideal = speciesDetails.idealTemperature
        label = "Temp :"
        sufix = "C"
    elif displayScreen == "HUMIDITY":
        current = sensor.humidity
        ideal = speciesDetails.idealHumidity
        label = "Humid:"
        sufix = "%"
            
    displayScreenDetails = DisplayScreenDetails(current, ideal, label, sufix)
    
    return displayScreenDetails


def GetWarningLevel(details):
    if (details.ideal - WARNING_THRESHOLD) < details.current < (details.ideal + WARNING_THRESHOLD):
        warningLevel = "Good"
    elif (details.ideal - ALARM_THRESHOLD) < details.current < (details.ideal + ALARM_THRESHOLD):
        warningLevel = "Warn"
    else:
        warningLevel = "Alarm"
        
    return warningLevel
        

def SetRBGColorToWarningLevel(warningLevel):
    if warningLevel == "Good":
        LCD.setRGB(GOOD_COLOR[0],GOOD_COLOR[1], GOOD_COLOR[2])
    elif warningLevel == "Warn":
        LCD.setRGB(WARN_COLOR[0], WARN_COLOR[1], WARN_COLOR[2])
    elif warningLevel == "Alarm":
        LCD.setRGB(ALARM_COLOR[0], ALARM_COLOR[1], ALARM_COLOR[2])
        
        
def CreateLinesToOutputToLCD(details):
    line1 = f"{details.label} {details.current} {details.sufix}"
    line2 = f"Ideal: {details.ideal} {details.sufix}"
    
    return line1, line2


def PauseDisplayForRefreshDelay():
    time.sleep(SCREEN_REFRESH_DELAY)
    
    
if __name__ == "__main__":
    main()