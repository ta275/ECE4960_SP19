#ECE 4960 Spring 2019
#Programming Assignment 1
#Integer Exceptions in Python 3.7.0
#Author: Tejas Advait (ta275)



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
			return "No overflow caused."
		else:
			return "Overflow caused."

	except:
		return "Programmer error in overflow_fac"



#Integer divided by zero
def zerodivision():
	try:
		a = int(0)
		return int(10)//a

	except ZeroDivisionError:
		return "Zero Division Error"

	except:
		"Programmer error in zerodivision"
