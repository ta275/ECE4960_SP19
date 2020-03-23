"""
ECE 4960 SPRING 2019
Programming Assignment 5
Direct Full-Matrix Solver

Authors: Tejas Advait (TA275)

The direct full-matrix solver returns the solution of the system by calculating the matrix
inverse using Cramer's rule for a general matrix of rank n.
"""

from matrix import FullMatrix
import numpy as np
import math
import copy



class Direct_Full_Solver:
	"""
	An instance is a representation of the linear system to be solved directly
	in the full-matrix format.
	"""

	def __init__(self,A,b):
		"""
		Initializes the matrix A, and column matrix b.
		"""

		assert(A.colRank == A.rowRank)
		self.A = copy.deepcopy(A)
		self.b = copy.deepcopy(b)
		self.A_inv = FullMatrix(A.rowRank, A.colRank)
		self.x = FullMatrix(A.rowRank,1)

		self.Anp = np.array(self.A.toNP(),dtype = np.float64)

		self.det = np.linalg.det(self.Anp)

	def minor(self,rowInd,colInd):
		"""
		Calculates the minor of the matrix at rowInd and colInd.
		"""
		assert(self.A.rowRank == self.A.colRank)
		sub = np.delete(np.delete(self.A._mat,rowInd, axis = 0),colInd, axis = 1)
		return np.linalg.det(sub)

	def cofactor(self,rowInd,colInd):
		"""
		Calculates the cofactor of the matrix at rowInd and colInd.
		"""
		assert(self.A.rowRank == self.A.colRank)
		return ((-1)**(rowInd + colInd))*self.minor(rowInd,colInd)

	def invertA(self):
		"""
		Inverts the matrix A.
		"""
		inv = np.linalg.inv(self.Anp)
		assert(self.A.rowRank == self.A.colRank)
		for i in range (self.A.rowRank):
			for j in range (self.A.colRank):
				self.A_inv.addElement(i,j,inv[i,j])

	def solve(self):

		self.invertA()
		self.x = self.A_inv.productAx(self.b)