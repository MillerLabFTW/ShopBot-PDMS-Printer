# Printing with PDMS

### Materials Preparation

We are using non-flowing PDMS: [Dow Corning SE 1700] (http://www.dowcorning.com/applications/search/products/details.aspx?prod=01707116&type=PROD)
The mix of PDMS follows a 10 of base: 1 of catalyst. 

1. Grab a 60mL syringe. This is where we will deposit the materials. Remove the plunger at this time.
Use a luer lock stopper for the tip of the syringe. This will prevent materials from seeping out.
Place syringe in a cup on scale and tare to 0 g.  Use spatula to add base to syringe.  Avoid touching the material to the sides of the syringe, and try to get as much of the base towards the bottom of the syringe as possible.  (N.B. If too much of the base gets stuck on the sides of the syringe, you can centrifuge the syringe prior to adding the catalyst). 
2. Once the appropriate portions are added to the syringe, stir vigorously with a spatula for at least 5 minutes.
3. To rid the syringe of any air bubbles, we will now centrifuge the PDMS solution. Parafilm the top of the syringe to prevent any spills. You will likely need an special adapter for your centrifuge - we have a printed adapter for the 60mL syringe on our Allegra X-15R centrifuge and to counter weight! **Spin for 4 minutes at 2500CFM.**
4. Once the syringe is spun down and air bubbles are gone, remove the syringe from the centrifuge. If not, run it again until the mixture is bubble free. Decompress the bottom of the syringe if it was deformed in the centrifuge.
Grab the plunger for the syringe and cut it down at the first reinforced inner ring, this will be our piston for the air to press against. I like to drill a hole in the plunger so PDMS isn't lost while inserting the plunger.

5. Once the plunger is positioned well below the top of the syringe, you can now attach the syringe tip..
We can now load it onto the Shugabot with the proper adapter.
The 60mL syringe should fit rather snuggly into the holder. It will get a bit tighter around the area where the plunger is, apply a bit of force and it should clear it.
Seat the syringe all the way to the bottom, so that the flanges rest on the printer side walls.
Attach and secure the rubber stopper now. Tighten the four bolts around the stopper holder.
At this point you are ready to move over to the software side of things

### Slicing for PDMS Printing of Basic Profiles 

We will be using Cura to print with PDMS. The structures you can print at this time are only perimeters of objects, that is single/thin walled objects with little to no overhang. Further experimentation is needed for more complex geometries.

Open Cura and create a new machine. Go under “Machine” and choose “Add new machine” to do so.

A Cura profile has been created for use with 15ga needles (1.37mm ID). Feel free to change the various parameters such as speeds and layer thicknesses, just remember the nozzle size as a lot of parameters are based around it.

Go under the “Expert” option and go into “Open Expert Settings”. Make sure that “Only follow mesh contours” is checked. This is how we are achieving the single walled prints.


Once the settings are to your liking, go ahead and export the g-code. We will still need to modify the code physically.
Open the g-code file and find the start of the actual object. It is after the start sequence and is usually signified with a G0 move (a travel move). You need to add a M126 right before the G1 move that follows. This will allow the solenoid to open.
Since we are printing continuously so to speak, we simply need to have it turn of once it starts on the object. We also need to add a M127 to the last line of g-code for the object. This will close the solenoid.
**Note: This step (manual editing of gcode) is replaced by the gcode munging utility.**

Also ensure that the start and end gcode sequence is the following: (you can copy and paste if needed)

````
Start.gcode

;Sliced at: {day} {date} {time}
;Basic settings: Layer height: {layer_height} Walls: {wall_thickness} Fill: {fill_density}
;Print time: {print_time}
;Filament used: {filament_amount}m {filament_weight}g
;Filament cost: {filament_cost}
;M190 S{print_bed_temperature} ;Uncomment to add your own bed temperature line
;M109 S{print_temperature} ;Uncomment to add your own temperature line
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
```
