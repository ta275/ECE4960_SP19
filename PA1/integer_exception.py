#ECE 4960 Spring 2019
#Programming Assignment 1
#Integer Exceptions in Python 3.7.0
#Author: Tejas Advait (ta275)
#Date of Creation: Feb 12 2019

from common import *

#Integer overflow check using factorials
def overflow_fac():
	try:
		n = 50000
		fac = 1
		for i in range (2,n+1):
			fac = fac*i

		for i in range (2,n+1):
			fac = fac//i

		if (fac == 1):
			result.put(("Result of 50000!: No overflow",False))
		else:
			result.put(("Result of 50000!: Overflow caused.",False))

	except Exception as e:
		result.put(("Result of 50000!: " + str(e),False))



#Integer divided by zero
def zerodivision():
	try:
		a = int(0)
		b = int(10)//a
		if b == float('inf'):
			result.put(("Result of 10//0: "+str(b),False))
		else:
			result.put(("Result of 10//0: "+str(b),True))
	except Exception as e:
		result.put(("Result of 10//0: "+str(e), True))

def main():
	overflow_fac()
	zerodivision()
	return result
