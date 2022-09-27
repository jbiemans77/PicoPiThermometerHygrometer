<p># PicoPiThermometerHygrometer A Thermometer and Hygrometer for a Pico Pi to check climate of a terrarium.</p>

<p>This is a project I created for the final assignment for CS50. It is a micropython program that runs on a Pico Pi. It reads the temprature and humidity data from a sensor, and then outputs that information to an LCD screen for easy viewing. There are also 3 thresholds that are fully customizable. By default, the settings are:</p>

<p>Good = Ideal temprature +- 5 (degrees or %) - The screen will be green.</p>

<p>Warn = Ideal temprature +- 5-10 (degrees or %) - The screen will be amber.</p>

<p>Alarm = Ideal temprature > 10 (degrees or %) - The screen will be red.</p>

<hr>

<p> Both the colors, and theresholds can be set in the global variables at the top of the program:</p>

<p>GOOD_COLOR = [0,255,0]</p>

<p>WARN_COLOR = [255,209,0]</p>

<p>ALARM_COLOR = [255,0,0]</p>

<br>

<p>WARNING_THRESHOLD = 5</p>

<p>ALARM_THRESHOLD = 10</p>

<hr>

<p> The time that it will wait before switching between temprature and humidity: 
<br> SCREEN_REFRESH_DELAY = 5</p>

<p> Additional sensors or species can easily be added to the code on the fly if you want to use multiple sensors at a time. Please see the comments of the code to see how to add them.</p>

<hr>

<p> BOM:</p>

<p>Raspberry-Pi Pico - 8-10$</p>
  https://www.pishop.ca/product/raspberry-pi-pico-w/</p>

<p>Waveshare LCD1602 RGB - 18$
  https://www.waveshare.com/lcd1602-rgb-module.htm</p> 
  
<p>KY-15 sensor - 3$
  https://www.banggood.com/KY-015-DHT11-Temperature-Humidity-Sensor-Module-p-916173.html?cur_warehouse=CN</p>
  
<hr>

<p>I plan to design an enclosure for the Pico and sensor that can be 3D printed and I will add it here once it has been made and tested.</p>

<p> If anyone has questions, I will do my best to answer.</p>
