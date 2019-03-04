#HW 4 ECE 4960 SPRING 2019
#Matrix Module
#TEJAS ADVAIT (TA275)

class FullMatrix():
	def __init__(self,rowRank, colRank):
		
		self.rowRank = rowRank
		self.colRank = colRank
		
		self._colInd = []
		self._rowInd = []
		self._value  = []


	def addElement(self,rowInd, colInd, value):

		self._rowInd.append(rowInd)
		self._colInd.append(colInd)
		self._value.append(value)

	def retrieveElement(self, rowInd, colInd):
		
		for i in range(len(self._rowInd)):
			if self._rowInd[i] == rowInd and self._colInd[i] == colInd:
				return self._value[i]

		return 0

	def deleteElement(self,rowInd,colInd):
		
		for i in range(len(self._rowInd)):
			if self._rowInd[i] == rowInd and self._colInd[i] == colInd:
				del self._value[i]
				del self._rowInd[i]
				del self._colInd[i]

	def rankMatrix(self):
		
		return min(self.rowRank,self.colRank)


	def countElementMatrix(self):
		count = 0
		for i in range(self.rowRank):
			for k in range (self.colRank):
				if self.retrieveElement(i,k) != 0:
					count += 1
		return count

	def printFull(self):
		a = [[0 for i in range(self.rowRank)] for i in range(self.colRank)]

		for i in range(len(self._rowInd)):
			r = self._rowInd[i]
			c = self._colInd[i]
			v = self._value[i]
			a[r][c] = v

		for i in a:
			print (i)





class SparseMatrix():

	def __init__(self,rowRank, colRank):

		self.rowRank = rowRank
		self.colRank = colRank

		self._colInd = []
		self._rowPtr = [0 for i in range(0,rowRank+1)]
		self._value  = []

	def addElement(self, rowInd, colInd, value):
		fst = self._rowPtr[rowInd]
		lst = self._rowPtr[rowInd+1]
		col = self._colInd[fst:lst]
		pos = fst
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

		fst = self._rowPtr[rowInd]
		lst = self._rowPtr[rowInd+1]
		col = self._colInd[fst:lst]
		pos = fst
		for i in col:
			if i == colInd:
				return self._value[pos]
			if colInd > i:
				pos+=1
		

		return 0

	def toFullMatrix(self):
		full = FullMatrix(self.rowRank, self.colRank)

		for i in range(self.rowRank):
			for j in range(self.colRank):
				e = self.retrieveElement(i,j)
				if e != 0:
					full.addElement(i,j,e)

		return full

	def deleteElement(self, rowInd,colInd):
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


	def rankMatrix(self):
		return min(self.rowRank, self.colRank)

	def countElementMatrix(self):
		return len(self._value)

	def rowPermute(self, i, j):

		# fsti = self._rowPtr[i]
		# lsti = self._rowPtr[i+1]
		# coli = self._colInd[fsti : lsti]
		# vali = self._value[fsti : lsti]

		# fstj = self._rowPtr[j]
		# lstj = self._rowPtr[j+1]
		# colj = self._colInd[fstj : lstj]
		# valj = self._value[fstj : lstj]

		for t in range(self.colRank):
			ait = self.retrieveElement(i,t)
			ajt = self.retrieveElement(j,t)
			self.deleteElement(i,t)
			self.deleteElement(j,t)
			
			if ait != 0:
				self.addElement(j,t,ait)

			if ajt != 0:
				self.addElement(i,t,ajt)

		# for t in range(len(coli)):
		# 	self.addElement(j,coli[t],vali[t])

		# for t in range(len(colj)):
		# 	self.addElement(i,colj[t],valj[t])

	def rowScale(self, i, j, a):


		for t in range(self.colRank):
			ait = self.retrieveElement(i,t)
			ajt = self.retrieveElement(j,t)
			newajt = a*ait + ajt
			self.deleteElement(j,t)
			
			if newajt != 0:
				self.addElement(j,t,newajt)

	def productAx(self, x):
		
		b = SparseMatrix(self.rowRank,0)

		for i in range (self.rowRank):
			p = 0
			for j in range(self.colRank):
				a = self.retrieveElement(i,j)
				e = x.retrieveElement(j,0)
				p += (a.e)

			b.addElement(i,0,p)

		return b






mat1 = SparseMatrix(5,5)

mat1.addElement(3,3,10)
mat1.addElement(4,0,11)
mat1.addElement(4,4,12)
mat1.addElement(0,0,1)
mat1.addElement(0,1,2)
mat1.addElement(0,4,3)
mat1.addElement(1,0,4)
mat1.addElement(1,1,5)
mat1.addElement(1,2,6)
mat1.addElement(2,1,7)
mat1.addElement(2,2,8)
mat1.addElement(2,4,9)

#mat1.deleteElement(0,0)
#mat1.deleteElement(2,1)
#mat1.deleteElement(0,2)
