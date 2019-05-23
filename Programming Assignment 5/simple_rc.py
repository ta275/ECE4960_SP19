"""
ECE 4960 SPRING 2019
Programming Assignment 4
Simple RC Circuit Assembly
Author: Tejas Advait (TA275)
"""

# import matplotlib.pyplot as plt

import numpy as np
from ode_solver import ForwardEuler, RK34, AdaptiveRK34, TRBDF2
from current_source import *
import time
import matplotlib.pyplot as plt

#All physical values are in SI units

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
	f1 = -1*((C1*R1)**-1 + (C1*R2)**-1)*V1 + ((C1*R2)**-1)*V2 + large_signal(t)/C1
	f2 = V1/(C2*R2) - V2*((C2*R2)**-1 + (C2*R3)**-1)
	A = np.zeros((2,1),dtype = np.float64)
	A[0,0] = f1
	A[1,0] = f2
	return A

def ODE_data(ODE):
	"""
	This function solves the ODE and returns a tuple which contains:
	1) exec_time: Execution time for the solver
	2) t: Timestamps in ns
	3) V1: V1 values at the timestamps
	4) V2: V2 values at the timestamps
	5) V12: V1-V2 values at the timestamps
	"""
	start = time.time()
	ODE.solve()
	end = time.time()
	exec_time = end-start #Execution time
	t = []
	V1 = []
	V2 = []
	V12 = []
	for i in range (len(ODE.solution)):
		t.append(ODE.solution[i][1]*1e9)
		V1.append(ODE.solution[i][0][0,0])
		V2.append(ODE.solution[i][0][1,0])
		V12.append(ODE.solution[i][0][0,0]-ODE.solution[i][0][1,0])

	return (exec_time,t,V1,V2,V12)


#Initial Conditions and Step Size
init_x = np.zeros((2,1),dtype = np.float64)
init_t = 0
end_t = 100e-9
step1 = 1e-9
step2 = 0.2e-9

#ODE setup and solution with step size 1ns
#Forward Euler###############################
FE1 = ForwardEuler(init_t, end_t, init_x,f, step1)
FE1_data = ODE_data(FE1)

#RK34########################################
RKNA1 = RK34(init_t,end_t,init_x,f,step1)
RKNA1_data = ODE_data(RKNA1)

#TR-BDF2###############################
TRBDF2NA1 = TRBDF2(init_t,end_t,init_x,f,step1)
TRBDF2NA1_data = ODE_data(TRBDF2NA1)

#ODE setup and Solution with step size 0.2ns
#Forward Euler###############################
FE2 = ForwardEuler(init_t,end_t,init_x,f,step2)
FE2_data = ODE_data(FE2)

#RK34########################################
RKNA2 = RK34(init_t,end_t,init_x,f,step2)
RKNA2_data = ODE_data(RKNA2)

#TR-BDF2###############################
TRBDF2NA2 = TRBDF2(init_t,end_t,init_x,f,step2)
TRBDF2NA2_data = ODE_data(TRBDF2NA2)


#Adaptive RK34###############################
RKA = AdaptiveRK34(init_t,end_t,init_x,f,step1)
RKA_data = ODE_data(RKA)



#Combining all the data
data = [(FE1_data,"Forward Euler with step 1ns"),
		(RKNA1_data,"RK34 with step 1ns"),
		(FE2_data,"Forward Euler with step 0.2ns"),
		(RKNA2_data,"RK34 with step 0.2 ns"),
		(RKA_data, "Adaptive RK34"),
		(TRBDF2NA1_data, "TR-BDF2 with step 1ns"),
		(TRBDF2NA2_data, "TR-BDF2 with step 0.2ns")]


#Report generation#################################################################################

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
text.append(blank_row.format("    TR-BDF2  ", "    1ns     ",("%.12f"%TRBDF2NA1_data[0])[:12]))
text.append(row_divider)
text.append(blank_row.format("Forward Euler", "   0.2ns    ",("%.12f"%FE2_data[0])[:12]))
text.append(row_divider)
text.append(blank_row.format("     RK34    ", "   0.2ns    ",("%.12f"%RKNA2_data[0])[:12]))
text.append(row_divider)
text.append(blank_row.format("    TR-BDF2  ", "   0.2ns    ",("%.12f"%TRBDF2NA2_data[0])[:12]))
text.append(row_divider)
text.append(blank_row.format("    ARK34    ", "  Adaptive  ",("%.12f"%RKA_data[0])[:12]))
text.append(row_divider)

file = open("reports/simple_rc/execution_times.txt", "w")
for i in text:
	file.write(i)
file.close()


#Plot generation###################################################################################

#Plot for V1
fig = plt.figure()
plt.title(r"$V1$ vs $Time$")
for i in data:
	t = i[0][1]
	v1 = i[0][2]
	plt.plot(t,v1, label = i[1])

plt.xlabel(r"$Time$ (ns)")
plt.ylabel(r"$V1$ (V)")
plt.legend()
plt.savefig('reports/simple_rc/V1_vs_Time.png')

#Plot for V2
fig2 = plt.figure()
plt.title(r"$V2$ vs $Time$")
for i in data:
	t = i[0][1]
	v2 = i[0][3]
	plt.plot(t,v2, label = i[1])

plt.xlabel(r"$Time$ (ns)")
plt.ylabel(r"$V2$ (V)")
plt.legend()
plt.savefig('reports/simple_rc/V2_vs_Time.png')

#Plot for V1-V2
fig2 = plt.figure()
plt.title(r"$V1-V2$ vs $Time$")
for i in data:
	t = i[0][1]
	v12 = i[0][4]
	plt.plot(t,v12, label = i[1])

plt.xlabel(r"$Time$ (ns)")
plt.ylabel(r"$V1-V2$ (V)")
plt.legend()
plt.savefig('reports/simple_rc/V12_vs_Time.png')