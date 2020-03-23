"""
 * float_under_over.py
 *
 * Date Created: 12-Feb-2019
 * Author : Tejas Advait (ta275)
 *
 * Description: Floating-Point Overflow and Gradual Underflow in Python 3.7
 """

import math
from common import *

inf 

#Floating-point overflow check using factorials
def overflow_fac():
	try:
		n = 171
		fac = 1.0
		for i in range (2,n+1):
			fac = fac*i

		for i in range (2,n+1):
			fac = fac//i

		if (fac == 1):
			result.put(("Result of 171! (in floating-point) : No overflow",False))
		else:
			result.put(("Result of 171! (in floating-point) : "+str(fac),False))

	except Exception as e:
		result.put(("Result of 171! (in floating-point) : " + str(e),False))


temp1 = queue.Queue()
temp2 = queue.Queue()
temp3 = queue.Queue()
temp4 = queue.Queue()
def underflow_helper(x,y):
	r0 = x/10

	temp1.put((str(x)+" / 10 " , r0, r0))


	add_to_result(str(x)+" / 10 " , r0, r0)

	r1 = y - x
	temp2.put((str(y) + " - " + str(x), r1, r1))

	try:
		r2 = y/x
		temp3.put((str(y) + " / " + str(x), r2, r2))
	except Exception as e:
		r2 = e
		temp3.put((str(y)+" / " + str(x), r2, inf))

	try:
		r3 = math.sin(1.23456789012345*x)/x
		temp4.put(("sin(1.23456789012345*" + str(x) + ")/" + str(x), r3, r3))
	except Exception as e:
		r3 = e
		temp4.put(("sin(1.23456789012345*" + str(x) + ")/" + str(x), r3, 1.0))

def underflow():
	x = 1.2345678909876543
	y = 1.2345678909876543
	x *= 10**-307
	y *= 10**-303
	for i in range(0,20):
		underflow_helper(x,y)
		x /= 10



def queue_to_result(q):
	while (not q.empty()):
		a = q.get()
		add_to_result(a[0],a[1],a[2])

def main():
	try:
		large = (10.0**156)**2
	except Exception as e:
		large = e
	add_to_result("171!", large, inf)
	overflow_fac()
	underflow()
	queue_to_result(temp1)
	queue_to_result(temp3)
	queue_to_result(temp4)


