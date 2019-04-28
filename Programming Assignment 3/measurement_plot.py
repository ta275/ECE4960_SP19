"""
ECE 4960 SPRING 2019
Programming Assignment 3
Measurement Data Plots
Author: Tejas Advait (TA275)
"""

import pickle
import numpy as np
import matplotlib.pyplot as plt

file1 = open("Measurement Files/outputPMOS.bin", "rb")
file2 = open("Measurement Files/outputNMOS.bin", "rb")

outputPMOS = pickle.load(file1)
outputNMOS = pickle.load(file2)

VgsP = np.unique(outputPMOS[:,0])
VgsN = np.unique(outputNMOS[:,0])

PMOS = []
NMOS = []

figP = plt.figure()
plt.title(r"$I_{D}$ vs $V_{DS}$ for PMOS")
for i in VgsP:
	sub = outputPMOS[outputPMOS[:,0] == i]
	y = sub[:,2].flatten()
	x = sub[:,1].flatten()
	plt.plot(x,y, label = r"$V_{GS}$ = " + str(i))
	PMOS.append(sub)

plt.xlabel(r"$V_{DS}$ (V)")
plt.ylabel(r"$I_{D}$ (A)")
plt.legend()
plt.show()


figN = plt.figure()
plt.title(r"$I_{D}$ vs $V_{DS}$ for NMOS")
for i in VgsN:
	sub = outputNMOS[outputNMOS[:,0] == i]
	y = sub[:,2].flatten()
	x = sub[:,1].flatten()
	plt.plot(x,y, label = r"$V_{GS}$ = " + str(i))
	NMOS.append(sub)

plt.xlabel(r"$V_{DS}$ (V)")
plt.ylabel(r"$I_{D}$ (A)")
plt.legend()
plt.show()

# figN = plt.figure()
# for i in VgsN:
# 	sub = outputNMOS[outputNMOS[:,0] == i]
# 	NMOS.append(sub)



# print (PMOS)
# # print (NMOS)