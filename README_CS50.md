# Pico Pi Thermometer / Hygrometer

#### Video Demo: <URL>

#### Description: A micro-python program for a Pico Pi that takes temperature and humidity from a sensor and displays it on an LCD screen.

#### Included Files:
<hr>
<u>This project contains 5 python files:</u>
<br>dht.py
<br>RGB1602.py
<br>DisplayScreen.py
<br>main.py
<br>Reptile.py

<hr>

### dht.py
The dht.py file is the driver file for the KY-15 sensor.  It came from:

https://how2electronics.com/interfacing-dht11-temperature-humidity-sensor-with-raspberry-pi-pico/

It gets the serial data from the sensor and breaks it down into variables that are usable in my main function.
<hr>

### RBG1602.py
The RGB1602.py file is the driver file for the WaveShare LCD1602 RGB Sceen.  It can be found on the manufacturer web site:

https://www.waveshare.com/wiki/LCD1602_RGB_Module

It is used to control the LCD screen.

<hr>

### Reptile.py
This contains a class called <b>ReptileDetails</b>.  This class is a container that holds the specific reptile details that other functions will need in order to output the correct information.  It contains 3 properties: <br>
<p><b>species</b> - A label for the spices name to show on the info screen.<br>
<b>idealTemprature</b> - The idea temperature for the terrarium.<br>
<b>idealHumidity</b> - The ideal humidity for the terrarium. </p>

I created this as a class so that all the information could be grouped together when getting passed to various functions.  It keeps all of the variables together, and allows for the easy addition of a reptile or change to the current settings.

<hr>

### DisplayScreen.py
This contains a class called <b>DisplayScreenDetails</b>.  This class is a container to hold the specific details that are used for the display screens.  It contains 4 properties:<br>
<p><b>current</b> - This is the current temprature or humidity.<br>
<b>ideal</b> - This is the ideal temperature or humidity (pulled from the ReptileDetails object)<br>
<b>label</b> - This is the label to be shown on the screen. (EX: "Temp :" or "Humid:", etc)<br>
<b>suffix</b> - This is the suffix to be shown on the screen. (EX: "C", "%", etc)<br>

I created this as a class because I noticed that some of the code was duplicated when I was creating the screens, so having this class allows me to reduce the duplication.

<hr>

### main.py
This is the main class that contains most of the logic.  I created a couple of global variables at the top of the file to hold most of the configuration details:
<p><b>SCREEN_WIDTH</b> - Number of characters across for the display (EX: 16)<br>
<b>SCREEN_HEIGHT</b> Number of rows for the display (EX: 2)<br>
<b>LCD</b> - This is an LCD object that will be used later to operate the screen.  <i>Usage - RGB1602.RGB1602(SCREEN_WIDTH,SCREEN_HEIGHT)</i><br>
<b>SENSOR_PIN</b> - This is the pin that the sensor is wired to (EX: 28)<br>

#Display Variables
<b>GOOD_COLOR</b> - This is RGB color code for the Good screen as a list (EX: [0,255,0])
<b>WARN_COLOR</b> - This is RGB color code for the Warn screen as a list (EX: [255,209,0])
<b>ALARM_COLOR</b>- This is RGB color code for the Warn screen as a list (EX: [255,0,0])<br>
<b>WARNING_THRESHOLD</b> - This is the amount +- that the current (temp or humid) has to differ from the ideal by before a warning will trigger. (this will change the screen color EX: 5)
<b>ALARM_THRESHOLD</b> - This is the amount +- that the current (temp or humid) has to differ from the ideal by before an alarm will trigger (this will change the screen color EX: 10)
<b>SCREEN_REFRESH_DELAY</b> - This is the amount of time each screen will display for</p>
<hr>
The main() method is pretty straight forward.  First you create a pin and then pass that pin to a method that creates and returns a sensor object.  The sensor object is consistently checking the sensor to retrieve the current temperature and humidity.  The second think you create is a ReptileDetails object with the specific details for the reptile that will be in the terrarium.  EX: Reptile.ReptileDetails("Boa", 27, 60) 

Once those 2 configuration details are out of the way, the only other thing in the main() is an infinite loop that:
<p>Displays an info screen<br>
Pauses<br>
Displays a temperature screen<br>
Pauses<br>
Displays a humidity screen<br>
Pauses<br></p>

I designed it to be minimal because it makes it much easier for anyone else who is reading the code to follow what the code is doing.  From there, there are a handful of other functions that break all of the logic into small and easily manageable bits of logic.  The methods are:

def <b>CreateSensor(sensorPin):</b>
Creates and returns a sensor object

def <b>DisplayInfo(speciesDetails):</b>
Set the color for the info screen, get the lines of text, display the text)

def <b>SetRBGColorToInfo():</b>
Sets the base color for an info screen

def <b>OutputToLCD(line1, line2):</b>
Outputs the lines of text to the LCD

def <b>DisplayScreen(displayScreenType, sensor, speciesDetails):</b>
Creates a DisplayScreenDetailsObject, Gets the warning level, Sets the color based on the warning level, gets the lines of text, displays the text.

def <b>CreateDisplayScreenDetails(displayScreen, sensor, speciesDetails):</b>
Creates a DisplayScreenDetailsObject

def <b>GetWarningLevel(details):</b>
Gets the warning level based on the ideal temperature.

def <b>SetRBGColorToWarningLevel(warningLevel):</b>
Sets the color to the matching color (from global color variable) based on the warning level.

def <b>CreateLinesToOutputToLCD(details):</b>
creates 'line1' and 'line2' for the display based on the screen details 

def <b>PauseDisplayForRefreshDelay():</b>
Pause execution.

I broke everything out to individual methods to follow the practices I learned from Clean Code.  In many cases where there was duplicate code between the temperature and humidity screens,  I combined them into a single abstract "Display" function, rather than a specific "DisplayHumidity" and "DisplayTemperature".  I found this solution to be cleaner and required less duplicated code.  I had considered creating different states, and switching the screen output based on the state, but because there will only ever be 3 distinct screens, I thought this level of abstraction was overly complicated for the task.

This modular implementation also makes adding future features really easy.  If someone wanted to add another sensor or two, all they would have to do is create a new pin and pass that pin to "CreateSensor" to create a new sensor.  The Pico has many pins, so multiple sensors can be added pretty quickly.  If you had multiple terrariums (Pet Store, classroom, or just someone who really loves reptiles), you can easily create new "ReptileDetails" to contain the unique information for each distinct reptile, then simply pass the new details and sensors to "DisplayScreen" to display them.

There is also room to add future expansions using other pins on the Pico Pi to control basking lamps, heating pads, mist generators, etc in order to automatically adjust the terrarium if an alarm or a warning is generated.  (for example, if an alarm is generated for the temperature being too low, it could trigger a heating pad to turn on through an external relay).

Also, connecting an external Bluetooth module, or a Pico Pi W (with WIFI), and email could be sent, a notification sent to a phone or other device, or the data could be sent to an external webserver where a page could be generated to show the current status of various sensors at the same time. (this would probably only helpful for the larger scale options like pet stores)

<hr>

The files can be found at:
https://github.com/jbiemans77/PicoPiThermometerHygrometer

Soon I will be adding some 3D models for printable enclosures for all of the electronics, but they have not been created yet.

> Written with [StackEdit](https://stackedit.io/)
