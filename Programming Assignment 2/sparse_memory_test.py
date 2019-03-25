"""
ECE 4960 SPRING 2019
Programming Assignment 2
Sparse Memory-Usage Test Suite
Author: Tejas Advait (TA275)
"""

import math

import numpy as np
from scipy import sparse
from helper_test import *
from matrix import FullMatrix, SparseMatrix
import time
import pickle
from memory_profiler import profile


matrix1 = []
matrix2 = []
matrix3 = []
matrix4 = []
matrix5 = []

smatrix1 = []
smatrix2 = []
smatrix3 = []
smatrix4 = []
smatrix5 = []



def retrieve(inpt):
	for n in range(10000):
		i = np.random.randint(0,inpt.rowRank)
		j = np.random.randint(0,inpt.colRank)
		elem = inpt.retrieveElement(i,j)

def delete(inpt):
	for n in range(10000):
		i = np.random.randint(0,inpt.rowRank)
		j = np.random.randint(0,inpt.colRank)
		inpt.deleteElement(i,j)


def rowPermute(inpt):
	for n in range(400):
		i = np.random.randint(0,inpt.rowRank)
		j = np.random.randint(0,inpt.rowRank)
		inpt.rowPermute(i,j)


def rowScale(inpt):
	for n in range(400):
		i = np.random.randint(0,inpt.rowRank)
		j = np.random.randint(0,inpt.rowRank)
		a = np.random.random(1)[0]
		inpt.rowScale(i,j,a)

def productAx(inpt):
	total_time = 0
	for n in range(10):
		x = np.random.rand(inpt.colRank,1)
		fx = np2mat(x,FullMatrix)
		start = time.time()
		p = inpt.productAx(fx)
		end = time.time()
		total_time += (end-start)
	return total_time

f1 = open("memory_usage/add_scipy_mem.txt","w")
f2 = open("memory_usage/add_mem.txt","w")
f3 = open("memory_usage/retrieve_mem.txt","w")
f4 = open("memory_usage/delete_mem.txt","w")
f5 = open("memory_usage/rowPermute_mem.txt","w")
f6 = open("memory_usage/rowScale_mem.txt","w")
f7 = open("memory_usage/productAx_mem.txt","w")

@profile(stream = f1)
def initialize_csr():
	global matrix1
	global matrix2
	global matrix3
	global matrix4
	global matrix5
	matrix1 = sparse.random(500,500,density=0.01,format="csr",dtype= np.float64)
	matrix2 = sparse.random(1000,1000,density=0.01,format="csr",dtype= np.float64)
	matrix3 = sparse.random(1500,1500,density=0.01,format="csr",dtype= np.float64)
	matrix4 = sparse.random(2000,2000,density=0.01,format="csr",dtype= np.float64)
	matrix5 = sparse.random(2500,2500,density=0.01,format="csr",dtype= np.float64)

@profile(stream = f2)
def initialize_sparse():
	global smatrix1 
	global smatrix2 
	global smatrix3 
	global smatrix4 
	global smatrix5 
	smatrix1 = np2mat(matrix1,SparseMatrix)
	smatrix2 = np2mat(matrix2,SparseMatrix)
	smatrix3 = np2mat(matrix3,SparseMatrix)
	smatrix4 = np2mat(matrix4,SparseMatrix)
	smatrix5 = np2mat(matrix5,SparseMatrix)

@profile(stream = f3)
def retrieve_usage():
	retrieve(smatrix1)
	retrieve(smatrix2)
	retrieve(smatrix3)
	retrieve(smatrix4)
	retrieve(smatrix5)

@profile(stream = f4)
def delete_usage():
	delete(smatrix1)
	delete(smatrix2)
	delete(smatrix3)
	delete(smatrix4)
	delete(smatrix5)

@profile(stream = f5)
def rowPermute_usage():
	rowPermute(smatrix1)
	rowPermute(smatrix2)
	rowPermute(smatrix3)
	rowPermute(smatrix4)
	rowPermute(smatrix5)

@profile(stream = f6)
def rowScale_usage():
	rowScale(smatrix1)
	rowScale(smatrix2)
	rowScale(smatrix3)
	rowScale(smatrix4)
	rowScale(smatrix5)

@profile(stream = f7)
def productAx_usage():
	productAx(smatrix1)
	productAx(smatrix2)
	productAx(smatrix3)
	productAx(smatrix4)
	productAx(smatrix5)


if __name__ == '__main__':
	initialize_csr()
	initialize_sparse()
	retrieve_usage()
	delete_usage()
	rowPermute_usage()
	rowScale_usage()
	productAx_usage()