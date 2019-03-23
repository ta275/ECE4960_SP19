"""
ECE 4960 SPRING 2019
Programming Assignment 2
Matrix Module Test Suite
Author: Tejas Advait (TA275)
"""

import math
import unittest
import numpy as np
from scipy import sparse
from matrix import FullMatrix, SparseMatrix

def norm2(mat1,mat2):
	"""
	Calculates the second norm for comparing mat1 and mat2.

	mat1: A matrix in either full or sparse format
	mat2: A matrix in either full or sparse format

	Returns: Frobenius second norm of the matrix (mat1 - mat2)
	"""
	result = 0
	for i in range (mat1.rowRank):
		for k in range (mat2.colRank):
			a1 = mat1.retrieveElement(i,k)
			a2 = mat2.retrieveElement(i,k)
			s = (a1-a2)**2
			result += s
	return math.sqrt(result)




class TestPartI(unittest.TestCase):
	"""
	Test suite for part I, when ground truth is known.
	"""
	def setUp(self):
		self.A = [
		[1, 2, 0, 0, 3],
		[4, 5, 6, 0, 0],
		[0, 7, 8, 0, 9],
		[0, 0, 0, 10, 0],
		[11, 0, 0, 0, 12]]

		self.x = [
		[5],
		[4],
		[3],
		[2],
		[1]]

		self.x_full = FullMatrix(5,1)
		
		self.A_full = FullMatrix(5,5)
		self.A_sparse = SparseMatrix(5,5)

		for i in range(5):
			self.x_full.addElement(i,0,self.x[i][0])
			for j in range(5):
				self.A_full.addElement(i,j,self.A[i][j])
				self.A_sparse.addElement(i,j,self.A[i][j])


	def test_rowPermute(self):
		self.A_full.rowPermute(0,2)
		self.A_full.rowPermute(0,4)
		self.A_sparse.rowPermute(0,2)
		self.A_sparse.rowPermute(0,4)
		self.x_full.rowPermute(0,2)
		self.x_full.rowPermute(0,4)

		self.assertTrue(norm2(self.A_full, self.A_sparse) == 0.0)

	def test_rowScale(self):
		self.A_full.rowScale(0,3,3)
		self.A_full.rowScale(4,1,-4.4)
		self.A_sparse.rowScale(0,3,3)
		self.A_sparse.rowScale(4,1,-4.4)
		self.x_full.rowScale(0,3,3)
		self.x_full.rowScale(4,1,-4.4)
		self.assertTrue(norm2(self.A_full, self.A_sparse) == 0.0)


	def test_productAx(self):
		full = self.A_full.productAx(self.x_full)
		sparse = self.A_sparse.productAx(self.x_full)
		self.assertTrue(norm2(full,sparse) == 0.0)

	def test_combined(self):
		self.A_full.rowPermute(0,2)
		self.A_full.rowPermute(0,4)
		self.A_sparse.rowPermute(0,2)
		self.A_sparse.rowPermute(0,4)
		self.A_full.rowScale(0,3,3)
		self.A_full.rowScale(4,1,-4.4)
		self.A_sparse.rowScale(0,3,3)
		self.A_sparse.rowScale(4,1,-4.4)
		self.x_full.rowPermute(0,2)
		self.x_full.rowPermute(0,4)
		self.x_full.rowScale(0,3,3)
		self.x_full.rowScale(4,1,-4.4)

		full = self.A_full.productAx(self.x_full)
		sparse = self.A_sparse.productAx(self.x_full)
		self.assertTrue(norm2(full,sparse) == 0.0)



def helper_partII(A,b):
	"""
	Helper function for Part II testing.
	This function calculates the sum of all the elements of A
	and b and returns the magnitude of their difference.

	A: A matrix in SparseMatrix format
	b: A column matrix in SparseMatrix format
	"""
	s1 = sum(A._value)
	s2 = sum(b._value)
	return abs(s1-s2)

class TestPartII(unittest.TestCase):
	"""
	Test suite for part II, when ground truth is not known.
	"""
	
	def setUp(self):
		self.tolerance = 10**-7
		import pickle
		'''
		Load the memplus matrix in SparseMatrix format from 
		the file "memplus_sparse.bin" as generated and verified
		by the bin_generator.

		Also create the column matrix with rowRank = rowRank of A
		and with all of its entries as 1.0
		'''
		f = open("memplus_sparse.bin", "rb")
		self.A_sparse = pickle.load(f)
		f.close()
		self.x_full = FullMatrix(self.A_sparse.rowRank, 1)
		for i in range (self.x_full.rowRank):
			self.x_full.addElement(i,0,1.0)

	
	from memory_profiler import profile
	mem = open("memory_partII.txt","w+")
	@profile(stream = mem)
	def test_combined(self):
		# import time
		# start = time.time()
		self.A_sparse.rowPermute(0,2)
		self.A_sparse.rowPermute(0,4)
		self.A_sparse.rowPermute(9,2999)
		self.A_sparse.rowPermute(4999,9999)
		self.A_sparse.rowPermute(5,14999)
		self.A_sparse.rowScale(1,3,3.0)
		self.A_sparse.rowPermute(1,4)
		self.A_sparse.rowScale(4,3,-3.0)
		b = self.A_sparse.productAx(self.x_full)
		# end = time.time()
		# runtime = open("runtime_partII.txt","w+")
		# runtime.write("Total runtime for matrix operations in part II: %.4f seconds\n" % (end-start))
		# runtime.close()
		self.assertTrue(helper_partII(self.A_sparse,b) < self.tolerance)



if __name__ == '__main__':

	unittest.main()



