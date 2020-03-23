#ECE 4960 Spring 2019
#Programming Assignment 1
#Signed Zero Handling in Python 3.7.0
#Author: Tejas Advait (ta275)
#Date of Creation: Feb 12 2019

from common import *
import math

def limit_0(positive, f,name):
	x = 1.23456789012345
	if not positive:
		x *= -1
	x *= 10**-307

	for i in range(0,20):
		try:
			r = f(x)
			add_to_result(name.format(x), r, r)
		except Exception as e:
			add_to_result(name.format(x), e, 1)

		x/=10


def main():
	limit_0(True, lambda x : math.log(x),"log({0})")
	limit_0(False, lambda x : math.log(x),"log({0})")
	limit_0(True, lambda x : math.sin(x)/x,"sin({0}) / {0}")
	limit_0(False, lambda x : math.sin(x)/x,"sin({0}) / {0}")
	limit_0(False, lambda x : math.sin(x)/abs(x),"sin({0}) / |{0}|")
