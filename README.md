# PicoPiThermometerHygrometer
A Thermometer and Hygrometer for a Pico Pi to check climate of a terrarium.

This is a project I created for the final assignment for CS50.  It is a micropython program that runs on a Pico Pi.  It reads the temprature and humidity data from a sensor, and then outputs that information to an LCD screen for easy viewing.  There are also 3 thresholds that are fully customizable. By default, the settings are:

Good = Ideal temprature +- 5 (degrees or %) - The screen will be green.

Warn = Ideal temprature +- 5-10 (degrees or %) - The screen will be amber.

Alarm = Ideal temprature > 10 (degrees or %) - The screen will be red.


Both the colors, and theresholds can be set in the global variables at the top of the program:

GOOD_COLOR = [0,255,0]

WARN_COLOR = [255,209,0]

ALARM_COLOR = [255,0,0]



WARNING_THRESHOLD = 5

ALARM_THRESHOLD = 10


The time that it will wait before switching between temprature and humidity:
SCREEN_REFRESH_DELAY = 5


Additional sensors or species can easily be added to the code on the fly if you want to use multiple sensors at a time.  Please see the comments of the code to see how to add them.


BOM:

Raspberry-Pi Pico - 8-10$

  https://www.pishop.ca/product/raspberry-pi-pico-w/
  
Waveshare LCD1602 RGB - 18$

  https://www.waveshare.com/lcd1602-rgb-module.htm
  
KY-15 sensor - 3$

  https://www.banggood.com/KY-015-DHT11-Temperature-Humidity-Sensor-Module-p-916173.html?cur_warehouse=CN
  
 
I plan to design an enclosure for the Pico and sensor that can be 3D printed and I will add it here once it has been made and tested.


If anyone has questions, I will do my best to answer.
