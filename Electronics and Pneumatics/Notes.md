# Pneumatics

Air should flow through the following series of components:

0. Tank or wall (~100 psi)
1. Regulator (~35 psi)
2. Electropneumatic transducer
3. Solenoid valve
4. Tubing to stoppered syringe

The transducer provides (some) pressure control while the solenoid valve rapidly applies and removes pressure to start and stop flow of PDMS. 

# Electronics

- It's necessary to convert PWM output from the RAMBo to a constant-voltage signal. We are using an "E2P" adapter from Ultimachine
- Wire the grounds together on the RAMBo and ShopBot power supplies to match ground planes
- A simple diagram is provided for connecting RAMBo motor ext pins to ShopBot stepper drivers via a 37-pin connector. We've also included pinout info for RAMBo and the ShopBot (thanks Shopbot!) for full specs.
