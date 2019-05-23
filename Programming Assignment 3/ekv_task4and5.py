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
print ("Starting task 4")

def Id_ekv(x,a):
	Is = a[0]
	kap = a[1]
	Vth = a[2]
	Vgs = x[0]
	Vds = x[1]
	Vt = np.float64(26e-3)
	Id = Is*(np.log(1 + np.exp(kap*(Vgs-Vth)/(2*Vt))))**2 \
	- Is*(np.log(1 + np.exp((kap*(Vgs-Vth) - Vds)/(2*Vt))))**2
	return Id



#Initial guesses
Is = 1e-7
kap = 1
Vth = 1
#Initial Parameter Guess
p_est = np.array([Is,kap,Vth],dtype = np.float64)

#Tolerance and Step Size for optimization loop
tol = np.float64(1e-14)
step = np.float64(1e-5)

#Set-up of the EKV model with 2 independent variables and 3 parameters
num_indep = 2
num_param = 3
EKV_model = S_model(num_indep,num_param,Id_ekv,p_est)


#Set-up of the optimal parameter extraction problem with the measured data
OptNMOS = OPES(EKV_model,outputNMOS,p_est,tol,step)

print ("Extracting task4")

#Extract the parameters
extracted_p_nmos = OptNMOS.extractParam()

print ("reporting task4")
# if extracted_p_nmos.size == 0:
# 	Is = "Failed"
# 	kap = "Failed"
# 	Vth = "Failed"
# 	V = "Failed"
# 	d = "Failed"
# 	DS_Is = "Failed"
# 	DS_kap = "Failed"
# 	DS_Vth = "Failed"

# else:
# 	Is = extracted_p_nmos[0]
# 	kap = extracted_p_nmos[1]
# 	Vth = extracted_p_nmos[2]
# 	V = OptNMOS.objective(extracted_p_nmos)
	# d = (step**2)*(Is**-2 + kap**-2 + Vth**-2)

	# print (extracted_p_nmos + np.array([delta,0,0]))
	# DS_Is = (EKV_model.evaluate(outputNMOS[200,:-1], extracted_p_nmos + np.array([Is*0.001,0,0]))) \
	# /EKV_model.evaluate(outputNMOS[200,:-1],extracted_p_nmos)/((Is + Is*0.001)/Is)

	# DS_kap = (EKV_model.evaluate(outputNMOS[200,:-1],extracted_p_nmos + np.array([0,kap*0.001,0]))) \
	# /EKV_model.evaluate(outputNMOS[200,:-1],extracted_p_nmos)/((kap + kap*0.001)/kap)

	# DS_Vth = (EKV_model.evaluate(outputNMOS[200,:-1],extracted_p_nmos + np.array([0,0,Vth*0.001]))) \
	# /EKV_model.evaluate(outputNMOS[200,:-1],extracted_p_nmos)/((Vth + Vth*0.001)/Vth)
row_divider = "+----------------+----------------+----------------+-------------------+-------------------+\n"
blank_row = "|  {0}  |  {1}  |  {2}  |   {3}   |   {4}    |\n"

report = open("Reports/report_task4and5.txt", "w+")
report.write("**Results displayed are truncated to 12 significant figures. This is done mainly for generating clean tables as shown below.**\n")
report.write("**Note that this truncation is only for display purposes. The solver methods themselves don't perform this truncation.**\n")
report.write("==================================================\n")
report.write("Task 4 (quasi-Newton)\n")
report.write("==================================================\n")
report.write(row_divider)
report.write("|       Is       |      kappa     |       Vth      | Absolute Residual | Relative Residual |\n")
report.write(row_divider)

k = 0
for i in OptNMOS.report_data:
	print (i)
	# line = blank_row.format(("%.12f"%i[0][0])[:12],("%.12f"%i[0][1])[:12],("%.12f"%i[0][2])[:12],("%.12f"%i[1])[:12],("%.12f"%i[2])[:12])
	# report.write(line)
	# report.write(row_divider)

# report.write("Extracted Parameters\n")
# report.write("-------------------------------------\n")
# report.write("Is:    {0}\n".format(Is))
# report.write("kappa: {0}\n".format(kap))
# report.write("Vth:   {0}\n".format(Vth))
# report.write("-------------------------------------\n\n")
# report.write("Deviations\n")
# report.write("-------------------------------------\n")
# report.write("Absolute Deviation: {0}\n".format(V))
# # report.write("Relative Deviation: {0}\n".format(d))
# report.write("-------------------------------------\n\n")
# report.write("Parameter Sensitivity\n")
# report.write("-------------------------------------\n")
# report.write("Is Sensitivity:    {0}\n".format(DS_Is))
# report.write("kappa Sensitivity: {0}\n".format(DS_kap))
# report.write("Vth Sensitivity:   {0}\n".format(DS_Vth))
report.write("==========================================================================\n")
report.write("==========================================================================\n\n")
report.close()

