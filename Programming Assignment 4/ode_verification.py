"""
ECE 4960 SPRING 2019
Programming Assignment 4
ODE Solver Verification
Author: Tejas Advait (TA275)
"""

import matplotlib.pyplot as plt

import numpy as np
from ode_solver import ForwardEuler, RK34, AdaptiveRK34

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

text = []


row_divider = "+----------------+----------------+----------------+----------------+\n"
blank_row = "|  {0}  |  {1}  |  {2}  |  {3}  |\n"
text.append("ODE Verification Report\n")
text.append("==================================================\n")
text.append("**Results are truncated to 12 significant figures**\n")
text.append("t = time\nx_true = Ground truth value of x(t)\n")
text.append("x_FE = Simulated value of x(t) using Forward Euler\n")
text.append("x_RK34 = Simulated value of x(t) using RK34\n")
text.append("x_ARK34 = Simulated value of x(t) using Adaptive RK34\n")
text.append("|ex| = Normalized error\n\n")
text.append("==================================================\n")
text.append("Forward Euler\n")
text.append("==================================================\n")

text.append(row_divider)
text.append("|        t       |     x_true     |      x_FE      |      |ex|      |\n")
text.append(row_divider)

t_fe = []
e_fe = []
for i in range (FE.solution.shape[1]):
	xi = FE.solution[:-1,i]
	ti = FE.solution[-1,i]
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

file = open("reports/verification.txt", "w")
for i in text:
	file.write(i)

text = []
t_rkna = []
e_rkna = []
for i in range (RKNA.solution.shape[1]):
	xi = RKNA.solution[:-1,i]
	ti = RKNA.solution[-1,i]
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
for i in range (RKA.solution.shape[1]):
	xi = RKA.solution[:-1,i]
	ti = RKA.solution[-1,i]
	er = ex(x(ti),xi)
	t_rka.append(ti)
	e_rka.append(er)
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

plt.xlabel(r"$|e_{x}|$")
plt.ylabel(r"$t$")
plt.legend()
plt.savefig('reports/verification_plot.png')
plt.show()