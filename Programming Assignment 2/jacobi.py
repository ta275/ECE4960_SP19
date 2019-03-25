"""
ECE 4960 SPRING 2019
Programming Assignment 2
Jacobi Iterative Solver

Authors: Tejas Advait (TA275)
"""

from matrix import FullMatrix, SparseMatrix
import numpy as np
import math
import copy

class Jacobi_Solver:
	"""
	An instance is a representation of the linear system to be solved
	using the Jacobi iterative method.
	"""


	def __init__(self, A, b, x0 = 0, tol = 10**-9, max_iter = 10**100):
		"""
		Initializes the matrix A, column matrix b, initial guess x0, tolerance,
		and maximum number of iterations max_iter.

		D_inv is the inverse of the diagonal matrix D obtained from the diagonal elements of A.
		R is the matrix obtained from (A - D) which is equivalent to (L+U)

		Db is the product obtained from the matrix multiplication of D_inv and b.

		"""
		self.A = copy.deepcopy(A)

		self.b = b

		self.n = A.colRank

		if x0 == 0:
			self.x0 = FullMatrix(self.n,1)
		else:
			self.x0 = x0

		self.tol = tol
		self.max_iter = max_iter
		
		self.D_inv = SparseMatrix(self.n,self.n)

		self.R = copy.deepcopy(A)
		
		for i in range (self.n):
			aii = A.retrieveElement(i,i)
			self.D_inv.addElement(i, i, 1/aii)
			self.R.deleteElement(i, i)

		self.Db = self.D_inv.productAx(self.b)

		self.x = False

	def one_iter(self):
		"""
		One iteration of the Jacobi method.
		"""
		a = self.D_inv.productAx(self.R.productAx(self.x0))
		x = FullMatrix(self.n, 1)
		for i in range (self.n):
			t = -1*a.retrieveElement(i,0) + self.Db.retrieveElement(i,0)
			x.addElement(i, 0, t)

		return x

	def norm2(self,mat1,mat2):
		"""
		Calculates the second norm of [mat1 - mat2].

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

	def residual_norm(self):
		"""
		Calculates the normalized residual norm using self.x, self.A, and self.b.
		This must be called once the method solve has been called.
		"""
		b_calc = self.A.productAx(self.x)
		numerator = self.norm2(self.b,b_calc)
		denominator = 0
		for i in range(self.b.rowRank):
			denominator += (self.b.retrieveElement(i,0))**2
		denominator = math.sqrt(denominator)
		return numerator/denominator

	def solve(self):
		"""
		Solves the sytem of lienar equations using Jacobi iterative method without
		implementing any matrix preconditioning.
		"""
		num_iter = 1
		while num_iter <= self.max_iter:
			x = self.one_iter()
			if self.norm2(x,self.x0) < self.tol:
				self.x = x
				break

			num_iter += 1
			self.x0 = x

		self.x = x
		self.max_iter = num_iter
