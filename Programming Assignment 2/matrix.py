"""
ECE 4960 SPRING 2019
Programming Assignment 2
Matrix Module
Authors: Tejas Advait (TA275)
"""

from abc import ABC, abstractmethod
import numpy as np
from numpy import ndarray, zeros, matmul, insert

class AbstractMatrix(ABC):
	"""
	An abstract class for a matrix and corresponding methods.
	This acts like an interface for multiple implementations of a matrix.

	Important Note: Row and column indexing follow the convention of
	starting from 0 like Python lists or C/C++ arrays.
	"""


	def __init__(self, rowRank, colRank):
		"""
		Concrete method for initializing the number of rows and columns
		of the matrix.

		rowRank: number of rows [int]
		colRank: number of columns [int]
		"""

		self.rowRank = rowRank
		self.colRank = colRank
		self.rank = min(rowRank,colRank)
		self.dim = (rowRank,colRank)
		self.augmented = False
		super().__init__()

	def __str__(self):
		"""
		Concrete method for providing a way of printing the matrix
		to console. This is useful for debugging with matrix of small
		dimensions.
		"""
		row_format = ("{:>4} |")*self.colRank
		out = ""
		for i in range(self.rowRank):
			row = []
			for j in range(self.colRank):
				row.append(self.retrieveElement(i,j))
			out += (row_format.format(*row) + "\n")
		return out


	@abstractmethod
	def addElement(self, rowInd, colInd, value):
		"""
		Abstract method for adding an element to the matrix.

		rowInd: Row index of the element to be added [int]
		colInd: Column index of the element to be added [int]
		value: Value of the element to be added [float or int]

		**This abstract method must be implemented in a concrete subclass**
		"""
		pass

	@abstractmethod
	def retrieveElement(self, rowInd, colInd):
		"""
		Abstract method for retrieving an element from the matrix.

		rowInd: Row index of the element to be retrieved [int]
		colInd: Column index of the element to be retrieved [int]

		**This abstract method must be implemented in a concrete subclass**
		"""
		pass

	@abstractmethod
	def deleteElement(self, rowInd, colInd):
		"""
		Abstract method for deleting an element from the matrix.
		Deletion of an element in this context means setting
		the value of the matrix entry given by the row and column
		index to 0. 

		rowInd: Row index of the element to be deleted [int]
		colInd: Column index of the element to be deleted [int]
		
		**This abstract method must be implemented in a concrete subclass**
		"""
		pass

	@abstractmethod
	def rowPermute(self, i, j):
		"""
		Abstract method for swapping rows i and j in the matrix.

		i: Row index of the first row [int]
		j: Row index of the second row [int]

		**This abstract method must be implemented in a concrete subclass**
		"""
		pass

	@abstractmethod
	def rowScale(self, i, j, a):
		"""
		Abstract method for scaling row i with a scalar multiplier a
		and adding it to row j.

		i: Row index of the first row [int]
		j: Row index of the row which gets changed [int]
		a: Scalar multiplier [float or int]

		**This abstract method must be implemented in a concrete subclass**
		"""
		pass

	@abstractmethod
	def augment(self, x):
		"""
		Abstract method for augmenting this matrix with another matrix x.

		x: A matrix with a single column and number of rows equal to the
		number of rows of this matrix.

		Augmenting this matrix with another matrix is only allowed if this
		is a square matrix.

		**This abstract method must be implemented in a concrete subclass**
		"""
		pass

	@abstractmethod
	def deaugment(self):
		"""
		Abstract method for deaugmenting this matrix, if this matrix is
		already augmented.

		Removes the the column matrix resulting from the last column of this
		augmented matrix and returns it.

		**This abstract method must be implemented in a concrete subclass**
		"""
		pass

	@abstractmethod
	def productAx(self, x):
		"""
		Abstract method for carrying out matrix multiplication with a vector x.

		x: A matrix with a single column and number of rows equal to the
		column-rank of this matrix

		Returns: A matrix which is the result of multiplying this matrix with x

		**This abstract method must be implemented in a concrete subclass**
		"""
		pass


	@abstractmethod
	def countNZ(self):
		"""
		Abstract method for returning the count of non-zero elements present in
		the matrix.

		Returns: Number of non-zero elements in the matrix [int]

		**This abstract method must be implemented in a concrete subclass**
		"""
		pass




