#ECE 4960 Spring 2019
#Programming Assignment 1
#Floating-Point operations of inf, ninf, nan in Python 3.7.0
#Author: Tejas Advait (ta275)
#Date of Creation: Feb 12 2019


from common import *



def n_inf_1():
	
	try:
		z = 1/inf
		add_to_result("1/inf", z, 0.0)
	except Exception as e:
		add_to_result("1/inf", e, 0.0)

	try:
		z = 1/ninf
		add_to_result("1/ninf", z, 0.0)
	except Exception as e:
		add_to_result("1/ninf", e, 0.0)

	exp1 = [inf, ninf, nan, nan, nan, nan, inf, ninf, inf, inf, ninf, ninf, nan, nan, nan, nan]
	basic_ops_result(inf,ninf,exp1)

	exp2 = [inf, 20.0, inf, inf, nan, 0.0, inf, ninf, inf, 100, inf, inf, nan, 1.0, inf, 0.0]
	basic_ops_result(inf,10,exp2)

	exp3 = [ninf, 20.0, ninf, ninf, nan, 0.0, ninf, inf, inf, 100, ninf, ninf, nan, 1.0, ninf,0.0]
	basic_ops_result(ninf,10.0,exp3)

	exp4 = [inf, 0.0, inf, inf, nan, 0.0, inf, ninf, inf, 0.0, nan, nan, nan, nan, inf, 0.0]
	basic_ops_result(inf,0.0,exp4)

	exp5 = [ninf, 0.0, ninf, ninf, nan, 0.0, ninf, inf, inf, 0.0, nan, nan, nan, nan, ninf, 0.0]
	basic_ops_result(ninf,0.0,exp5)



def n_inf_2():
	
	exp1 = [0.0,nan,inf,inf]
	single_ops_result(inf,exp1)
	exp2 = [0.0,nan,0.0,nan]
	single_ops_result(ninf,exp2)

def nan_ops():
	exp1 = [nan, 20.0, nan, nan, nan, 0.0, nan, nan, nan, 100.0, nan, nan, nan, 1.0, nan, nan]
	basic_ops_result(nan,10.0,exp1)

	exp2 = [nan, 0.0, nan, nan, nan, 0.0, nan, nan, nan, 0.0, nan, nan, nan, nan, nan, nan]
	basic_ops_result(nan,0.0,exp2)

	exp3 = [nan, inf, nan, nan, nan, nan, nan, nan, nan, inf, nan, nan, nan, nan, nan, nan]
	basic_ops_result(nan,inf,exp3)


	exp4 = [nan, ninf, nan, nan, nan, nan, nan, nan, nan, inf, nan, nan, nan, nan, nan, nan]
	basic_ops_result(nan,ninf,exp4)

	exp5 = [nan,nan,nan,nan]
	single_ops_result(nan,exp5)


def main():
	n_inf_1()
	n_inf_2()
	nan_ops()
