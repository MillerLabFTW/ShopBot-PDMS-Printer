# Notes for Gcode preparation

Gcode is generated using the Cura machine profile. Crucially, you need to select "Only follow mesh surface" under expert options in Cura so you only get single-layer walls in your gcode. 

The same effect can be achieved in Slic3r by setting zero vertical shells and zero top and bottom layers. 

Note that depending on what needle you use on your syringe (we use [Nordson precision tips] (http://www.nordson.com/en/divisions/efd/products/dispense-tips/general-purpose-tips)), and what pressure you print at, the nozzle diameter will need to be changed. Our printing profile is based on printing with a 20GA 0.5" needle.

To print anything where the flow of PDMS needs to switch on and off (e.g. multiple parts next to each other, gaps between walls, etc), you need to add gcodes to open and close the solenoid valve. You can do this manually (see special gcodes below) or use a text munging tool we have provided. This simple script just looks through the original gcode for travel moves (G0 or G1 moves without an accompanying extrusion length) and turns off the pressure during these moves. 
The gcode munging script is supplied as a python script and and EXE.

## Special Gcodes for Pressure-driven extrusion

### M128 S## : Prime E2P
The electro-pneumatic transducer must be primed at the beginning of each print! This command requires a PWM value - we use M128 S110

### M127 : Close solenoid valve
Initiates flow of PDMS

### M129 : Vent solenoid
Stops flow of PDMS

# Start/end Gcode
### The following Gcode should be used at the beginning/end of each file (should be part of the Cura profile already):

Start.gcode
G21        ;metric values
G90        ;absolute positioning
M128 S110; ;prime e2p
G28 X0 Y0  ;move X/Y to min endstops
G28 Z0     ;move Z to max endstops
G1 X350 Y30 F2000 ;move to print origin
G1 Z0.5 F2000 ;move the platform down 15mm
G92 X0 Y0 Z0.5 ;set current position to origin

End.gcode
M127 ;close solenoid
M129 ;vent e2p
G28 Z0 ;home Z max
G28 X0 Y0 ;home X/Y min
M84                         ;steppers off
G90                         ;absolute positioning
;{profile_string}



