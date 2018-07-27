'''
JSONtoCSV.py

Mohamed Ebsim

Contact Jesse Rogerson, @ jrogerson@ingeniumcanada.org

Originally created on July 26, 2018
-----------------------------

This program was created in order to conver the data into
a .csv file in order to use it in certain application, such
as graphing in a program like Excel.

-----------------------------
Resources Used:

https://stackoverflow.com/a/29132429
http://stackabuse.com/reading-and-writing-csv-files-in-python/
https://stackoverflow.com/a/3976765
https://stackoverflow.com/a/6921760

'''

# Import Libraries
import csv
import json
from collections import OrderedDict

# Load in JSON file and convert it into an Ordered Dict
json_data = open("log.json")
data = json.load(json_data, object_pairs_hook=OrderedDict)

# Headers of the table
headers = ["datetime", "temperature", "pressure", "altitude", "sensorVoltage","humidity","trueHumidity"]

# Create a .csv file and start a writer with the headers
file = open("data.csv","w")
writer = csv.DictWriter(file, headers)

# Write the headers to the top
writer.writeheader()

# This loop will go through every row of the JSON file
# and save it to the .csv file
print("Starting loop")

for i in range(0,len(data)):
    row = data[i]
    writer.writerow(row)

print("Finished loop")

# Close up the file
json_data.close()
file.close()
