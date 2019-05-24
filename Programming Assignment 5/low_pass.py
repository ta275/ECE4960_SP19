"""
ECE 4960 SPRING 2019
Programming Assignment 5
Low-Pass Filter Simulation
Author: Tejas Advait (TA275)
"""

import numpy as np
from ode_solver import ForwardEuler, RK34, AdaptiveRK34, TRBDF2
from filter import Filter
import time
import matplotlib.pyplot as plt

#All physical values are in SI units

#R and C values
R = 60
L = 0.27
C = 47e-6

def VS(t):
	return (np.sin(2*np.pi*20*t) + np.sin(2*np.pi*500*t) + np.sin(2*np.pi*140))

def F(R,L,C,VS,x,t):
	i = x[0]
	V = x[1]
	f1 = (VS(t) - V - i*R)/L
	f2 = i/C
	A = np.zeros((2,1),dtype = np.float64)
	A[0,0] = f1
	A[1,0] = f2
	return A

#Initial Conditions and Step Size
init_x = np.zeros((2,1),dtype = np.float64)
init_t = 0
end_t = 0.2
step1 = 1e-4
step2 = 0.2e-4

lpf = Filter(R,L,C,VS,F,init_x,init_t,end_t,step1,step2,"Low-Pass","reports/low_pass")
lpf.generate()