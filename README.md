#ShopBot PDMS Printer

#####Modified ShopBot Desktop CNC for pneumatic 3D printing of PDMS elastomer
#####Miller Lab: Physiologic Systems Engineering and Advanced Materials
#####[millerlab.rice.edu](http://millerlab.rice.edu)
&nbsp;

The ability to 3D print with PDMS (polydimethylsiloxane) is extremely useful in the lab for constructing custom lab equipment and devices. We are 3D printing PDMS via a modified ShopBot desktop CNC system. The toolhead of the ShopBot was replaced with a simple syringe mount and PDMS is extruded through the syringe under air pressure.

![ShotBot pic](https://github.com/MillerLabFTW/ShopBot-PDMS-Printer/blob/master/Pics/PDMSShopBot.JPG?raw=true)

With an appropriate syringe mount, you can implement PDMS printing with this setup on any 3D printer running Marlin. We like the ShopBot for its robust construction, high-precision positioning, and large build area. 


###Documentation
This git repository includes:
- STL files for 3D printing syringe-mount for the ShopBot
- Current firmware (modified Marlin for pressure-driven extrusion)
- Cura configuration and G-code munging script for G-code creation and processing
- Wiring diagram for electronics configuration (based on RAMBo electronics)
- Instructions for 3D printing with PDMS
- Bill of materials

###Modifications to the ShopBot:
- Remove toolhead and replace with syringe holder (see Syringe Mount STLs)
- Remove motherboard and use RAMBo to signal onboard stepper drivers
- Install endstops 
- Install a build platform. We used extrusion pre-assembly nuts slipped in between the grooves of the ShopBot base to anchor an aluminum sheet for our build platform (spring-loaded for bed leveling). We print on glass, binder-clipped to the metal platform. 



![MillerLab logo](https://github.com/MillerLabFTW/OpenSLS/blob/master/MillerLab_logo.jpg)

###Acknowledgements

3D printing of PDMS in this formulation was first demonstrated in Jennifer Lewis' lab at Harvard University:

D. B. Kolesky, R. L. Truby, A. S. Gladman, T. A. Busbee, K. A. Homan and J. A. Lewis, Adv. Mater., 2014, 26, 3124–3130.

Hat-tip to the [Lewis lab](http://lewisgroup.seas.harvard.edu/) for all the exciting 3D printing work that they do.

- Thanks to ShopBot for assistance modifying their desktop unit to be driven by RAMBo
- Thanks to Ultimachine for RAMBo support and assistance with electropneumatic transducers
- Thanks to the Marlin dev team and all the other open-source tools that support 3D printing
