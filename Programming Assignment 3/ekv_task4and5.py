"""
ECE 4960 SPRING 2019
Programming Assignment 3
EKV Model Parameter Extraction - Tasks 4 and 5
Author: Tejas Advait (TA275)
"""
import numpy as np
from opes import OPES
from s_model import S_model
import pickle

#Load the measured data

file1 = open("Measurement Files/outputNMOS.bin", "rb")
outputNMOS = pickle.load(file1)
file1.close()

###################################################################################################
#Task 4

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



#Initial guesses
Is = 10**-7
kap = 1
Vth = 1
#Initial Parameter Guess
p_est = np.array([Is,kap,Vth],dtype = np.float64)

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
if extracted_p_nmos.size == 0:
	Is = "Failed"
	kap = "Failed"
	Vth = "Failed"
	V = "Failed"
	d = "Failed"
	DS_Is = "Failed"
	DS_kap = "Failed"
	DS_Vth = "Failed"

else:
	Is = extracted_p_nmos[0]
	kap = extracted_p_nmos[1]
	Vth = extracted_p_nmos[2]
	V = OptNMOS.objective(extracted_p_nmos)
	d = (step**2)*(Is**-2 + kap**-2 + Vth**-2)

	delta = 1e-3
	DS_Is = (EKV_model.evaluate(outputNMOS[500,:-1],extracted_p_nmos + np.array([delta,0,0]))) \
	/EKV_model.evaluate(outputNMOS[500,:-1],extracted_p_nmos)/((Is + delta)/Is)

	DS_kap = (EKV_model.evaluate(outputNMOS[500,:-1],extracted_p_nmos + np.array([0,delta,0]))) \
	/EKV_model.evaluate(outputNMOS[500,:-1],extracted_p_nmos)/((kap + delta)/kap)

	DS_Vth = (EKV_model.evaluate(outputNMOS[500,:-1],extracted_p_nmos + np.array([0,0,delta]))) \
	/EKV_model.evaluate(outputNMOS[500,:-1],extracted_p_nmos)/((Vth + delta)/Vth)

report = open("Reports/report_task4and5.txt", "w+")
report.write("Task 4 (quasi-Newton)\n")
report.write("==========================================================================\n")
report.write("Extracted Parameters\n")
report.write("-------------------------------------\n")
report.write("Is:    {0}\n".format(Is))
report.write("kappa: {0}\n".format(kap))
report.write("Vth:   {0}\n".format(Vth))
report.write("-------------------------------------\n\n")
report.write("Deviations\n")
report.write("-------------------------------------\n")
report.write("Absolute Deviation: {0}\n".format(V))
report.write("Relative Deviation: {0}\n".format(d))
report.write("-------------------------------------\n\n")
report.write("Parameter Sensitivity\n")
report.write("-------------------------------------\n")
report.write("Is Sensitivity:    {0}\n".format(DS_Is))
report.write("kappa Sensitivity: {0}\n".format(DS_kap))
report.write("Vth Sensitivity:   {0}\n".format(DS_Vth))
report.write("==========================================================================\n")
report.write("==========================================================================\n\n")

###################################################################################################
#Task 5
ones = np.ones((outputNMOS.shape[0],1))
outputNMOS = np.append(outputNMOS, ones, axis = 1)
def Id_ekv(x,a):
	Is = a[0]
	kap = a[1]
	Vth = a[2]
	Vgs = x[0]
	Vds = x[1]
	Id_measured = x[2]
	Vt = np.float64(26*10-3)
	Id = Is*(np.log(1 + np.exp((kap*(Vgs-Vth))/(2*Vt))))**2 \
	- Is*(np.log(1 + np.exp((kap*(Vgs-Vth) - Vds)/(2*Vt))))**2
	return Id/Id_measured



#Initial guesses
Is = 10**-7
kap = 1
Vth = 1
#Initial Parameter Guess
p_est = np.array([Is,kap,Vth],dtype = np.float64)

#Tolerance and Step Size for optimization loop
tol = np.float64(10**-7)
step = np.float64(10**-5)

#Set-up of the EKV model with 3 independent variables and 3 parameters
num_indep = 3
num_param = 3
EKV_model = S_model(num_indep,num_param,Id_ekv,p_est)


#Set-up of the optimal parameter extraction problem with the measured data
OptNMOS = OPES(EKV_model,outputNMOS,p_est,tol,step)


#Extract the parameters
extracted_p_nmos = OptNMOS.extractParam()
if extracted_p_nmos.size == 0:
	Is = "Failed"
	kap = "Failed"
	Vth = "Failed"
	V = "Failed"
	d = "Failed"
	DS_Is = "Failed"
	DS_kap = "Failed"
	DS_Vth = "Failed"

else:
	Is = extracted_p_nmos[0]
	kap = extracted_p_nmos[1]
	Vth = extracted_p_nmos[2]
	V = OptNMOS.objective(extracted_p_nmos)
	d = (step**2)*(Is**-2 + kap**-2 + Vth**-2)

	delta = 1e-3
	DS_Is = (EKV_model.evaluate(outputNMOS[500,:-1],extracted_p_nmos + np.array([delta,0,0]))) \
	/EKV_model.evaluate(outputNMOS[500,:-1],extracted_p_nmos)/((Is + delta)/Is)

	DS_kap = (EKV_model.evaluate(outputNMOS[500,:-1],extracted_p_nmos + np.array([0,delta,0]))) \
	/EKV_model.evaluate(outputNMOS[500,:-1],extracted_p_nmos)/((kap + delta)/kap)

	DS_Vth = (EKV_model.evaluate(outputNMOS[500,:-1],extracted_p_nmos + np.array([0,0,delta]))) \
	/EKV_model.evaluate(outputNMOS[500,:-1],extracted_p_nmos)/((Vth + delta)/Vth)


report.write("Task 5 (quasi-Newton)\n")
report.write("==========================================================================\n")
report.write("Extracted Parameters\n")
report.write("-------------------------------------\n")
report.write("Is:    {0}\n".format(Is))
report.write("kappa: {0}\n".format(kap))
report.write("Vth:   {0}\n".format(Vth))
report.write("-------------------------------------\n\n")
report.write("Deviations\n")
report.write("-------------------------------------\n")
report.write("Absolute Deviation: {0}\n".format(V))
report.write("Relative Deviation: {0}\n".format(d))
report.write("-------------------------------------\n\n")
report.write("Parameter Sensitivity\n")
report.write("-------------------------------------\n")
report.write("Is Sensitivity:    {0}\n".format(DS_Is))
report.write("kappa Sensitivity: {0}\n".format(DS_kap))
report.write("Vth Sensitivity:   {0}\n".format(DS_Vth))
report.close()