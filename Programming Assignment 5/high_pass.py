"""
ECE 4960 SPRING 2019
Programming Assignment 5
High-Pass Filter Simulation
Author: Tejas Advait (TA275)
"""

import numpy as np
from ode_solver import ForwardEuler, RK34, AdaptiveRK34, TRBDF2
from filter import Filter
import time
import matplotlib.pyplot as plt

#All physical values are in SI units

#R and C values
R = 300
L = 0.15
C = 1e-6

def VS(t):
	return (np.sin(2*np.pi*10*t) + np.sin(2*np.pi*500*t))

def F(R,L,C,VS,x,t):
	i = x[0]
	V = x[1]
	i1 = x[2]
	V1 = x[3]

	a = 2*np.pi*10
	b = 2*np.pi*500
	
	f1 = i1
	f2 = V1
	f3 = V1/L
	# f4 = -1*((np.sin(a*t)*a**2 + np.sin(b*t)*b**2) + i1/C + (R*V1)/L)
	f4 = ((VS(t+1e-6)-2*VS(t)+VS(t-1e-6))/1e-12) - i1/C - (R*V1)/L
	A = np.zeros((4,1),dtype = np.float64)
	A[0,0] = f1
	A[1,0] = f2
	A[2,0] = f3
	A[3,0] = f4
	return A


#Initial Conditions and Step Size
init_x = np.zeros((4,1),dtype = np.float64)
init_t = 0
end_t = 0.2
step1 = 1e-4
step2 = 0.2e-4

hpf = Filter(R,L,C,VS,F,init_x,init_t,end_t,step1,step2,"High-Pass","reports/high_pass")
hpf.generate()