class FullMatrix(AbstractMatrix):
	"""
	An instance is an implementation of the AbstractMatrix class.
	This is the full matrix format implemented using the numpy module.
	"""

	

	def __init__(self,rowRank, colRank):
		"""
		Initializes a zero matrix with dimension = rowRank x colRank.

		rowRank: number of rows [int]
		colRank: number of columns [int]

		"""
		
		super().__init__(rowRank,colRank)
		
		#self._mat is the initial zero matrix
		self._mat = zeros((rowRank, colRank),dtype = np.float64)

	def __str__(self):
		return super().__str__()

	def addElement(self,rowInd, colInd, value):
		"""
		Concrete implementation of the abstract addElement method in 
		AbstractMatrix.
		"""

		self._mat[rowInd,colInd] = np.float64(value)

	def retrieveElement(self, rowInd, colInd):
		"""
		Concrete implementation of the abstract retrieveElement method in 
		AbstractMatrix.
		"""

		return self._mat[rowInd,colInd]

	def deleteElement(self,rowInd,colInd):
		"""
		Concrete implementation of the abstract deleteElement method in 
		AbstractMatrix.
		"""

		self._mat[rowInd,colInd] = 0.


	def countNZ(self):
		"""
		Concrete implementation of the abstract countNZ method in AbstractMatrix.
		"""

		count = 0
		for i in range(self.rowRank):
			for k in range (self.colRank):
				if self._mat[i,k] != 0:
					count += 1
		return count

	def augment(self, x):
		"""
		Concrete implementation of the abstract augment method in AbstractMatrix.
		"""
		if self.rowRank != self.colRank:
			raise Exception("Cannot augment a non-square-matrix.")

		if self.rowRank != x.rowRank:
			raise Exception ("Matrices incompatible.")

		if x.colRank != 1:
			raise Exception ("Cannot augment with a non-column-matrix.")

		if self.augmented:
			raise Exception ("Matrix already augmented.")
		else:
			
			self.augmented = True
			self.colRank += 1
			v = zeros((self.rowRank,1))
			for i in range (self.rowRank):
				v[i,0] = x.retrieveElement(i,0)
			self._mat = insert(self._mat, (self.rowRank,), v,axis = 1) 

	def deaugment(self):
		"""
		Concrete implementation of the abstract deaugment method in AbstactMatrix.
		"""
		
		if not self.augmented:
			raise Exception ("Matrix not augmented.")

		else:
			x = FullMatrix(self.rowRank, 1)

			for i in range (self.rowRank):
				x.addElement(i,0,self.retrieveElement(i,self.colRank - 1))

			self._mat = self._mat[:,:-1]
				
			self.colRank -= 1
			return x

	def productAx(self,x):
		"""
		Concrete implementation of the abstract productAx method in AbstractMatrix.
		"""

		if x.rowRank != self.colRank:
			raise Exception("Dimensions mismatch")

		else:
			
			ans = FullMatrix(self.rowRank,1)
			v = zeros((self.colRank, 1))
			for i in range(self.colRank):
				v[i,0] = x.retrieveElement(i,0)

			v = matmul(self._mat, v)

			for i in range(self.rowRank):
				ans.addElement(i,0,v[i,0])

			return ans

	def rowPermute(self,i,j):
		"""
		Concrete implementation of the abstract rowPermute method in 
		AbstractMatrix.
		"""
		self._mat[[i,j]] = self._mat[[j,i]]

	def rowScale(self, i, j, a):
		"""
		Concrete implementation of the abstract rowScale method in 
		AbstractMatrix.
		"""

		self._mat[j] = self._mat[i]*a + self._mat[j]




