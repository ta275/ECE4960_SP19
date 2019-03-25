# Programming Assignment 1: Arithmetic Exception Handling

This directory contains the implementation of a utility program that can observe and validate the exception handling of the integer and floating-point arithmetic in Python 3.7.0. The exception is validated against IEEE 754 standard for integer and floating-point representation by binary bits.

Computational schemes to observe the following exception handling rules are implemented:
* Integer overflow
* Integer division by 0
* Floating-point overflow
* Floating-point operations of INF and NINF
* Floating-point operations of NaN
* Signed zero
* Floating-point gradual underflow

Additionally, a [spigot algorithm](https://en.wikipedia.org/wiki/Spigot_algorithm) is implemented to calculate &#960 with **arbitrary digits** of precision. The first 30 digits after the decimal point are reported.

A short IEEE compliance report is generated to determine whether the platform obeys the IEEE 754 standard. A maximum of 10 violations is listed in this compliance report. A detailed log of the behavior for every rule is generated in a separate file.


## Usage

Run the main.py file in Python 3.7 to generate the reports.


## Author

**Tejas Advait**



## Acknowledgments

* Prof. Edwin Kan for providing the assignment details and continuous guidance.

* "Unbounded Spigot Algorithms for the Digits of Pi" by Jeremy Gibbons. The paper can be found [here](http://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf).