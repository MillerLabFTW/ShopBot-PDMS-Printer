# ShopBot PDMS Printer

##### Modified ShopBot Desktop CNC for pneumatic 3D printing of PDMS elastomer
##### Miller Lab: Physiologic Systems Engineering and Advanced Materials
##### jmil@rice.edu
&nbsp;

The ability to 3D print with PDMS (polydimethylsiloxane) is extremely useful in the lab for constructing custom lab equipment and devices. We are 3D printing PDMS via a modified ShopBot desktop CNC system. The toolhead of the ShopBot was replaced with a simple syringe mount and PDMS is extruded through the syringe under air pressure.

![ShotBot pic] (https://github.com/MillerLabFTW/ShopBot-PDMS-Printer/blob/master/Pics/PDMSShopBot.JPG?raw=true)

With an appropriate syringe mount, you can implement PDMS printing with this setup on any 3D printer running Marlin. We like the ShopBot for its robust construction and large build area. 


### Documentation
This git repository includes:
- STL files for 3D printing syringe-mount for the ShopBot
- Current firmware (modified Marlin for pressure-driven extrusion)
- Cura configuration and G-code munging script for G-code creation and processing
- Wiring diagram for electronics configuration (based on RAMBo electronics)
- Instructions for 3D printing with PDMS
- Bill of materials

Modifications to the ShopBot:
- Remove toolhead and replace with syringe holder (see Syringe Mount STLs)
- Remove motherboard and use RAMBo to signal onboard stepper drivers
- Install endstops 
- Install a build platform. We used extrusion pre-assembly nuts slipped in between the grooves of the ShopBot base to anchor an aluminum sheet for our build platform (spring-loaded for bed leveling). We print on glass, binder-clipped to the metal platform. 



![MillerLab logo](https://github.com/MillerLabFTW/OpenSLS/blob/master/MillerLab_logo.jpg)