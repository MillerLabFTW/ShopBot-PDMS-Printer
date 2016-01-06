###Munge File for #MillerLab PDMS Shopbot
#
# Ian Kinstlinger
# Revised 11/22/15
#
#

##DEFINE PAUSE TIME
#This is how long the system will wait between opening the solenoid valve
#and moving along the toolpath

#No pause leaves gaps in print
#0.5 s is a bit too high and you get a glob of PDMS at corners of print

pause = 0.25;

import math
import re
 
from Tkinter import Tk
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfilename
from tkFileDialog import asksaveasfile



print("\n\nChoose the original G-code file")


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
orig_gcode = askopenfilename() # show an "Open" dialog box and return the path to the selected file

print(orig_gcode)

Munged = asksaveasfile(mode='w', defaultextension=".gcode")

#outname = raw_input("Name for the output file: ")

#Munged = open(outname + ".gcode", 'a')


with open(orig_gcode, 'r') as original_gcode:
    for line in original_gcode:

        #Remove the carriage return that ends each line (for editing ease)
        line = line.replace('\n', '')


        #Fix XY motion commands

        if re.search('G0', line): #this line is a travel - turn off the pressure first

            line = "M127"  + '\n' + line + '\n' + "M126" + '\n' + "G4 S" + str(pause)

				
        
        #Add back the carriage return
        line += '\n'
        Munged.write(line)
                

                

                

                
