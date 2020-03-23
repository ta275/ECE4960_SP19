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
from helper_test import *
from matrix import FullMatrix, SparseMatrix

tolerance = 10**-9

class FullMatrixTest(unittest.TestCase):
	"""
	Test suite for FullMatrix format.
	"""
	def setUp(self):
		self.matrix0 = np.random.rand(1,1)
		self.fmatrix0 = np2mat(self.matrix0,FullMatrix)
		
		self.matrix1 = np.random.rand(100,100)
		self.fmatrix1 = np2mat(self.matrix1,FullMatrix)
		
		self.matrix2 = np.random.rand(10,10)
		self.fmatrix2 = np2mat(self.matrix2,FullMatrix)

		self.matrix3 = np.random.randint(low = 50, size = (10,10))		
		self.fmatrix3 = np2mat(self.matrix3,FullMatrix)

		self.x0 = np.zeros((1,1))
		self.fx0 = np2mat(self.x0,FullMatrix)

		self.x1 = np.zeros((100,1))
		self.fx1 = np2mat(self.x1,FullMatrix)

		self.x2 = np.zeros((10,1))
		self.fx2 = np2mat(self.x2,FullMatrix)

		self.x3 = np.ones((100,1))
		self.fx3 = np2mat(self.x3,FullMatrix)

		self.x4 = np.ones((10,1))
		self.fx4 = np2mat(self.x4,FullMatrix)

		self.x5 = np.ones((1,1))
		self.fx5 = np2mat(self.x5,FullMatrix)

	def test_row_n_col_Rank(self):
		self.assertTrue(self.fmatrix0.rowRank == 1)
		self.assertTrue(self.fmatrix1.rowRank == 100)
		self.assertTrue(self.fmatrix2.rowRank == 10)
		self.assertTrue(self.fmatrix3.rowRank == 10)
		self.assertTrue(self.fmatrix0.colRank == 1)
		self.assertTrue(self.fmatrix1.colRank == 100)
		self.assertTrue(self.fmatrix2.colRank == 10)
		self.assertTrue(self.fmatrix3.colRank == 10)

	def test_countNZ(self):
		self.assertTrue(self.fmatrix0.countNZ() == np.count_nonzero(self.matrix0))
		self.assertTrue(self.fmatrix1.countNZ() == np.count_nonzero(self.matrix1))
		self.assertTrue(self.fmatrix2.countNZ() == np.count_nonzero(self.matrix2))
		self.assertTrue(self.fmatrix3.countNZ() == np.count_nonzero(self.matrix3))

	def test_add_n_retrieve(self):
		self.assertTrue(norm2np(self.fmatrix0,self.matrix0) == 0)
		self.assertTrue(norm2np(self.fmatrix1,self.matrix1) == 0)
		self.assertTrue(norm2np(self.fmatrix2,self.matrix2) == 0)
		self.assertTrue(isEqualMatNp(self.fmatrix3,self.matrix3))
	
	def test_deleteElement0(self):
		self.fmatrix0.deleteElement(0,0)
		self.matrix0[0,0] = 0
		self.assertTrue(isEqualMatNp(self.fmatrix0,self.matrix0))

	def test_deleteElement1a(self):
		self.fmatrix1.deleteElement(0,8)
		self.fmatrix1.deleteElement(34,12)
		self.fmatrix1.deleteElement(23,23)
		self.fmatrix1.deleteElement(0,0)
		self.fmatrix1.deleteElement(99,99)
		self.fmatrix1.deleteElement(2,99)
		self.fmatrix1.deleteElement(99,12)
		self.fmatrix1.deleteElement(0,99)
		self.fmatrix1.deleteElement(0,54)
		self.matrix1[0,8] = self.matrix1[34,12] = self.matrix1[23,23] = 0
		self.matrix1[0,0] = self.matrix1[99,99] = self.matrix1[2,99] = 0
		self.matrix1[99,12] = self.matrix1[0,99] = self.matrix1[0,54] = 0
		self.assertTrue(norm2np(self.fmatrix1,self.matrix1) == 0)

	def test_deleteElement1b(self):
		for i in range (self.fmatrix1.rowRank):
			for j in range(self.fmatrix1.colRank):
				self.fmatrix1.deleteElement(i,j)

		self.assertTrue(isEqualMatNp(self.fmatrix1,np.zeros((100,100))))

	def test_deleteElement2(self):
		self.fmatrix2.deleteElement(3,8)
		self.fmatrix2.deleteElement(4,4)
		self.fmatrix2.deleteElement(0,0)
		self.matrix2[3,8] = self.matrix2[4,4] = self.matrix2[0,0] = 0
		self.assertTrue(norm2np(self.fmatrix2,self.matrix2) == 0)

	def test_deleteElement3(self):
		self.fmatrix3.deleteElement(9,9)
		self.fmatrix3.deleteElement(1,1)
		self.fmatrix3.deleteElement(0,0)
		self.fmatrix3.deleteElement(1,8)
		self.fmatrix3.deleteElement(5,1)
		self.fmatrix3.deleteElement(3,9)

		self.matrix3[9,9] = self.matrix3[1,1] = self.matrix3[0,0] = 0
		self.matrix3[1,8] = self.matrix3[5,1] = self.matrix3[3,9] = 0
		self.assertTrue(isEqualMatNp(self.fmatrix3,self.matrix3))

	def test_rowScale1(self):
		self.fmatrix1.rowScale(23,12,8)
		self.fmatrix1.rowScale(92,1,9)
		self.fmatrix1.rowScale(12,8,2.2)
		self.fmatrix1.rowScale(0,99,1.3)
		self.fmatrix1.rowScale(99,12,2.2)

		self.matrix1[12] = self.matrix1[23]*8 + self.matrix1[12]
		self.matrix1[1] = self.matrix1[92]*9 + self.matrix1[1]
		self.matrix1[8] = self.matrix1[12]*2.2 + self.matrix1[8]
		self.matrix1[99] = self.matrix1[0]*1.3 + self.matrix1[99]
		self.matrix1[12] = self.matrix1[99]*2.2 + self.matrix1[12]

		self.assertTrue(norm2np(self.fmatrix1,self.matrix1) == 0)

	def test_rowScale3(self):
		self.fmatrix3.rowScale(8,0,22)
		self.fmatrix3.rowScale(0,1,-1)
		self.fmatrix3.rowScale(1,9,4)
		self.fmatrix3.rowScale(2,6,1)
		self.fmatrix3.rowScale(6,2,-1)

		self.matrix3[0] = self.matrix3[8]*22 + self.matrix3[0]
		self.matrix3[1] = self.matrix3[0]*-1 + self.matrix3[1]
		self.matrix3[9] = self.matrix3[1]*4 + self.matrix3[9]
		self.matrix3[6] = self.matrix3[2]*1 + self.matrix3[6]
		self.matrix3[2] = self.matrix3[6]*-1 + self.matrix3[2]
		self.assertTrue(isEqualMatNp(self.fmatrix3,self.matrix3))

	def test_rowPermute1(self):
		self.fmatrix1.rowPermute(23,12)
		self.fmatrix1.rowPermute(92,1)
		self.fmatrix1.rowPermute(12,8)
		self.fmatrix1.rowPermute(0,99)
		self.fmatrix1.rowPermute(99,12)

		self.matrix1[[23,12]] = self.matrix1[[12,23]]
		self.matrix1[[92,1]] = self.matrix1[[1,92]]
		self.matrix1[[12,8]] = self.matrix1[[8,12]]
		self.matrix1[[0,99]] = self.matrix1[[99,0]]
		self.matrix1[[99,12]] = self.matrix1[[12,99]]

		self.assertTrue(norm2np(self.fmatrix1,self.matrix1) == 0)

	def test_rowPermute3(self):
		self.fmatrix3.rowPermute(8,0)
		self.fmatrix3.rowPermute(0,1)
		self.fmatrix3.rowPermute(1,9)
		self.fmatrix3.rowPermute(2,6)
		self.fmatrix3.rowPermute(6,2)

		self.matrix3[[8,0]] = self.matrix3[[0,8]]
		self.matrix3[[0,1]] = self.matrix3[[1,0]]
		self.matrix3[[1,9]] = self.matrix3[[9,1]]
		self.matrix3[[2,6]] = self.matrix3[[6,2]]
		self.matrix3[[6,2]] = self.matrix3[[2,6]]

		self.assertTrue(isEqualMatNp(self.fmatrix3,self.matrix3))

	def test_productAx0(self):
		b1 = self.fmatrix0.productAx(self.fx0)
		b2 = self.fmatrix0.productAx(self.fx5)
		self.assertTrue(isEqualMatNp(b1,np.zeros((1,1))))
		self.assertTrue(b2.retrieveElement(0,0) == self.matrix0[0,0])

	def test_productAx1a(self):
		b1 = self.fmatrix1.productAx(self.fx1)
		b2 = self.fmatrix1.productAx(self.fx3)
		
		b2np = np.matmul(self.matrix1,self.x3)

		self.assertTrue(isEqualMatNp(b1,np.zeros((100,1))))
		self.assertTrue(norm2np(b2,b2np) < tolerance)

	def test_productAx1b(self):
		x = np.random.rand(100,1)
		fx = np2mat(x,FullMatrix)
		b = self.fmatrix1.productAx(fx)
		bnp = np.matmul(self.matrix1,x)
		self.assertTrue(norm2np(b,bnp) < tolerance)

	def test_productAx3(self):
		x = np.random.randint(low = 50, size = (10,1))
		fx = np2mat(x,FullMatrix)
		b = self.fmatrix3.productAx(fx)
		bnp = np.matmul(self.matrix3,x)
		self.assertTrue(isEqualMatNp(b,bnp))

