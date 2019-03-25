"""
ECE 4960 SPRING 2019
Programming Assignment 2
Helper Functions for Testing
Author: Tejas Advait (TA275)
"""
import math
import numpy as np
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

def norm2np(mat1,npmat):
	"""
	Calculates the second norm for comparing mat1 and npmat.

	mat1: A matrix in either full or sparse format
	mat2: A matrix in numpy ndarray format

	Returns: Frobenius second norm of the matrix (mat1 - npmat)
	"""
	result = 0
	for i in range (mat1.rowRank):
		for k in range (mat1.colRank):
			a1 = mat1.retrieveElement(i,k)
			a2 = npmat[i,k]
			s = (a1-a2)**2
			result += s
	return math.sqrt(result)


def np2mat(inpt,mat):
	"""
	Helper function to generate a matrix of type mat (full or sparse) from a
	numpy ndarray inpt.
	"""	
	row = inpt.shape[0]
	col = inpt.shape[1]
	result = mat(row,col)
	for i in range (row):
		for k in range (col):
			if inpt[i,k] != 0:
				result.addElement(i,k,inpt[i,k])
	return result

def mat2np(inpt):
	"""
	Helper function to generate a numpy ndarray from a matrix (full or sparse)
	inpt.
	"""
	result = np.zeros((inpt.rowRank,inpt.colRank),dtype = np.float64)
	for i in range (inpt.rowRank):
		for k in range(inpt.colRank):
			result[i,k] = inpt.retrieveElement(i,k)
	return result

def isEqualMat(mat1, mat2):
	"""
	Helper function to check whether the matrices mat1 and mat2 are equal.
	Two matrices are equal if and only if all the corresponding elements
	are equal. This helper function is useful only to compare matrices
	containing integer elements.

	mat1: A matrix in either full or sparse format containing only integers
	mat2: A matrix in either full or sparse format containing only integers
	"""

	n = mat1.rowRank
	m = mat1.colRank
	if n != mat2.rowRank or m != mat2.colRank:
		return False

	for i in range (n):
		for j in range (m):
			a = int(mat1.retrieveElement(i,j))
			b = int(mat2.retrieveElement(i,j))
			if a != b:
				return False

	return True


def isEqualMatNp(mat1, npmat):
	"""
	Helper function to check whether the matrices mat1 and npmat are equal.
	Two matrices are equal if and only if all the corresponding elements
	are equal. This helper function is useful only to compare matrices
	containing integer elements.

	mat1: A matrix in either full or sparse format containing only integers
	npmat: A matrix in numpy ndarray format containing only integers
	"""

	n = npmat.shape[0]
	m = npmat.shape[1]
	if n != mat1.rowRank or m != mat1.colRank:
		return False

	for i in range (n):
		for j in range (m):
			a = int(mat1.retrieveElement(i,j))
			b = npmat[i,j]
			if a != b:
				return False
				
	return True

def isEqualSparse(mat1,spmat):
	"""
	Helper function to check whether the matrices mat1 and spmat are equal.
	Two matrices are equal if and only if all the corresponding elements
	are equal. This helper function is useful only to compare sparse matrices.

	mat1: A matrix in SparseMatrix format
	spmat: A matrix in scipy csr format
	"""
	spmat.eliminate_zeros()
	r1 = spmat.indptr
	r2 = np.array(mat1._rowPtr)

	v1 = spmat.data
	v2 = np.array(mat1._value)
	
	c1 = spmat.indices
	c2 = np.array(mat1._colInd)
	
	return (np.array_equal(v1,v2) and np.array_equal(c1,c2) and np.array_equal(r1,r2))




# def productHelper(A,b):
# 	"""
# 	Helper function for testing of productAx.
# 	This function calculates the sum of all the elements of A
# 	and b and returns the magnitude of their difference.

# 	A: A matrix in SparseMatrix format
# 	b: A column matrix in SparseMatrix format
# 	"""
# 	s1 = sum(A._value)
# 	s2 = sum(b._value)
# 	return abs(s1-s2)