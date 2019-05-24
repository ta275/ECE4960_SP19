"""
ECE 4960 SPRING 2019
Programming Assignment 5
Band-Pass Filter Simulation
Author: Tejas Advait (TA275)
"""

import numpy as np
from ode_solver import ForwardEuler, RK34, AdaptiveRK34, TRBDF2
from filter import Filter
import time
import matplotlib.pyplot as plt

#All physical values are in SI units

#R and C values
R = 70
L = 0.27
C = 4.7e-6

def VS(t):
	return (np.sin(2*np.pi*10*t) + np.sin(2*np.pi*500*t)) + np.sin(2*np.pi*140*t)

def F(R,L,C,VS,x,t):
	i = x[0]
	V = x[1]
	i1 = x[2]
	V1 = x[3]

	a = 2*np.pi*10
	b = 2*np.pi*500
	c = 2*np.pi*140
	
	f1 = i1
	f2 = V1
	f3 = ((VS(t+0.5e-6)-VS(t-0.5e-6))/1e-6 - V1 - (i/C))/L
	f4 = R*((VS(t+0.5e-6)-VS(t-0.5e-6))/1e-6 - V1 - (i/C))/L
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

hpf = Filter(R,L,C,VS,F,init_x,init_t,end_t,step1,step2,"Band-Pass","reports/band_pass")
hpf.generate()