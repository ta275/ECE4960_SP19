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

f1 = lambda x: np.array([np.float64(x[0,0]) + np.exp(np.float64(x[0,0]))]).reshape((1,1))

def f2(x):
	return np.array([x[0,0]**2 - 3*x[0,0] - 2]).reshape(1,1)

def f3(x):
	return np.array([x[0,0] - np.log(1/x[0,0]) + np.exp(x[0,0]) - x**2 + 15*np.cos(x[0,0])]).reshape((1,1))

def f4(x):
	a = f1(np.array([x[0]]).reshape(1,1))
	b = f2(np.array([x[1]]).reshape(1,1))
	c = f3(np.array([x[2]]).reshape(1,1))
	return ((np.array([a,b,c],dtype=np.float64)).flatten()).reshape(3,1)


NR1 = NRSolver(f1,1,[[-0.7]])
NR21 = NRSolver(f2,1,[[-0.6]])
NR22= NRSolver(f2,1,[[3]])
NR31 = NRSolver(f3,1,[[1.5]])
NR32 = NRSolver(f3,1,[[3.5]])

NR41 = NRSolver(f4,3,[[-0.7],[-0.6],[1.5]])
NR42 = NRSolver(f4,3,[[-0.7],[3],[1.5]])
NR43 = NRSolver(f4,3,[[-0.7],[-0.6],[3.5]])
NR44 = NRSolver(f4,3,[[-0.7],[3],[3.5]])

assert(abs(NR1.solve()[0,0] + 0.567143290) < 1e-9)
assert(abs(NR21.solve()[0,0] + 0.561552812) < 1e-9)
assert(abs(NR22.solve()[0,0] - 3.561552812) < 1e-9)
assert(abs(NR31.solve()[0,0] - 1.981925282) < 1e-9)
assert(abs(NR32.solve()[0,0] - 2.974045163) < 1e-9)

assert(np.linalg.norm(NR41.solve()) - np.linalg.norm(np.array([-0.567143290,-0.561552812,1.981925282])) < 1e-8)
assert(np.linalg.norm(NR42.solve()) - np.linalg.norm(np.array([-0.567143290, 3.561552812,1.981925282])) < 1e-8)
assert(np.linalg.norm(NR43.solve()) - np.linalg.norm(np.array([-0.567143290,-0.56155281,2.97404516])) < 1e-8)
assert(np.linalg.norm(NR44.solve()) - np.linalg.norm(np.array([-0.567143290,3.561552812,2.974045163])) < 1e-8)