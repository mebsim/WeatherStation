'''
receiveData.py

Mohamed Ebsim

Contqact Jesse Rogerson, @ jrogerson@ingeniumcanada.org

Originally created on Jully 11, 2018
-------------------------------------

This program is made to read from the serial port and
decode it in order for future use. It currently saves
the data to a file for testing purposes and might
change as the project progresses.

'''

#Import Libraries
import serial
import time

#Setting up serial connection through port ACM0 with a rate of 9600 baud
ser = serial.Serial('/dev/ttyACM0', 9600)

# Open a file (called "file") with the intention of adding to it 
file = open('file', 'a')       

# set basic values for the variables
temp = 0 # temperature
pres = 0 # pressure
altitude = 0 # altitude
sV = 0 # sensor Voltage (for the humidity sensor)
hum = 0 # relative humidity
truhum = 0 # true relative humidity

'''
This function has the job of recieving data from the serial port
and decoding it. Along with that it checks for significant changes
to the information in order to minimize relatively insignificant
changes to the data.
'''
def updateData():
    # bring the variables into the method
    global temp
    global pres
    global altitude
    global sV
    global hum
    global truhum
    
    # Reads data that is coming in
    data = ser.readline()
    
    # decodes it for use
    data = data.decode('utf-8')
    
    '''
    The following lines determine if the data that is coming in
    is of which type. It then removes the extra data until only
    the number remains. It then checks if it is a significant
    enough of a change to be worth changing the variable.
    '''
    if data.startswith('Temperature = '): #14 characters long
        tempNew = float(data[14:-14])
        if abs(temp-tempNew) > 0.:
            temp = tempNew
    if data.startswith('Altitude = '): #11 characters long
        altitudeNew = float(data[11:-9])
        if abs(altitude-altitudeNew) > 0.5:
            altitude = altitudeNew
    if data.startswith('Pressure = '): #11 characters long
        presNew = float(data[11:-6])
        if abs(pres-presNew) > 0.5:
            pres = presNew
    if data.startswith('Sensor Voltage = '): #17 characters long
        sVNew = float(data[17:-4])
        if abs(sV-sVNew) > 0.5:
            sV = sVNew
    if data.startswith('Relative Humidity = '): #19 characters long
        humNew = float(data[19:-4])
        if abs(hum-humNew) > 0.5:
            hum = humNew
    if data.startswith('True Relative Humidity = '): #24 characters long
        truhumNew = float(data[24:-4])
        if abs(truhum-truhumNew) > 0.5:
            truhum = truhumNew
    
    # Writes the full data to file
    file.write(data)

x = 0

# This python program currently only runs 50 times.
while x < 50:
    # Writes the time to file
    file.write(time.asctime(time.localtime(time.time())) + "\n")
    
    # Calls to update the data
    updateData()
    
    # Increases 50 until the loop breaks
    x+=1

# Closes the file
file.close()

# Prints out the final data
print(temp)
print(pres)
print(altitude)
print(sV)
print(hum)
print(truhum)
