#Binary File Generator for memplus.mtx
from matrix import FullMatrix, SparseMatrix
import pickle

file = open("memplus.mtx","r")
line = file.readline()
line = file.readline()
line = line.split()
rowRank = int(line[0])
colRank = int(line[1])
A_sparse = SparseMatrix(rowRank,colRank)

s = 1
while True:
	if s%1000 == 0:
		print ("Added " + str(s) + " elements")
	line = file.readline()
	line = line.split()

	if len(line) == 3:
		row_coord = int(line[0]) - 1
		col_coord = int(line[1]) - 1
		value = float(line[2].strip("\n"))
		A_sparse.addElement(row_coord,col_coord,value)
	else:
		file.close()
		break
	s+= 1

file = open("memplus_sparse.bin","wb")
pickle.dump(A_sparse, file)
file.close()

#Verification

file = open("memplus_sparse.bin", "rb")

A = pickle.load(file)
file.close()

assert(len(A._value) == 99147)
assert(len(A._colInd) == 99147)
assert(len(A._rowPtr) == 17759)

