# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 00:27:45 2023

@author: divak
"""


import time

# Input file name
filename = input("Enter log file name: ")

# Open the input file
with open(filename, 'r') as file:
    # Read the contents of the file
    contents = file.readlines()

    # Loop through each line in the file
    for line in contents:
        # Split the line into timestamp and message
        timestamp, message = line.split(':', 1)

        # Convert the timestamp to human-readable format
        timestamp = time.strftime('%a %d %b %Y %H:%M:%S', time.localtime(float(timestamp)))

        # Print the converted timestamp and message
        print(f"{timestamp}:{message}", end="")
