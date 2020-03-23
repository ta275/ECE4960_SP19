"""
ECE 4960 SPRING 2019
Programming Assignment 3
Binary File Generation
Author: Tejas Advait (TA275)
"""

"""
This script generates binary files from outputPMOS.txt and outputNMOS.txt
The binary files contain a numpy array representation of the measurement
data.
"""
import numpy as np

file1 = open("Measurement Files/outputPMOS.txt", "r")
line = file1.readline()
line = file1.readline()

outputPMOS = []
while line != "":
	l = line.split()
	row = [np.float64(l[0]), np.float64(l[1]), np.float64(l[2])]
	row = np.array(row,dtype = np.float64)
	outputPMOS.append(row)
	line = file1.readline()
file1.close()
outputPMOS = np.array(outputPMOS, dtype = np.float64)
outputPMOS.dump("Measurement Files/outputPMOS.bin")


#########################################################################################

file2 = open("Measurement Files/outputNMOS.txt", "r")
line = file2.readline()
line = file2.readline()

outputNMOS = []
while line != "":
	l = line.split()
	row = [np.float64(l[0]), np.float64(l[1]), np.float64(l[2])]
	row = np.array(row,dtype = np.float64)
	outputNMOS.append(row)
	line = file2.readline()

file2.close()

outputNMOS = np.array(outputNMOS, dtype = np.float64)
outputNMOS.dump("Measurement Files/outputNMOS.bin")

	