###################################################################################################
#Task 5

# print ("Starting task 5")
# ones = np.ones((outputNMOS.shape[0],1))
# outputNMOS = np.append(outputNMOS, ones, axis = 1)
# def Id_ekv(x,a):
# 	Is = a[0]
# 	kap = a[1]
# 	Vth = a[2]
# 	Vgs = x[0]
# 	Vds = x[1]
# 	Id_measured = x[2]
# 	Vt = np.float64(26e-3)
# 	Id = Is*(np.log(1 + np.exp((kap*(Vgs-Vth))/(2*Vt))))**2 \
# 	- Is*(np.log(1 + np.exp((kap*(Vgs-Vth) - Vds)/(2*Vt))))**2
# 	return Id/Id_measured



# #Initial guesses
# Is = 10**-7
# kap = 1
# Vth = 1
# #Initial Parameter Guess
# p_est = np.array([Is,kap,Vth],dtype = np.float64)

# #Tolerance and Step Size for optimization loop
# tol = np.float64(10**-7)
# step = np.float64(10**-5)

# #Set-up of the EKV model with 3 independent variables and 3 parameters
# num_indep = 3
# num_param = 3
# EKV_model = S_model(num_indep,num_param,Id_ekv,p_est)


# #Set-up of the optimal parameter extraction problem with the measured data
# OptNMOS = OPES(EKV_model,outputNMOS,p_est,tol,step)


# #Extract the parameters
# print ("extracting task 5")
# extracted_p_nmos = OptNMOS.extractParam()

# print ("Reporting task 5")
# if extracted_p_nmos.size == 0:
# 	Is = "Failed"
# 	kap = "Failed"
# 	Vth = "Failed"
# 	V = "Failed"
# 	d = "Failed"
# 	DS_Is = "Failed"
# 	DS_kap = "Failed"
# 	DS_Vth = "Failed"

# else:
# 	Is = extracted_p_nmos[0]
# 	kap = extracted_p_nmos[1]
# 	Vth = extracted_p_nmos[2]
# 	V = OptNMOS.objective(extracted_p_nmos)
# 	d = (step**2)*(Is**-2 + kap**-2 + Vth**-2)

# 	delta = 1e-3
# 	DS_Is = (EKV_model.evaluate(outputNMOS[500,:-1],extracted_p_nmos + np.array([delta,0,0]))) \
# 	/EKV_model.evaluate(outputNMOS[500,:-1],extracted_p_nmos)/((Is + delta)/Is)

# 	DS_kap = (EKV_model.evaluate(outputNMOS[500,:-1],extracted_p_nmos + np.array([0,delta,0]))) \
# 	/EKV_model.evaluate(outputNMOS[500,:-1],extracted_p_nmos)/((kap + delta)/kap)

# 	DS_Vth = (EKV_model.evaluate(outputNMOS[500,:-1],extracted_p_nmos + np.array([0,0,delta]))) \
# 	/EKV_model.evaluate(outputNMOS[500,:-1],extracted_p_nmos)/((Vth + delta)/Vth)


# report.write("Task 5 (quasi-Newton)\n")
# report.write("==========================================================================\n")
# report.write("Extracted Parameters\n")
# report.write("-------------------------------------\n")
# report.write("Is:    {0}\n".format(Is))
# report.write("kappa: {0}\n".format(kap))
# report.write("Vth:   {0}\n".format(Vth))
# report.write("-------------------------------------\n\n")
# report.write("Deviations\n")
# report.write("-------------------------------------\n")
# report.write("Absolute Deviation: {0}\n".format(V))
# report.write("Relative Deviation: {0}\n".format(d))
# report.write("-------------------------------------\n\n")
# report.write("Parameter Sensitivity\n")
# report.write("-------------------------------------\n")
# report.write("Is Sensitivity:    {0}\n".format(DS_Is))
# report.write("kappa Sensitivity: {0}\n".format(DS_kap))
# report.write("Vth Sensitivity:   {0}\n".format(DS_Vth))
# report.close()