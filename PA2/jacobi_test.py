"""
ECE 4960 SPRING 2019
Programming Assignment 2
Jacobi Solver Testing
Author: Tejas Advait (TA275)
"""

import math
import numpy as np
from matrix import FullMatrix, SparseMatrix
import pickle
from jacobi import Jacobi_Solver

f = open("mat1/sparse_mat1.bin", "rb")
mat1 = pickle.load(f)
f.close()

b1 = FullMatrix(mat1.rowRank,1) #b-vector with 1 in its first row
b2 = FullMatrix(mat1.rowRank,1) #b-vector with 1 in its fifth row
b3 = FullMatrix(mat1.rowRank,1) #b-vector with 1 in every row

b1.addElement(0, 0, 1.0)
b2.addElement(4, 0, 1.0)
for i in range (b3.rowRank):
	b3.addElement(i,0,1.0)

J1 = Jacobi_Solver(mat1,b1) #System with mat1 and b1
J2 = Jacobi_Solver(mat1,b2) #System with mat1 and b2
J3 = Jacobi_Solver(mat1,b3) #System with mat1 and b3

J1.solve()
J2.solve()
J3.solve()


#Reporting normalized residual norms
file = open("reports\\residual_norms.txt","w+")
file.write("Residual Norms\n")
file.write("\n")
file.write("Matrix        b-transpose             Residual Norm        # of Iterations\n")
file.write("==========================================================================\n")
file.write("mat1       (1.0,0,0,...,0)      {0}        {1}\n".format(J1.residual_norm(),J1.max_iter))
file.write("mat1     (0,0,0,0,1.0,0...,0)   {0}       {1}\n".format(J2.residual_norm(),J3.max_iter))
file.write("mat1    (1.0,1.0,1.0,...,1.0)   {0}       {1}\n".format(J3.residual_norm(),J2.max_iter))
file.close()