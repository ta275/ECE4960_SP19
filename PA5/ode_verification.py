"""
ECE 4960 SPRING 2019
Programming Assignment 5
ODE Solver Verification
Author: Tejas Advait (TA275)
"""

import matplotlib.pyplot as plt

import numpy as np
from ode_solver import ForwardEuler, RK34, AdaptiveRK34, TRBDF2, AdaptiveTRBDF2

def f(x,t):
	"""
	dx/dt = f(x,t)
	"""
	return np.array([4*np.exp(0.8*t)-0.5*x[0]],dtype = np.float64).reshape(1,1)

def x(t):
	"""
	Ground Truth Solution
	"""
	ans = (4/1.3)*(np.exp(0.8*t) - np.exp(-0.5*t))+2*np.exp(-0.5*t)
	return np.array([ans],dtype = np.float64).reshape(1,1)

def ex(x_gnd,x_sim):
	return  np.linalg.norm(x_gnd-x_sim)/np.linalg.norm(x_gnd)

def ODE_data(ODE):
	start = time.time()
	ODE.solve()
	end = time.time()
	exec_time = end-start #Execution time
	t = []
	V1 = []
	V2 = []
	for i in range (len(ODE.solution)):
		t.append(ODE.solution[i][1])
		V1.append(ODE.solution[i][0][0])
		V2.append(ODE.solution[i][0][1])

	return (exec_time,t,V1,V2)

init_x = np.array([[2]],dtype = np.float64)
init_t = 0
end_t = 5
step = 1

FE = ForwardEuler(init_t,end_t,init_x,f,step)
FE.solve()

RKNA = RK34(init_t,end_t,init_x,f,step)
RKNA.solve()

RKA = AdaptiveRK34(init_t,end_t,init_x,f,step)
RKA.solve()

TR_BDF2NA = TRBDF2(init_t,end_t,init_x,f,step)
TR_BDF2NA.solve()

TR_BDF2A = AdaptiveTRBDF2(init_t,end_t,init_x,f,step)
TR_BDF2A.solve()



#Report and plot generation
text = []


row_divider = "+----------------+----------------+----------------+----------------+\n"
blank_row = "|  {0}  |  {1}  |  {2}  |  {3}  |\n"
text.append("ODE Verification Report\n")
text.append("==================================================\n")
text.append("**Results displayed are truncated to 12 significant figures. This is done mainly for generating clean tables as shown below.**\n")
text.append("**Note that this truncation is only for display purposes. The solver methods themselves don't perform this truncation.**\n")
text.append("==================================================\n")
text.append("Table header variables:\n")
text.append("t = time\nx_true = Ground truth value of x(t)\n")
text.append("x_FE = Simulated value of x(t) using Forward Euler\n")
text.append("x_RK34 = Simulated value of x(t) using RK34\n")
text.append("x_ARK34 = Simulated value of x(t) using Adaptive RK34\n")
text.append("x_TR-BDF2 = Simulated value of x(t) using TR-BDF2\n")
text.append("x_TR-BDF2A = Simulated value of x(t) using Adaptive TR-BDF2\n")
text.append("|ex| = Normalized error\n\n")
text.append("==================================================\n")
text.append("Forward Euler\n")
text.append("==================================================\n")

text.append(row_divider)
text.append("|        t       |     x_true     |      x_FE      |      |ex|      |\n")
text.append(row_divider)

t_fe = []
e_fe = []
for i in range (len(FE.solution)):
	xi = FE.solution[i][0]
	ti = FE.solution[i][1]
	er = ex(x(ti),xi)
	t_fe.append(ti)
	e_fe.append(er)
	line = blank_row.format(("%.10f"%ti)[:12], ("%.10f"%x(ti)[0])[:12], ("%.10f"%xi[0])[:12], ("%.10f"%er)[:12])
	text.append(line)
	text.append(row_divider)

text.append("\n==================================================\n")
text.append("RK34\n")
text.append("==================================================\n")
text.append(row_divider)
text.append("|        t       |     x_true     |     x_RK34     |      |ex|      |\n")
text.append(row_divider)

