'''
receiveData.py

Mohamed Ebsim

Contqact Jesse Rogerson, @ jrogerson@ingeniumcanada.org

Originally created on Jully 11, 2018
-------------------------------------

This program is made to read from the serial port and
decode it in order for future use. It currently saves
the data to an MySQL database.

-------------------------------------

Resources Used:

https://www.tutorialspoint.com/python3/python_database_access.htm
http://www.penguintutor.com/electronics/rpi-arduino

'''

#Import Libraries
import serial
import time
import pymysql

#Setting up serial connection through port ACM0 with a rate of 9600 baud
ser = serial.Serial('/dev/ttyACM0', 9600)    

# set basic values for the variables
temp = 0 # temperature
pres = 0 # pressure
altitude = 0 # altitude
sV = 0 # sensor Voltage (for the humidity sensor)
hum = 0 # relative humidity
truhum = 0 # true relative humidity

#Setting up for use of MySQL database
username = ""
password = ""
databaseName = ""

database = pymysql.connect("localhost",username,password,databaseName)
cursor = database.cursor()

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
        tempNew = float(data[14:-4])
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

x = 0

# This python program currently only runs 600 times.
while x < 600:
    # Calls to update the data
    updateData()
    if(x % 6 == 0):
        #Finds time
        timeDate = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
        
        # Command to add to table "log" the data
        sql = ("""INSERT INTO log (datetime, temperature, pressure, altitude, sensorVoltage, humidity, trueHumidity) VALUES (%s,%s,%s,%s,%s,%s,%s)""",(timeDate,temp,pres,altitude,sV,hum,truhum))
        
        # Tries to run command and prints outcome
        try:
            print("Writing to database...")
            cursor.execute(*sql)
            database.commit()
            print("Write Complete")
        except:
            database.rollback()
            print("Failed writing to database")
    
    # Increases x until the loop breaks
    x+=1

# Closes/terminates variables for database
cursor.close()
database.close()

# Prints out the final data
print(temp)
print(pres)
print(altitude)
print(sV)
print(hum)
print(truhum)
