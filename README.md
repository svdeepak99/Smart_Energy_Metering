# Smart_Energy_Metering

Using a Current Transformer and Voltage Transformer with signal conditioning circuits, the signal were fed to the Arduino’s ADC port to convert it
to the digital form to process it.

A miniature version of a Smart Meter was created to operate on 18V AC, and monitor the live stats of Voltage, Current, Power Factor, Power & Energy folowing in both ways (inwards and outwards) of a miniature house, which has different forms of loads.

The firmware was written in Arduino, and the UI was created with Python pygame package. The noises incurred while measuing the 50Hz waveform, were minimized by implementing a software-based Kalman Filter.
