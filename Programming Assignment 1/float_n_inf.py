#ECE 4960 Spring 2019
#Programming Assignment 1
#Floating-Point operations of inf and ninf in Python 3.7.0
#Author: Tejas Advait (ta275)

#def overflow_fac:


import math

#n_inf_1() returns a dictionary with results of the first set of inf and ninf operations
def n_inf_1():
	
	val = {}

	ninf = float('-inf')
	
	inf = float('inf')
	
	try:
		z = 1/inf
	except:
		z = "Programmer error in 1/inf"

	try:
		nz = 1/ninf
	except:
		nz = "Programmer error in 1/(-inf)"

	z_eq_nz = (z == nz)


	val["+zero"] = z
	val["-0"]
	

	try:
		sin_inf = math.sin(inf)
	except ValueError:
		sin_inf = 'Tried to calculate math.sin(inf). Got Value Error: math domain error."'
	except:
		sin_inf - 'Programmer error in math.sin(inf).'


	try:
		sin_ninf = math.sin(ninf)
	except ValueError:
		sin_ninf = 'Tried to calculate math.sin(-inf). Got Value Error: math domain error."'
	except:
		sin_ninf = 'Programmer error in math.sin(-inf).'


	try:
		exp_inf = math.exp(inf)
	except:
		exp_inf - 'Programmer error in math.exp(inf).'


	try:
		exp_ninf = math.exp(ninf)
	except:
		exp_ninf = 'Programmer error in math.exp(-inf).'

	try:
		log_ninf = math.log(ninf)
	except ValueError:
		log_ninf = 'Tried to calculate math.log(-inf). Got Value Error: math domain error."'
	except:
		log_ninf = 'Programmer error in math.log(-inf).'


	try:
		log_inf = math.exp(inf)
	except:
		log_inf - 'Programmer error in math.log(inf).'









def n_inf_add():

	try:
		inf_add_ninf = inf + ninf
		
		ninf_add_inf = ninf + inf
		
		inf_add_inf = inf + inf

		ninf_add_ninf = ninf + ninf

	inf_sub_ninf = inf - ninf
	
	ninf_sub_inf = ninf - inf
	
	inf_sub_inf = inf - inf

	ninf_sub_ninf = ninf - ninf

	inf_mul_ninf = inf + ninf
	
	ninf_mul_inf = ninf + inf
	
	inf_mul_inf = inf + inf

	ninf_mul_ninf = ninf + ninf
