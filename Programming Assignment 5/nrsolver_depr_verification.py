"""
ECE 4960 SPRING 2019
Programming Assignment 5
Newton-Raphson Solver Verification
Author: Tejas Advait (TA275)
"""

from nrsolver import NRSolver
import numpy as np

# def f1(x):
# 	x = np.float64(x)
# 	return x + np.exp(x)

f1 = lambda x: np.float64(x) + np.exp(np.float64(x))

def f2(x):
	x = np.float64(x)
	return x**2 - 3*x - 2

def f3(x):
	x = np.float64(x)
	return x - np.log(1/x) + np.exp(x) - x**2 + 15*np.cos(x)




NR1 = NRSolver(f1,-0.7)
NR21 = NRSolver(f2,-0.6)
NR22= NRSolver(f2,3)
NR31 = NRSolver(f3,1.5)
NR32 = NRSolver(f3,3.5)

assert(abs(NR1.solve() + 0.567143290) < 1e-9)
assert(abs(NR21.solve() + 0.561552812) < 1e-9)
assert(abs(NR22.solve() - 3.561552812) < 1e-9)
assert(abs(NR31.solve() - 1.981925282) < 1e-9)
assert(abs(NR32.solve() - 2.974045163) < 1e-9)