class SparseMatrixTest(unittest.TestCase):
	"""
	Test suite for SparseMatrix format.
	"""
	def setUp(self):
		
		self.matrix1 = sparse.random(100,100,density=0.01,format="csr",dtype= np.float64)
		self.smatrix1 = np2mat(self.matrix1,SparseMatrix)
		
		self.x1 = np.zeros((100,1))
		self.fx1 = np2mat(self.x1,FullMatrix)
		self.x2 = np.ones((100,1))
		self.fx2 = np2mat(self.x2,FullMatrix)

	def test_row_n_col_Rank(self):
		self.assertTrue(self.smatrix1.rowRank == 100)
		self.assertTrue(self.smatrix1.colRank == 100)


	def test_countNZ(self):
		self.assertTrue(self.smatrix1.countNZ() == self.matrix1.count_nonzero())

	def test_add_n_retrieve(self):
		self.assertTrue(norm2np(self.smatrix1,self.matrix1) == 0)


	def test_deleteElement1a(self):
		self.smatrix1.deleteElement(0,8)
		self.smatrix1.deleteElement(34,12)
		self.smatrix1.deleteElement(23,23)
		self.smatrix1.deleteElement(0,0)
		self.smatrix1.deleteElement(99,99)
		self.smatrix1.deleteElement(2,99)
		self.smatrix1.deleteElement(99,12)
		self.smatrix1.deleteElement(0,99)
		self.smatrix1.deleteElement(0,54)
		self.matrix1[0,8] = self.matrix1[34,12] = self.matrix1[23,23] = 0
		self.matrix1[0,0] = self.matrix1[99,99] = self.matrix1[2,99] = 0
		self.matrix1[99,12] = self.matrix1[0,99] = self.matrix1[0,54] = 0
		self.assertTrue(norm2np(self.smatrix1,self.matrix1) == 0)
		
		self.assertTrue(isEqualSparse(self.smatrix1,self.matrix1))

	def test_deleteElement1b(self):
		for i in range (self.smatrix1.rowRank):
			for j in range(self.smatrix1.colRank):
				self.smatrix1.deleteElement(i,j)

		self.assertTrue(isEqualMatNp(self.smatrix1,np.zeros((100,100))))

	def test_rowScale1(self):
		self.smatrix1.rowScale(23,12,8)
		self.smatrix1.rowScale(92,1,9)
		self.smatrix1.rowScale(12,8,2.2)
		self.smatrix1.rowScale(0,99,1.3)
		self.smatrix1.rowScale(99,12,2.2)

		self.matrix1[12] = self.matrix1[23]*8 + self.matrix1[12]
		self.matrix1[1] = self.matrix1[92]*9 + self.matrix1[1]
		self.matrix1[8] = self.matrix1[12]*2.2 + self.matrix1[8]
		self.matrix1[99] = self.matrix1[0]*1.3 + self.matrix1[99]
		self.matrix1[12] = self.matrix1[99]*2.2 + self.matrix1[12]


		self.assertTrue(norm2np(self.smatrix1,self.matrix1) == 0)
	
		self.assertTrue(isEqualSparse(self.smatrix1,self.matrix1))

	def test_rowPermute1(self):
		self.smatrix1.rowPermute(23,12)
		self.smatrix1.rowPermute(92,1)
		self.smatrix1.rowPermute(12,8)
		self.smatrix1.rowPermute(0,99)
		self.smatrix1.rowPermute(99,12)

		self.matrix1[[23,12]] = self.matrix1[[12,23]]
		self.matrix1[[92,1]] = self.matrix1[[1,92]]
		self.matrix1[[12,8]] = self.matrix1[[8,12]]
		self.matrix1[[0,99]] = self.matrix1[[99,0]]
		self.matrix1[[99,12]] = self.matrix1[[12,99]]

		self.assertTrue(norm2np(self.smatrix1,self.matrix1) == 0)

		self.assertTrue(isEqualSparse(self.smatrix1,self.matrix1))
		

	def test_productAx1a(self):
		b1 = self.smatrix1.productAx(self.fx1)
		b2 = self.smatrix1.productAx(self.fx2)
		
		b2np = np.matmul(self.matrix1.toarray(),self.x2)

		self.assertTrue(isEqualMatNp(b1,np.zeros((100,1))))
		self.assertTrue(norm2np(b2,b2np) < tolerance)

	def test_productAx1b(self):
		x = np.random.rand(100,1)
		fx = np2mat(x,FullMatrix)
		b = self.smatrix1.productAx(fx)
		bnp = np.matmul(self.matrix1.toarray(),x)
		self.assertTrue(norm2np(b,bnp) < tolerance)


