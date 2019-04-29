"""
ECE 4960 SPRING 2019
Programming Assignment 4
Simple RC Circuit Assembly
Author: Tejas Advait (TA275)
"""

# import matplotlib.pyplot as plt

import numpy as np
from ode_solver import ForwardEuler, RK34, AdaptiveRK34
from current_source import *
import time


#R and C values
R1 = 1e4
R2 = 1e4
R3 = 1e4
C1 = 1e-12
C2 = 1e-12

# def f(x,t):
# 	"""
# 	dx/dt = f(x,t); f(x,t) for simple RC as shown in figure 3
# 	"""
# 	A = np.zeros((2,2),dtype = np.float64)
# 	A[0,0] = -1*(1/(C1*R1) + 1/(C1*R2))
# 	A[0,1] = 1/(C1*R2)
# 	A[1,0] = 1/(C2*R2)
# 	A[1,1] = -1*(1/(C2*R2) + 1/(C2*R3))

# 	B = np.zeros((2,1),dtype = np.float64)
# 	B[0,0] = large_signal(t)/C1

# 	return np.dot(A,x) + B

def f(x,t):
	V1 = x[0]
	V2 = x[1]
	f1 = -1*V1/(C1*R1) - (V1-V2)/(C1*R2) + large_signal(t)/C1
	f2 = -1*(V2-V1)/(C2*R2) - V2/(C2*R3)
	A = np.zeros((2,1),dtype = np.float64)
	A[0,0] = f1
	A[1,0] = f2
	return A

def ODE_data(ODE):
	start = time.time()
	ODE.solve()
	end = time.time()
	exec_time = end-start #Execution time
	t = []
	V1 = []
	V2 = []
	for i in range (ODE.solution.shape[1]):
		t.append(ODE.solution[2,i])
		V1.append(ODE.solution[0,i])
		V2.append(ODE.solution[1,i])

	return (exec_time,t,V1,V2)


#Initial Conditions and Step Size
#Unit of time is ns
init_x = np.zeros((2,1),dtype = np.float64)
init_t = 0
end_t = 100
step1 = 1
step2 = 0.2

#ODE setup and solution with step size 1ns
#Forward Euler###############################
FE1 = ForwardEuler(init_t,end_t,init_x,f,step1)
FE1_data = ODE_data(FE1)

#RK34########################################
RKNA1 = RK34(init_t,end_t,init_x,f,step1)
RKNA1_data = ODE_data(RKNA1)



#ODE setup and Solution with step size 0.2ns
#Forward Euler###############################
FE2 = ForwardEuler(init_t,end_t,init_x,f,step2)
FE2_data = ODE_data(FE2)

#RK34########################################
RKNA2 = RK34(init_t,end_t,init_x,f,step2)
RKNA2_data = ODE_data(RKNA2)


#Adaptive RK34###############################
import pickle
RKA = AdaptiveRK34(init_t,end_t,init_x,f,step1)
RKA_data = ODE_data(RKA)
file = open("rka_data.bin","wb+")
pickle.dump(RKA_data,file)
file.close()
#Report and plot generation
text = []

row_divider = "+----------------+----------------+----------------+\n"

blank_row = "| {0}  |  {1}  |  {2}  |\n"
text.append("Simple RC Circuit Execution Time Report\n")
text.append("==================================================\n")
text.append("**Results displayed are truncated to 12 significant figures. This is done mainly for generating clean tables as shown below.**\n")
text.append("**Note that this truncation is only for display purposes. The solver methods themselves don't perform this truncation.**\n")
text.append("==================================================\n")

text.append(row_divider)
text.append("|     Method     |    Step Size   | Execution Time |\n")
text.append(row_divider)
text.append(blank_row.format("Forward Euler", "    1ns     ",("%.12f"%FE1_data[0])[:12]))
text.append(row_divider)
text.append(blank_row.format("     RK34    ", "    1ns     ",("%.12f"%RKNA1_data[0])[:12]))
text.append(row_divider)
text.append(blank_row.format("Forward Euler", "   0.2ns    ",("%.12f"%FE2_data[0])[:12]))
text.append(row_divider)
text.append(blank_row.format("     RK34    ", "   0.2ns    ",("%.12f"%RKNA2_data[0])[:12]))
text.append(row_divider)
text.append(blank_row.format("    ARK34    ", "  Adaptive  ",("%.12f"%RKA2_data[0])[:12]))
text.append(row_divider)

file = open("reports/task4-simple_rc/execution_times.txt", "w")
for i in text:
	file.write(i)
file.close()