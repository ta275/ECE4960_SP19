"""
HW 4 ECE 4960 SPRING 2019
Sparse Matrix Generator
Authors: Tejas Advait (TA275)

Functionality: This small script generates and validated a SparseMatrix from a 
.mtx file and stores it in a binary file which can be loaded in test.py.
This is helpful as generating the SparseMatrix of huge sizes takes a lot of time.
Thus, it saves time to generate them once and store it for use in other programs.
This avoids generating the sparse matrix again and again when doing regression
testing.
"""

from matrix import FullMatrix, SparseMatrix
import pickle

file = open("memplus.mtx","r") #Opening memplus.mtx in reading mode
line = file.readline() #Reading the first line which is a comment
line = file.readline() #Reading the second line which contains rowRank, colRank, and number of entries

#Extracting rowRank and colRank
line = line.split()
rowRank = int(line[0])
colRank = int(line[1])
num_elem = int(line[2])

#Initializing a SparseMatrix
A_sparse = SparseMatrix(rowRank,colRank)

#Reading the remainder of memplus.mtx to complete the SparseMatrix

for i in range (1,num_elem+1): #Loop for reading till the end of memplus.mtx
	
	#Print for every 1000 elements added
	if i%1000 == 0:
		print ("Added %d elements." %i)

	'''
	Reading the file and extracting the row, column, and the value of
	the element.
	'''
	line = file.readline()
	line = line.split()
	row_coord = int(line[0]) - 1
	col_coord = int(line[1]) - 1
	value = float(line[2].strip("\n"))
	A_sparse.addElement(row_coord,col_coord,value)

#Finished reading the file
file.close()
print ("Added %d elements." %i)
print ("SparseMatrix generation complete.")


#Creating a binary file and dumping the SparseMatrix in it
file = open("memplus_sparse.bin","wb")
pickle.dump(A_sparse, file)
file.close()


'''
Verification of the binary file - Load the binary file and check the length
of the list containing non-zero values, row pointers, and column indices.
Additionally, one can start reading the .mtx file from the beginning again and
call the retrieveElement method to compare the value of each entry of the
stored SparseMatrix with the data in .mtx file. 
'''
file = open("memplus_sparse.bin", "rb")
A = pickle.load(file)
file.close()

assert(len(A._value) == 99147)
assert(len(A._colInd) == 99147)
assert(len(A._rowPtr) == 17759)

file = open("memplus.mtx","r") #Opening memplus.mtx in reading mode
line = file.readline() #Reading the first line which is a comment
line = file.readline() #Reading the second line which contains rowRank, colRank, and numbre of entries.

#Extracting rowRank and colRank
line = line.split()
rowRank = int(line[0])
colRank = int(line[1])
num_elem = int(line[2])


#Reading the remainder of memplus.mtx to validate the binary file

for i in range (1,num_elem+1): #Loop for reading till the end of memplus.mtx
	
	#Print for every 1000 elements validated
	if i%1000 == 0:
		print ("Validated %d elements." %i)

	'''
	Reading the file and extracting the row, column, and the value of
	the element.
	'''
	line = file.readline()
	line = line.split()
	row_coord = int(line[0]) - 1
	col_coord = int(line[1]) - 1
	value = float(line[2].strip("\n"))
	assert(A.retrieveElement(row_coord,col_coord) == value)

#Finished validating the file
file.close()
print ("Validated %d elements." %i)
print ("Binary file validation complete.")