file = open("reports/ode-verification/verification_results.txt", "w")
for i in text:
	file.write(i)

text = []
t_rkna = []
e_rkna = []
for i in range (len(RKNA.solution)):
	xi = RKNA.solution[i][0]
	ti = RKNA.solution[i][1]
	er = ex(x(ti),xi)
	t_rkna.append(ti)
	e_rkna.append(er)
	line = blank_row.format(("%.10f"%ti)[:12], ("%.10f"%x(ti)[0])[:12], ("%.10f"%xi[0])[:12], ("%.10f"%er)[:12])
	text.append(line)
	text.append(row_divider)

text.append("\n==================================================\n")
text.append("ARK34\n")
text.append("==================================================\n")
text.append(row_divider)
text.append("|        t       |     x_true     |     x_ARK34    |      |ex|      |\n")
text.append(row_divider)

for i in text:
	file.write(i)

text = []
t_rka = []
e_rka = []
for i in range (len(RKA.solution)):
	xi = RKA.solution[i][0]
	ti = RKA.solution[i][1]
	er = ex(x(ti),xi)
	t_rka.append(ti)
	e_rka.append(er)
	line = blank_row.format(("%.10f"%ti)[:12], ("%.10f"%x(ti)[0])[:12], ("%.10f"%xi[0])[:12], ("%.10f"%er)[:12])
	text.append(line)
	text.append(row_divider)

text.append("\n==================================================\n")
text.append("TR-BDF2\n")
text.append("==================================================\n")
text.append(row_divider)
text.append("|        t       |     x_true     |    x_TR-BDF2   |      |ex|      |\n")
text.append(row_divider)

for i in text:
	file.write(i)

text = []
t_trbdf = []
e_trbdf = []
for i in range (len(TR_BDF2NA.solution)):
	xi = TR_BDF2NA.solution[i][0]
	ti = TR_BDF2NA.solution[i][1]
	er = ex(x(ti),xi)
	t_trbdf.append(ti)
	e_trbdf.append(er)
	line = blank_row.format(("%.10f"%ti)[:12], ("%.10f"%x(ti)[0])[:12], ("%.10f"%xi[0])[:12], ("%.10f"%er)[:12])
	text.append(line)
	text.append(row_divider)


for i in text:
	file.write(i)

text = []
text.append("\n==================================================\n")
text.append("TR-BDF2A\n")
text.append("==================================================\n")
text.append(row_divider)
text.append("|        t       |     x_true     |   x_TR-BDF2A   |      |ex|      |\n")
text.append(row_divider)

for i in text:
	file.write(i)

text = []
t_trbdfa = []
e_trbdfa = []
for i in range (len(TR_BDF2A.solution)):
	xi = TR_BDF2A.solution[i][0]
	ti = TR_BDF2A.solution[i][1]
	er = ex(x(ti),xi)
	t_trbdfa.append(ti)
	e_trbdfa.append(er)
	line = blank_row.format(("%.10f"%ti)[:12], ("%.10f"%x(ti)[0])[:12], ("%.10f"%xi[0])[:12], ("%.10f"%er)[:12])
	text.append(line)
	text.append(row_divider)


for i in text:
	file.write(i)

file.close()

fig = plt.figure()
plt.title(r"Normalized Error ($|e_{x}|$) vs Time ($t$)")

plt.plot(t_fe,e_fe, label = "Forward Euler")
plt.plot(t_rkna,e_rkna, label = "RK34")
plt.plot(t_rka,e_rka, label = "Adaptive RK34")
plt.plot(t_trbdf,e_trbdf, label = "TR-BDF2")
plt.plot(t_trbdfa,e_trbdfa, label = "Adaptive TR-BDF2")

plt.xlabel(r"$|e_{x}|$")
plt.ylabel(r"$t$")
plt.legend()
plt.savefig('reports/ode-verification/error_plot.png')