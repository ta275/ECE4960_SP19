# PA1: Arithmetic Exception Handling

This directory contains the implementation of a utility program that can observe and validate the exception handling of the integer and floating-point arithmetic in Python 3.7. The exception is validated against IEEE 754 standard for integer and floating-point representation by binary bits.

Computational schemes to observe the following exception-handling rules are implemented:
* Integer overflow
* Integer division by 0
* Floating-point overflow
* Floating-point gradual underflow
* Floating-point operations of INF and NINF
* Floating-point operations of NaN
* Signed zero

Additionally, a [spigot algorithm](https://en.wikipedia.org/wiki/Spigot_algorithm) is implemented to calculate π with **arbitrary digits** of precision. The first 30 digits after the decimal point are reported.

A short IEEE compliance report is generated to determine whether the platform obeys the IEEE 754 standard. A maximum of 10 violations is listed in this compliance report.

A detailed log of the behavior for every rule is generated in a separate file.

These reports can be found in the REPORTS directory.

## Files

* REPORTS - Directory containing all the reports
* common.py - Common functions to be used by other scripts
* float_inf_ninf_nan.py - Floating-Point operations of inf, ninf, nan in Python 3.7
* integer_exception.py - Integer exceptions in Python 3.7
* main.py - Generate compliance reports for Python 3.7
* signed_zero.py - Signed zero handling in Python 3.7
* **spigot_pi.py - Digits of Pi upto n (can be arbitrarily large) decimal places in Python 3.7**

## Usage


Download all the source code and run the main.py script in Python 3.7.6 to generate the reports in the REPORTS directory.

Feel free to use any other source code from any other file, as long as you acknowledge me.

I have tested the source code on Python 3.7 and Python 3.8, but it should work on any Python 3 platform.


## Author

**Tejas Advait**



## Acknowledgments

* Prof. Edwin Kan for theoretical details and guidance.

* "Unbounded Spigot Algorithms for the Digits of Pi" by Jeremy Gibbons. The paper can be found [here](http://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf).