class SparseMatrix(AbstractMatrix):
	"""
	An instance is an implementation of the AbstractMatrix class.
	This is the compressed-row storage format implemented using Python lists.
	"""

	def __init__(self,rowRank, colRank):
		"""
		Initializes a zero matrix with dimension = rowRank x colRank.

		rowRank: number of rows [int]
		colRank: number of columns [int]
		"""

		super().__init__(rowRank, colRank)

		self._colInd = []
		self._rowPtr = [0 for i in range(0,rowRank+1)]
		self._value  = []

	def __str__(self):
		return super().__str__()

	def addElement(self, rowInd, colInd, value):
		"""
		Concrete implementation of the abstract addElement method in AbstractMatrix.
		"""
		if value == 0:
			pass
		else:	
			fst = self._rowPtr[rowInd]
			lst = self._rowPtr[rowInd+1]
			col = self._colInd[fst:lst]
			pos = fst
			value = np.float64(value)
			replaced = False
			for i in col:
				if i == colInd:
					self._value[pos] = value
					self._colInd[pos] = colInd
					replaced = True
				if colInd > i:
					pos+=1

			if not replaced:
				self._value.insert(pos,value)
				self._colInd.insert(pos,colInd)
				for i in range(rowInd+1, len(self._rowPtr)):
					self._rowPtr[i] += 1

	def retrieveElement(self, rowInd, colInd):
		"""
		Concrete implementation of the abstract retrieveElement method in 
		AbstractMatrix.
		"""

		fst = self._rowPtr[rowInd]
		lst = self._rowPtr[rowInd+1]
		col = self._colInd[fst:lst]
		pos = fst
		for i in col:
			if i == colInd:
				return self._value[pos]
			if colInd > i:
				pos+=1

		return 0.

	def toFullMatrix(self):
		"""
		Returns a copy of this sparse matrix in FullMatrix format.
		"""

		full = FullMatrix(self.rowRank, self.colRank)

		for i in range(self.rowRank):
			for j in range(self.colRank):
				e = self.retrieveElement(i,j)
				if e != 0:
					full.addElement(i,j,e)

		return full



	def deleteElement(self, rowInd,colInd):
		"""
		Concrete implementation of the abstract deleteElement method in 
		AbstractMatrix.
		"""
		fst = self._rowPtr[rowInd]
		lst = self._rowPtr[rowInd+1]
		col = self._colInd[fst:lst]
		suc = False
		pos = fst 
		for i in col:
			if colInd > i:
				pos+=1

			if i == colInd:
				suc = True
				del self._colInd[pos]
				del self._value[pos]
				for k in range(rowInd+1, len(self._rowPtr)):
					self._rowPtr[k] -= 1

	def countNZ(self):
		"""
		Concrete implementation of the abstract countNZ method in AbstractMatrix.
		"""
		return len(self._value)

	def rowPermute(self, i, j):
		"""
		Concrete implementation of the abstract rowPermute method in 
		AbstractMatrix.
		"""

		fsti = self._rowPtr[i]
		lsti = self._rowPtr[i+1]
		coli = self._colInd[fsti : lsti]
		vali = self._value[fsti : lsti]

		fstj = self._rowPtr[j]
		lstj = self._rowPtr[j+1]
		colj = self._colInd[fstj : lstj]
		valj = self._value[fstj : lstj]

		for t in coli:
			self.deleteElement(i,t)

		for t in colj:
			self.deleteElement(j,t)

		for t in range(len(coli)):
			self.addElement(j,coli[t],vali[t])

		for t in range(len(colj)):
			self.addElement(i,colj[t],valj[t])

	def rowScale(self, i, j, a):
		"""
		Concrete implementation of the abstract rowScale method in 
		AbstractMatrix.
		"""
		fsti = self._rowPtr[i]
		lsti = self._rowPtr[i+1]
		coli = self._colInd[fsti : lsti]


		fstj = self._rowPtr[j]
		lstj = self._rowPtr[j+1]
		colj = self._colInd[fstj : lstj]



		for t in range(len(coli)):
			ait = self.retrieveElement(i,coli[t])
			ajt = self.retrieveElement(j,coli[t])
			newajt = a*ait + ajt
			self.deleteElement(j,coli[t])
			if newajt != 0:
				self.addElement(j,coli[t],newajt)

	def productAx(self, x):
		"""
		Concrete implementation of the abstract productAx method in AbstractMatrix.
		"""

		if x.rowRank != self.colRank:
			raise Exception("Dimensions mismatch")

		ans = SparseMatrix(self.rowRank,1)


		for i in range(self.rowRank):
			s = 0
			fsti = self._rowPtr[i]
			lsti = self._rowPtr[i+1]
			coli = self._colInd[fsti : lsti]
			vali = self._value[fsti : lsti]

			for k in range(len(coli)):
				col = coli[k]
				s += vali[k]*x.retrieveElement(col,0)
			
			ans.addElement(i,0,s)

		return ans

	def augment(self,x):
		"""
		Concrete implementation of the abstract augment method in AbstractMatrix.
		"""
		if self.rowRank != self.colRank:
			raise Exception("Cannot augment a non-square-matrix.")

		if self.rowRank != x.rowRank:
			raise Exception ("Matrices incompatible.")

		if x.colRank != 1:
			raise Exception ("Cannot augment with a non-column-matrix.")

		if self.augmented:
			raise Exception ("Matrix already augmented.")
		
		else:
			self.augmented = True
			self.colRank += 1
			for i in range (self.rowRank):
				self.addElement(i, self.colRank - 1, x.retrieveElement(i,0))


	def deaugment(self):
		"""
		Concrete implementation of the abstract deaugment method in AbstactMatrix.
		"""

		if not self.augmented:
			raise Exception ("Matrix not augmented.")

		else:

			x = SparseMatrix(self.rowRank, 1)

			for i in range (self.rowRank):
				x.addElement(i,0,self.retrieveElement(i,self.colRank - 1))
				self.deleteElement(i,self.colRank - 1)

			self.colRank -= 1
			return x
