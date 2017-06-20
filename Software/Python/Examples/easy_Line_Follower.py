#!/usr/bin/env python
# Dexter Industries Distance Sensor example for the GoPiGo3
#
# This example shows a basic example to read sensor data from the Dexter Industries Distance Sensor.  This sensor is a white PCB. 
#
# Connect the Dexter Industries Distance Sensor to an I2C port on the GoPiGo3.
# You can find the Distance Sensor here: https://www.dexterindustries.com/shop/distance-sensor/
# Have a question about this example?  Ask on the forums here:  
# http://forum.dexterindustries.com/c/gopigo
# 
# Initial Date: 16 Jun 2017  John Cole
# http://www.dexterindustries.com/GoPiGo
'''
## License
 Copyright (C) 2017  Dexter Industries

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/gpl-3.0.txt>.
'''
from __future__ import print_function
from __future__ import division
from builtins import input
# the above lines are meant for Python3 compatibility.
# they force the use of Python3 functionality for print(), 
# the integer division and input()
# mind your parentheses!

# import the GoPiGo3 drivers
import easygopigo3 as easy
import time

# Create an instance of the Distance Sensor class.
Distance_Sensor = easy.DistanceSensor()     # Distance_Sensor will be the Line Follower object.

# Read the Distance Sensor
def get_sensorval():
    while True:
        val=Distance_Sensor.read_mm()           # Read the distance sensor in mm.
        # You can also read the sensor in cm or inches.  Uncomment the lines below to read in different units.
        # val=Distance_Sensor.read()            # Read the distance sensor in cm.
        # val=Distance_Sensor.read_inches()     # Read the distance sensor in inches.
        return val

while True:
    # Directly print the values of the sensor.
    print ("Distance Sensor Reading (mm): " + str(get_sensorval()))