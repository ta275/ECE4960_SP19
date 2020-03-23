"""
ECE 4960 SPRING 2019
Programming Assignment 3
Numerical Differentiation
Authors: Tejas Advait (TA275)

This file provides numerical differentiation functions.
"""

import numpy as np
import copy

default_h = np.float64(10**-5)

def fd_diff1(f, x, i, h = default_h):
	"""
	Returns the first derivative of f with respect to x's ith variable using 
	forward approximation.

	f: A python function definition which takes in a numpy array as an argument. The numpy
	array represents the x vector.

	x: A 1D numpy array which represents the input to f. The derivative is calculated at x.

	i: The index of variable with respect to which the derivative is calculated.

	h: step size for the calculation of the derivative.

	"""
	n = x.shape[0]

	x_new = np.zeros(n,dtype = np.float64)
	x_new += x
	x_new[i] += h

	return (f(x_new)-f(x))/h



def fd_diff2(f, x, i, j, h = default_h):
	"""
	Returns the second derivative of f with respect to x's ith variable and jth variable
	using forward approximation.

	f: A python function definition which takes in a numpy array as an argument. The numpy
	array represents the x vector.

	x: A 1D numpy array which represents the input to f. The second derivative is 
	calculated at x.

	i: The index of the first variable with respect to which the derivative is calculated.

	j: The index of the second variable with respect to which the derivative is calculated.

	h: step size for the calculation of the derivative.
	"""

	n = x.shape[0]
	x_new1 = np.zeros(n,dtype = np.float64)
	x_new2 = np.zeros(n,dtype = np.float64)
	x_new3 = np.zeros(n,dtype = np.float64)
	
	x_new1[i] += h
	x_new1[j] += h
	x_new1 += x

	x_new2[j] += h
	x_new2 += x
	
	x_new3[i] += h
	x_new3 += x

	return (f(x_new1) - f(x_new2) - f(x_new3) + f(x))/h**2


def bd_diff1(f, x, i, h = default_h):
	"""
	Returns the first derivative of f with respect to x's ith variable using 
	backward approximation.

	f: A python function definition which takes in a numpy array as an argument. The numpy
	array represents the x vector.

	x: A 1D numpy array which represents the input to f. The derivative is calculated at x.

	i: The index of variable with respect to which the derivative is calculated.

	h: step size for the calculation of the derivative.

	"""
	n = x.shape[0]
	x_new = np.zeros(n,dtype = np.float64)
	x_new[i] -= h
	x_new += x

	return (f(x)-f(x_new))/h

def bd_diff2(f, x, i, j, h = default_h):
	"""
	Returns the second derivative of f with respect to x's ith variable and jth variable
	using backward approximation.

	f: A python function definition which takes in a numpy array as an argument. The numpy
	array represents the x vector.

	x: A 1D numpy array which represents the input to f. The second derivative is 
	calculated at x.

	i: The index of the first variable with respect to which the derivative is calculated.

	j: The index of the second variable with respect to which the derivative is calculated.

	h: step size for the calculation of the derivative.
	"""
	return fd_diff2(f, x, i, j, -1*h)

def cd_diff1(f, x, i, h = default_h):
	"""
	Returns the first derivative of f with respect to x's ith variable using 
	central approximation.

	f: A python function definition which takes in a numpy array as an argument. The numpy
	array represents the x vector.

	x: A 1D numpy array which represents the input to f. The derivative is calculated at x.

	i: The index of variable with respect to which the derivative is calculated.

	h: step size for the calculation of the derivative.

	"""
	n = x.shape[0]
	x_new = np.zeros(n,dtype = np.float64)

	x_new = x_new + x
	x_new[i] = x_new[i] + h
	a = f(x_new)

	x_new[i] = x_new[i] - 2*h
	b = f(x_new)

	return (a-b)/(2*h)

def cd_diff2(f, x, i, j, h = default_h, k = default_h):
	"""
	Returns the second derivative of f with respect to x's ith variable and jth variable
	using forward approximation.

	f: A python function definition which takes in a numpy array as an argument. The numpy
	array represents the x vector.

	x: A 1D numpy array which represents the input to f. The second derivative is 
	calculated at x.

	i: The index of the first variable with respect to which the derivative is calculated.

	j: The index of the second variable with respect to which the derivative is calculated.

	h: step size for the calculation of the derivative.
	"""

	k = h
	n = x.shape[0]
	x_new = np.zeros(n,dtype = np.float64)
	x_new = x_new + x

	x_new[i] = x_new[i] + h
	x_new[j] = x_new[j] + k
	a = f(x_new)

	x_new[i] = x_new[i] - 2*h
	b = f(x_new)

	x_new[j] = x_new[j] - 2*k
	d = f(x_new)

	x_new[i] = x_new[i] + 2*h
	c = f(x_new)

	return (a-b-c+d)/(4*h*k)