"""
ECE 4960 SPRING 2019
Programming Assignment 3
EKV Model Parameter Extraction - Task 6
Author: Tejas Advait (TA275)
"""

import numpy as np
from opes import OPES
from s_model import S_model
import pickle

IS = [1e-8, 3e-8, 1e-7, 3e-7, 1e-6, 3e-6, 1e-5, 3e-5]
KAP = [0.5,0.6,0.7,0.8,0.9]
VTH = [0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]

#Load the measured data

file1 = open("Measurement Files/outputNMOS.bin", "rb")
outputNMOS = pickle.load(file1)
file1.close()

###################################################################################################
#Task 6

def Id_ekv(x,a):
	Is = a[0]
	kap = a[1]
	Vth = a[2]
	Vgs = x[0]
	Vds = x[1]
	Vt = np.float64(26*10-3)
	Id = Is*(np.log(1 + np.exp((kap*(Vgs-Vth))/(2*Vt))))**2 \
	- Is*(np.log(1 + np.exp((kap*(Vgs-Vth) - Vds)/(2*Vt))))**2
	return Id


V = 1e4
Is_opt = 0
kap_opt = 0
Vth_opt = 0
extracted_p = 0
data = []
import pickle

for Is in IS:
	for kap in KAP:
		for Vth in VTH:
			#Initial Parameter Guess
			p_est = np.array([Is,kap,Vth],dtype = np.float64)
			print (p_est)

			#Tolerance and Step Size for optimization loop
			tol = np.float64(10**-7)
			step = np.float64(10**-5)

			#Set-up of the EKV model with 2 independent variables and 3 parameters
			num_indep = 2
			num_param = 3
			EKV_model = S_model(num_indep,num_param,Id_ekv,p_est)


			#Set-up of the optimal parameter extraction problem with the measured data
			OptNMOS = OPES(EKV_model,outputNMOS,p_est,tol,step)


			#Extract the parameters
			extracted_p_nmos = OptNMOS.extractParam()

			if extracted_p_nmos.size != 0:
				
				v = OptNMOS.objective(extracted_p_nmos)
				if v < V:
					V = v
					Is_opt = Is
					kap_opt = kap
					Vth_opt = Vth
					extracted_p = extracted_p_nmos

print ("Smallest ||V|| achieved by the initial guesses of Is = {0}, kap = {1}, Vth = {2}".format(Is_opt,kap_opt,Vth_opt))
print ("Smallest ||V|| is {0}".format(V))
print ("Extracted parameters are: Is = {0}, kap = {1}, Vth = {2}".format(extracted_p[0],extracted_p[1],extracted_p[2]))