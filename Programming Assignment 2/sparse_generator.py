"""
ECE 4960 SPRING 2019
Programming Assignment 2
Sparse Matrix Generator
Authors: Tejas Advait (TA275)

Functionality: This program generates and validates a SparseMatrix from a
.mtx file or from three csv files containing row pointer, column indicesz and values 
and stores it in a binary file which can be loaded in other programs using the pickle
module.

This is helpful as generating the SparseMatrix of huge sizes takes a lot of time.
Thus, it saves time by generating them once and storing them for use in other programs.
This avoids generating the sparse matrix again and again when doing regression
testing.
"""

from matrix import FullMatrix, SparseMatrix
import pickle
import numpy as np

def from_mtx(file_in, file_out):
	"""
	Generates a binary file named file_out which represents the SparseMatrix
	generated from the .mtx file named file_in.
	"""
	file = open(file_in,"r") #Opening file_in in reading mode
	line = file.readline() #Reading the first line which is a comment
	line = file.readline() #Reading the second line which contains rowRank, colRank, and number of entries

	#Extracting rowRank and colRank
	line = line.split()
	rowRank = int(line[0])
	colRank = int(line[1])
	num_elem = int(line[2])

	#Initializing a SparseMatrix
	A_sparse = SparseMatrix(rowRank,colRank)

	#Reading the remainder of the file_in file to complete the SparseMatrix

	for i in range (1,num_elem+1): #Loop for reading till the end of file_in

		# Extracting the row, column, and the value of the element.
		line = file.readline()
		line = line.split()
		row_coord = int(line[0]) - 1
		col_coord = int(line[1]) - 1
		value = np.float64(line[2].strip("\n"))
		A_sparse.addElement(row_coord,col_coord,value)

	#Finished reading file_in
	file.close()


	#Creating a binary file and dumping the SparseMatrix A_sparse in it
	file = open(file_out,"wb")
	pickle.dump(A_sparse, file)
	file.close()

def from_csv_crs(rowPtr, colInd, value, file_out):
	"""
	Generates a binary file named file_out which represents the SparseMatrix
	generated from the csv files containing row pointer, column indices, and
	values in files named rowPtr, colInd, and value respectively.
	Precondition: Number of values in colInd and value is strictly greater
	than the number of values in rowPtr. Each entry in rowPtr and colInd is
	an integer and each entry in value is either a float or an integer.
	"""
	f1 = open(rowPtr,"r")
	f2 = open(colInd,"r")
	f3 = open(value, "r")
	rowP = []
	colI = []
	val = []

	while True:

		l1 = f1.readline()
		if l1 == "":
			f1.close()
			break
		
		else:
			l1 = int(l1.strip("\n")) - 1
			rowP.append(l1)

			l2 = int(f2.readline().strip("\n")) - 1
			colI.append(l2)
			l3 = np.float64(f3.readline().strip("\n"))
			val.append(l3)
	
	while True:
		l2 = f2.readline()
		if l2 == "":
			f2.close()
			f3.close()
			break
		
		else:
			l2 = int(l2.strip("\n")) - 1
			colI.append(l2)

			l3 = np.float64(f3.readline().strip("\n"))
			val.append(l3)

	A_sparse = SparseMatrix(len(rowP)-1,len(rowP)-1)
	A_sparse._rowPtr = rowP[:]
	A_sparse._colInd = colI[:]
	A_sparse._value = val[:]
	#Creating a binary file and dumping the SparseMatrix A_sparse in it
	file = open(file_out,"wb")
	pickle.dump(A_sparse, file)
	file.close()



def from_mtx_valid(file_in, file_out):
	'''
	Verification of the binary file named file_out generated from the .mtx
	file named file_in.
	'''
	file = open(file_out, "rb")
	A = pickle.load(file)
	file.close()

	file = open(file_in,"r") #Opening file_in in reading mode
	line = file.readline() #Reading the first line which is a comment
	line = file.readline() #Reading the second line which contains rowRank, colRank, and numbre of entries.

	#Extracting rowRank and colRank
	line = line.split()
	rowRank = int(line[0])
	colRank = int(line[1])
	num_elem = int(line[2])

	num_nonzero = 0

	#Reading the remainder of file_in to validate file_out

	for i in range (1,num_elem+1): #Loop for reading till the end of file_in.
		
		'''
		Reading the file and extracting the row, column, and the value of
		the element.
		'''
		line = file.readline()
		line = line.split()
		row_coord = int(line[0]) - 1
		col_coord = int(line[1]) - 1
		value = float(line[2].strip("\n"))
		if value != 0:
			num_nonzero += 1
		try:
			assert(A.retrieveElement(row_coord,col_coord) == value)
		except:
			return False

	#Finished validating file_out
	file.close()


	try:
		assert(len(A._value) == num_nonzero )
		assert(len(A._colInd) == num_nonzero)
		assert(len(A._rowPtr) == rowRank+1)
	except:
		return False

	return True

def from_csv_crs_valid(rowPtr, colInd, value, file_out):
	'''
	Verification of the binary file named file_out generated from the csv files
	named rowPtr, colInd, and value. 
	'''

	f1 = open(rowPtr,"r")
	f2 = open(colInd,"r")
	f3 = open(value, "r")

	file = open(file_out, "rb")
	A = pickle.load(file)
	file.close()

	rowPtr_len = 0
	i = 0
	while True:
		l1 = f1.readline()
		if l1 == "":
			f1.close()
			break
		
		else:
			l1 = int(l1.strip("\n")) - 1
			l2 = int(f2.readline().strip("\n")) - 1
			l3 = np.float64(f3.readline().strip("\n"))
			assert(l1 == A._rowPtr[i])
			assert(l2 == A._colInd[i])
			assert(l3 == A._value[i])
			i += 1
			rowPtr_len += 1
	
	while True:
		l2 = f2.readline()
		if l2 == "":
			f2.close()
			f3.close()
			break
		
		else:
			l2 = int(l2.strip("\n")) - 1
			l3 = np.float64(f3.readline().strip("\n"))
			assert(l2 == A._colInd[i])
			assert(l3 == A._value[i])
			i += 1
	try:
		assert(len(A._value) == i)
		assert(len(A._colInd) == i)
		assert(len(A._rowPtr) == rowPtr_len)
	except:
		return False

	return True
