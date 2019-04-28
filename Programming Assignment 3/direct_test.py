"""
ECE 4960 SPRING 2019
Programming Assignment 3
Direct Full Solver Test
Author: Tejas Advait (TA275)
"""
import numpy as np
from direct_full_solver import Direct_Full_Solver
from helper_test import *
from matrix import FullMatrix

tol = np.float64(1e-7)
count = 0
for i in range(1000):
	rank = np.random.randint(1,15)
	matrix = np.random.rand(rank,rank)
	mult1 = np.random.randint(1,100)
	matrix *= mult1
	if np.linalg.det(matrix) != 0:
		A = np2mat(matrix, FullMatrix)
		col = np.random.rand(rank,1)
		mult2 = np.random.randint(0,100)
		col *= mult2
		b = np2mat(col,FullMatrix)
		S = Direct_Full_Solver(A,b)
		S.solve()
		x = np.dot(np.linalg.inv(matrix),col)
		assert (norm2np(S.x,x) < tol)
		count += 1

print ("Tested {0} linear equations with non-singular matrices. Tolerance = {1}".format(count,tol))