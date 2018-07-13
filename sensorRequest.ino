/*
sensorRequest.ino

Mohamed Ebsim

Contact Jesse Rogerson, @ jrogerson@ingeniumcanada.org

Originally created on July 11, 2018
-----------------------------

This program is made to get sensor and return them via serial 
transmission to the host computer. It periodically (every
quarter second) returns a variety of formated sensor readings.

*/

// LIBRARIES
#include <Wire.h> // Used by the barometer in order to return data
#include <Adafruit_MPL3115A2.h> // Allows access to barometer's functions
#include <SparkFun_HIH4030.h> // Allows access to humidity sensor's functions

// Specifying the analog pin connected to humidity sensor
#define HIH4030_OUT A0

// Specifying the supply voltage 
#define HIH4030_SUPPLY 5

// Creating a humidity sensor object in order to interact with data
// obtained from the sensor
HIH4030 humidity = HIH4030(HIH4030_OUT, HIH4030_SUPPLY);

// Creating a barometer object to utilize the functions that allow
// interaction with data from the sensor
Adafruit_MPL3115A2 barometer = Adafruit_MPL3115A2();

/*
Setup method is run once, at boot up. For this specific program,
it is used to prepare the various libraries for transmission.

*/
void setup()
{
  // Start up serial transmission with a speed of 9600 baud
  Serial.begin(9600);
  
  // Starting the communication using the Wire library
  Wire.begin();
}

/*
This method is the main operating loop. The arduino will continually
loop through this code unless interupted. It collects the data from
each sensor and it "prints" it through serial transmission back to 
host computer.

*/

void loop()
{
  // Checks if it can sense the sensor, if not quits
  
  // Consider removing?
  if(!barometer.begin()) {
    Serial.println("Could not find sensor");
    return;
  }
  
  float pascals = barometer.getPressure(); /*Gets pressure from
                                            barometer (in pascals)*/
  Serial.print("Pressure = ");
  Serial.print(pascals/1000); // Converts from pascals to kilopascals
  Serial.println(" kPa");

  float altm = barometer.getAltitude(); /*Gets altitude from
                                          barometer (in meters)*/
  Serial.print("Altitude = ");
  Serial.print(altm);
  Serial.println(" meters");

  float temp = barometer.getTemperature(); /*Gets temperature from
                                            barometer (in Celsius)*/
  Serial.print("Temperature = ");
  Serial.print(temp);
  Serial.println(" C");
  
  Serial.print("Sensor Voltage = "); /*Gets sensor voltage from
                                       humidity sensor (in volts)*/
  Serial.print(humidity.vout());
  Serial.println(" V");
  
  Serial.print("Relative Humidity = "); /*Gets relative humidity from
                                          humidity sensor (in %)*/
  Serial.print(humidity.getSensorRH());
  Serial.println(" %");
  
  Serial.print("True Relative Humidity = "); /*Gets relative humidity
                                               from humidity sensor
                                               (in %)*/
  Serial.print(humidity.getTrueRH(temp));
  Serial.println(" %");
  
  // Program sleeps for a quarter of a second
  delay(250);
}
