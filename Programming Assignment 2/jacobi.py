"""
ECE 4960 SPRING 2019
Programming Assignment 2

Authors: Tejas Advait (TA275)
"""

from matrix import FullMatrix, SparseMatrix
import pickle
import numpy as np
import math
import copy

class Jacobi_Solver:

	def __init__(self, A, b, x0 = 0, tol = 10**-9, max_iter = -1):
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

		self.R = A
		
		for i in range (self.n):
			aii = A.retrieveElement(i,i)
			self.D_inv.addElement(i, i, 1/aii)
			self.R.deleteElement(i, i)

		self.Db = self.D_inv.productAx(self.b)

		self.x = False

	def one_iter(self):
		a = self.D_inv.productAx(self.R.productAx(self.x0))
		x = FullMatrix(self.n, 1)
		for i in range (self.n):
			t = -1*a.retrieveElement(i,0) + self.Db.retrieveElement(i,0)
			x.addElement(i, 0, t)

		return x


	def one_itera(self):

		x = FullMatrix(self.n,1)
		for i in range (0,self.n):
			xi = self.b.retrieveElement(i,0)
			for j in range(0,self.n):
				if j != i:
					xi += -1 * self.A.retrieveElement(i,j) * self.x0.retrieveElement(j,0)

			xi = xi / self.A.retrieveElement(i,i)
			x.addElement(i,0,xi)

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

	def solve(self):

		num_iter = 1
		if self.max_iter != -1:
			while num_iter <= self.max_iter:
				x = self.one_itera()
				if self.norm2(x,self.x0) < self.tol:
					self.x = x
					break

				num_iter += 1
				self.x0 = x

			self.x = x

		else:
			while True:
				x = self.one_iter()
				if self.norm2(x,self.x0) < self.tol:
					self.x = x
					self.max_iter = num_iter
					break
				num_iter += 1
				self.x0 = x



# A = SparseMatrix(2,2)
# A.addElement(0,0, 1)
# A.addElement(0,1, 0.1)
# A.addElement(1,0, 0.1)
# A.addElement(1,1, 1)
# b = FullMatrix(2,1)
# b.addElement(0,0,1.1)
# b.addElement(1,0,1.1)
# print ("start")
# prob1 = Jacobi_Solver(A,b)
# prob1.solve()
# print(prob1.x)
# print("done")

# mat1 = SparseMatrix(5,5)
# mat1.addElement(0,0,1)
# mat1.addElement(0,1,2)
# mat1.addElement(0,4,3)
# mat1.addElement(1,0,4)
# mat1.addElement(1,1,5)
# mat1.addElement(1,2,6)
# mat1.addElement(2,1,7)
# mat1.addElement(2,2,8)
# mat1.addElement(2,4,9)
# mat1.addElement(3,3,10)
# mat1.addElement(4,0,11)
# mat1.addElement(4,4,12)

# b = FullMatrix(5,1)
# b.addElement(0,0,5)
# b.addElement(1,0,4)
# b.addElement(2,0,3)
# b.addElement(3,0,2)
# b.addElement(4,0,1)
# print ("start")
# prob1 = Jacobi_Solver(mat1,b,max_iter = 100)
# prob1.solve()
# print(prob1.x)
# print("done")






