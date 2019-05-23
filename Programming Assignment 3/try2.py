import pickle
import numpy as np
file1 = open("Measurement Files/outputNMOS.bin", "rb")
outputNMOS = pickle.load(file1)
file1.close()
for i in outputNMOS:
	print ("{0}, {1}, {2}".format(i[0],i[1],i[2]))

print (outputNMOS.shape[0])