"""
ECE 4960 SPRING 2019
Programming Assignment 5
Filter Simulation
Author: Tejas Advait (TA275)
"""

import numpy as np
from ode_solver import ForwardEuler, RK34, AdaptiveRK34, TRBDF2
import time
import matplotlib.pyplot as plt

from functools import partial
#All physical values are in SI units

class Filter:
	def __init__(self, R, L, C, VS, F, init_x, init_t, end_t, step1, step2, filter_type,directory):
		self.R = R
		self.L = L
		self.C = C
		self.VS = VS
		self.f = partial(F,self.R,self.L,self.C,self.VS)
		self.init_x = init_x
		self.init_t = init_t
		self.end_t = end_t
		self.step1 = step1
		self.step2 = step2
		self.filter_type = filter_type
		self.directory = directory

		#ODE setup and solution with step size step1
		#Forward Euler###############################
		FE1 = ForwardEuler(self.init_t, self.end_t, self.init_x,self.f, self.step1)
		FE1_data = self.ODE_data(FE1)

		#RK34########################################
		RKNA1 = RK34(self.init_t, self.end_t, self.init_x,self.f, self.step1)
		RKNA1_data = self.ODE_data(RKNA1)

		#TR-BDF2###############################
		TRBDF2NA1 = TRBDF2(self.init_t, self.end_t, self.init_x,self.f, self.step1)
		TRBDF2NA1_data = self.ODE_data(TRBDF2NA1)

		#ODE setup and Solution with step size step2
		#Forward Euler###############################
		FE2 = ForwardEuler(self.init_t, self.end_t, self.init_x,self.f, self.step2)
		FE2_data = self.ODE_data(FE2)

		#RK34########################################
		RKNA2 = RK34(self.init_t, self.end_t, self.init_x,self.f, self.step2)
		RKNA2_data = self.ODE_data(RKNA2)

		#TR-BDF2###############################
		TRBDF2NA2 = TRBDF2(self.init_t, self.end_t, self.init_x,self.f, self.step2)
		TRBDF2NA2_data = self.ODE_data(TRBDF2NA2)


		#Adaptive RK34###############################
		RKA = AdaptiveRK34(self.init_t, self.end_t, self.init_x,self.f, self.step1)
		RKA_data = self.ODE_data(RKA)

		self.step1_str = self.format_e(step1)
		self.step2_str = self.format_e(step2)
		self.data = [(FE1_data,"Forward Euler with step "+self.step1_str+"s"),
		(RKNA1_data,"RK34 with step "+self.step1_str+"s"),
		(FE2_data,"Forward Euler with step "+self.step2_str+"s"),
		(RKNA2_data,"RK34 with step "+self.step2_str+"s"),
		(RKA_data, "Adaptive RK34"),
		(TRBDF2NA1_data, "TR-BDF2 with step "+self.step1_str+"s"),
		(TRBDF2NA2_data, "TR-BDF2 with step "+self.step2_str+"s")
		]

	@staticmethod
	def format_e(n):
		a = '%e' % n
		return a.split('e')[0].rstrip('0').rstrip('.') + 'e' + a.split('e')[1]


	@staticmethod
	def ODE_data(ODE):
		"""
		This function solves the ODE and returns a tuple which contains:
		1) exec_time: Execution time for the solver
		2) t: Timestamps in ns
		3) V: V values at the timestamps
		"""
		start = time.time()
		ODE.solve()
		end = time.time()
		exec_time = end-start #Execution time
		t = []
		V = []
		for i in range (len(ODE.solution)):
			t.append(ODE.solution[i][1])
			V.append(ODE.solution[i][0][1,0])

		return (exec_time,t,V)

	def report(self):
		row_divider = "+----------------+----------------+----------------+\n"
		text = []
		a = 12 - len(self.step1_str)
		a1 = a//2
		a2 = a - a1
		step1 = (a1*" ") + self.step1_str + (a2*" ")

		b = 12 - len(self.step2_str)
		b1 = b//2
		b2 = b - b1
		step2 = (b1*" ") + self.step2_str + (b2*" ")
		

		blank_row = "| {0}  |  {1}  |  {2}  |\n"
		text.append(self.filter_type+" Filter Execution Time Report\n")
		text.append("==================================================\n")
		text.append("**Results displayed are truncated to 12 significant figures. This is done mainly for generating clean tables as shown below.**\n")
		text.append("**Note that this truncation is only for display purposes. The solver methods themselves don't perform this truncation.**\n")
		text.append("==================================================\n")

		text.append(row_divider)
		text.append("|     Method     |    Step Size   | Execution Time |\n")
		text.append(row_divider)
		text.append(blank_row.format("Forward Euler", step1,("%.12f"%self.data[0][0][0])[:12]))
		text.append(row_divider)
		text.append(blank_row.format("     RK34    ", step1,("%.12f"%self.data[1][0][0])[:12]))
		text.append(row_divider)
		text.append(blank_row.format("    TR-BDF2  ", step1,("%.12f"%self.data[5][0][0])[:12]))
		text.append(row_divider)
		text.append(blank_row.format("Forward Euler", step2,("%.12f"%self.data[2][0][0])[:12]))
		text.append(row_divider)
		text.append(blank_row.format("     RK34    ", step2,("%.12f"%self.data[3][0][0])[:12]))
		text.append(row_divider)
		text.append(blank_row.format("    TR-BDF2  ", step2,("%.12f"%self.data[6][0][0])[:12]))
		text.append(row_divider)
		text.append(blank_row.format("    ARK34    ", "  Adaptive  ",("%.12f"%self.data[4][0][0])[:12]))
		text.append(row_divider)

		file = open(self.directory+"/execution_times.txt", "w")
		for i in text:
			file.write(i)
		file.close()

	def plot(self):
		fig = plt.figure()
		plt.title(r"$V$ vs $Time$")
		for i in self.data:
			t = i[0][1]
			V = i[0][2]
			plt.plot(t,V, label = i[1])

		plt.xlabel(r"$Time$ (s)")
		plt.ylabel(r"$V$ (V)")
		plt.legend()
		plt.savefig(self.directory + '/V_vs_Time.png')

	def generate(self):
		self.report()
		self.plot()