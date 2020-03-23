"""
ECE 4960 SPRING 2019
Programming Assignment 2
Sparse Runtime Test Suite
Author: Tejas Advait (TA275)
"""

import numpy as np
from scipy import sparse
from helper_test import *
from matrix import FullMatrix, SparseMatrix
import time
import pickle


matrix1 = sparse.random(500,500,density=0.01,format="csr",dtype= np.float64)
matrix2 = sparse.random(1000,1000,density=0.01,format="csr",dtype= np.float64)
matrix3 = sparse.random(1500,1500,density=0.01,format="csr",dtype= np.float64)
matrix4 = sparse.random(2000,2000,density=0.01,format="csr",dtype= np.float64)
matrix5 = sparse.random(2500,2500,density=0.01,format="csr",dtype= np.float64)



def create_and_time(inpt,num):
	start = time.time()
	sparse = np2mat(inpt,SparseMatrix)
	end = time.time()
	t = end - start
	file = open("runtime/sparse_{0}.bin".format(num),"wb")
	pickle.dump(sparse,file)
	file.close()
	return (sparse,t)



def retrieve_time(inpt):
	total_time = 0
	for n in range(10000):
		i = np.random.randint(0,inpt.rowRank)
		j = np.random.randint(0,inpt.colRank)
		start = time.time()
		elem = inpt.retrieveElement(i,j)
		end = time.time()
		total_time += (end-start)
	return total_time

def delete_time(inpt):
	total_time = 0
	for n in range(10000):
		i = np.random.randint(0,inpt.rowRank)
		j = np.random.randint(0,inpt.colRank)
		start = time.time()
		inpt.deleteElement(i,j)
		end = time.time()
		total_time += (end-start)
	return total_time


def rowPermute_time(inpt):
	total_time = 0
	for n in range(400):
		i = np.random.randint(0,inpt.rowRank)
		j = np.random.randint(0,inpt.rowRank)
		start = time.time()
		inpt.rowPermute(i,j)
		end = time.time()
		total_time += (end-start)
	return total_time

def rowScale_time(inpt):
	total_time = 0
	for n in range(400):
		i = np.random.randint(0,inpt.rowRank)
		j = np.random.randint(0,inpt.rowRank)
		a = np.random.random(1)[0]
		start = time.time()
		inpt.rowScale(i,j,a)
		end = time.time()
		total_time += (end-start)
	return total_time

def productAx_time(inpt):
	total_time = 0
	for n in range(10):
		x = np.random.rand(inpt.colRank,1)
		fx = np2mat(x,FullMatrix)
		start = time.time()
		p = inpt.productAx(fx)
		end = time.time()
		total_time += (end-start)
	return total_time

def time_function(func, filename,funcname):
	t1 = func(smatrix1)
	t2 = func(smatrix2)
	t3 = func(smatrix3)
	t4 = func(smatrix4)
	t5 = func(smatrix5)
	file = open("runtime/"+filename,"w")
	file.write("Timing of {0}\n\n".format(funcname))
	file.write("Matrix Rank        Time\n")
	file.write("===============================\n")
	file.write("%d              %.5f\n"%(smatrix1.rowRank,t1))
	file.write("%d             %.5f\n"%(smatrix2.rowRank,t2))
	file.write("%d             %.5f\n"%(smatrix3.rowRank,t3))
	file.write("%d             %.5f\n"%(smatrix4.rowRank,t4))
	file.write("%d             %.5f\n"%(smatrix5.rowRank,t5))
	file.close()

smatrix1,t1 = create_and_time(matrix1,1)
smatrix2,t2 = create_and_time(matrix2,2)
smatrix3,t3 = create_and_time(matrix3,3)
smatrix4,t4 = create_and_time(matrix4,4)
smatrix5,t5 = create_and_time(matrix5,5)

file = open("runtime/add_time.txt","w")
file.write("Timing of AddElement\n\n")
file.write("Matrix Rank        Time\n")
file.write("===============================\n")
file.write("%d              %.5f\n"%(smatrix1.rowRank,t1))
file.write("%d             %.5f\n"%(smatrix2.rowRank,t2))
file.write("%d             %.5f\n"%(smatrix3.rowRank,t3))
file.write("%d             %.5f\n"%(smatrix4.rowRank,t4))
file.write("%d             %.5f\n"%(smatrix5.rowRank,t5))
file.close()


file = open("runtime/sparse_1.bin","rb")
smatrix1 = pickle.load(file)
file.close()

file = open("runtime/sparse_2.bin","rb")
smatrix2 = pickle.load(file)
file.close()

file = open("runtime/sparse_3.bin","rb")
smatrix3 = pickle.load(file)
file.close()

file = open("runtime/sparse_4.bin","rb")
smatrix4 = pickle.load(file)
file.close()

file = open("runtime/sparse_5.bin","rb")
smatrix5 = pickle.load(file)
file.close()

time_function(retrieve_time,"retrieve_time.txt","RetrieveElement")
time_function(delete_time,"delete_time.txt","DeleteElement")
time_function(rowPermute_time,"rowPermute_time.txt","RowPermute")
time_function(rowScale_time,"rowScale_time.txt","RowScale")
time_function(productAx_time,"productAx_time.txt","ProductAx")