class WilkinsonTestPartI(unittest.TestCase):
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

		self.A_full.augment(self.x_full)
		self.A_sparse.augment(self.x_full)

	def test_rowPermute(self):
		self.A_full.rowPermute(0,2)
		self.A_full.rowPermute(0,4)
		self.A_sparse.rowPermute(0,2)
		self.A_sparse.rowPermute(0,4)

		self.assertTrue(norm2(self.A_full, self.A_sparse) == 0.0)

	def test_rowScale(self):
		self.A_full.rowScale(0,3,3)
		self.A_full.rowScale(4,1,-4.4)
		self.A_sparse.rowScale(0,3,3)
		self.A_sparse.rowScale(4,1,-4.4)
		self.assertTrue(norm2(self.A_full, self.A_sparse) == 0.0)


	def test_productAx(self):
		x = self.A_full.deaugment()
		self.A_sparse.deaugment()
		full = self.A_full.productAx(x)
		sparse = self.A_sparse.productAx(x)
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

		x = self.A_sparse.deaugment()
		self.A_full.deaugment()

		full = self.A_full.productAx(x)
		sparse = self.A_sparse.productAx(x)
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

class WilkinsonTestPartII(unittest.TestCase):
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
		f = open("memplus/memplus_sparse.bin", "rb")
		self.A_sparse = pickle.load(f)
		f.close()
		self.x_full = FullMatrix(self.A_sparse.rowRank, 1)
		for i in range (self.x_full.rowRank):
			self.x_full.addElement(i,0,1.0)

	def test_combined(self):
		self.A_sparse.rowPermute(0,2)
		self.A_sparse.rowPermute(0,4)
		self.A_sparse.rowPermute(9,2999)
		self.A_sparse.rowPermute(4999,9999)
		self.A_sparse.rowPermute(5,14999)
		self.A_sparse.rowScale(1,3,3.0)
		self.A_sparse.rowPermute(1,4)
		self.A_sparse.rowScale(4,3,-3.0)
		b = self.A_sparse.productAx(self.x_full)
		self.assertTrue(helper_partII(self.A_sparse,b) < self.tolerance)


if __name__ == '__main__':

	unittest.main()



