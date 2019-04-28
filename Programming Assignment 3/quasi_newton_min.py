"""
ECE 4960 SPRING 2019
Programming Assignment 3
Quasi-Newton Minimization
Authors: Tejas Advait (TA275)

The QNM class provides a blueprint for setting up a Quasi-Newton minimization
problem with a generic objective function V to be minimized.
"""


from num_diff import *
from matrix import FullMatrix
from direct_full_solver import Direct_Full_Solver
import numpy as np

class QNM:
	"""
	An instance is a representation of the Quasi-Newton minimization problem.
	"""

	def __init__(self, V, num_param, init_param = np.empty(0), tol = 10**-7, step = np.float(10**-7), max_iter = 10**2):
		"""
		V: Objective Function [python function which takes a np.ndarray as an
		input and returns a float]
		num_param: Number of paramters [int]
		init_param: Initial guess of parameters [np.ndarray]
		tol: Tolerance [float]
		step: Step size for calculating derivatives [np.float64]
		max_iter: Number of maximum iterations [int]
		"""

		self.V = V
		
		self.num_param = num_param
		self.step = step
		
		if init_param.size == 0:
			self.init_param = np.zeros(num_param)

		else:
			self.init_param = init_param

		self.max_iter = max_iter
		self.tol = tol

		self.residues = [] #Stores the residual at each iteration
		self.quad_conv = True #For quadratic-convergence validation
		self.grad = self.gradV()

	def gradV(self, param = np.empty(0)):
		"""
		Calculates the gradient of V at param.
		"""

		b = FullMatrix(self.num_param, 1)
		
		if param.size == 0:
			param = self.init_param

		for i in range(self.num_param):
			d = cd_diff1(self.V,param,i,self.step)
			b.addElement(i,0,d)
		return b

	def hessian(self):
		"""
		Calculates the Hessian of V at self.init_param.
		"""

		H = FullMatrix(self.num_param,self.num_param)
		for i in range(self.num_param):
			for j in range(self.num_param):
				d = cd_diff2(self.V, self.init_param, i, j, self.step)
				H.addElement(i,j,d)

		return H

	def one_iter(self):
		"""
		One iteration of the quasi-newton method.
		"""
	
		hess = self.hessian()
		S = Direct_Full_Solver(hess,self.grad)
		S.solve()
		delta = -1*(S.x.toNP().flatten())
		self.residues.append(np.linalg.norm(self.grad.toNP().flatten()))
		return delta

	def updateParam(self):
		"""
		Updates parameter to their optimal values such that
		the objective function is minimized using quasi-newton
		method.
		"""
		
		num_iter = 1
		try:
			while num_iter <= self.max_iter:
				# if self.V(self.init_param) == 0:
				# 	break
				self.grad = self.gradV(self.init_param)
				norm1 = np.linalg.norm(self.grad.toNP().flatten())


				if norm1 < self.tol:
					break

				param_x = self.one_iter()
				norm2 = np.linalg.norm(param_x)
				
				if norm2 < self.tol:
					break



				num_iter += 1
				self.init_param += param_x

		except:
			self.init_param = np.empty(0)

		if np.linalg.norm(self.init_param)*0 != 0:
			self.init_param = np.empty(0)
			

		self.max_iter = num_iter

	def extractParam(self):
		"""
		Calculates and returns the optimal parameters.
		""" 
		i == 0
		while (i < len(self.residues)):
			if i/10**(-2**i) >= 10:
				self.quad_conv == False
				i = len(self.residues)

		self.updateParam()
		return self.init_param