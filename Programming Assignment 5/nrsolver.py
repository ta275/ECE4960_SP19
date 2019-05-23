"""
ECE 4960 SPRING 2019
Programming Assignment 3
Newton-Raphson Solver
Authors: Tejas Advait (TA275)

The NRSolver class provides a blueprint for setting up a root finding problem
using the Newton-Raphson method for the function f.
"""

from matrix import FullMatrix
from direct_full_solver import Direct_Full_Solver
import numpy as np

class NRSolver:

	def __init__(self, f, num_param, init_x = np.empty(0), tol = 1e-10, step = 1e-8, max_iter = 10):
		"""
		f: Function for which the roots need to be found.
		num_param: Number of paramters [int]
		init_param: Initial guess of parameters [np.ndarray]
		tol: Tolerance [float]
		step: Step size for calculating derivatives [np.float64]
		max_iter: Number of maximum iterations [int]
		"""

		self.f = f
		
		self.num_param = num_param
		self.h = np.float64(step)
		init_x = np.array(init_x)

		if init_x.size == 0:
			self.init_x = np.zeros((num_param,1))
		else:
			self.init_x = np.array(init_x, dtype=np.float64).flatten()
			self.init_x = self.init_x.reshape((self.init_x.shape[0],1))

		self.max_iter = max_iter
		self.tol = np.float64(tol)
		self.fx = self.f(self.init_x)

	def df_dxi(self, x0,i):
		"""
		Calculates the gradient of f at x0 w.r.t xi using the central
		differentiation scheme.
		"""
		dx = np.zeros_like(x0,dtype=np.float64)
		dx[i,0] = 0.5*self.h
		return (self.f(x0 + dx) - self.f(x0 - dx))/self.h

	def hessian(self,x0):
		"""
		Calculates the Hessian of f at x0.
		"""

		H = FullMatrix(self.num_param,self.num_param)

		for i in range(self.num_param):
			Hi = self.df_dxi(x0,i)
			for k in range (Hi.shape[0]):
				H.addElement(k,i,Hi[k,0])

		return H

	def one_iter(self,x0):
	
		hess = self.hessian(x0)
		self.fx = self.f(x0)

		b = FullMatrix(self.num_param, 1)
		for i in range (self.fx.shape[0]):
			b.addElement(i,0,self.fx[i,0])

		S = Direct_Full_Solver(hess,b)
		S.solve()
		delta = S.x.toNP()
		return -1*delta

	def solve(self):

		# fx = self.f(self.init_x)
		delx = self.one_iter(self.init_x)

		k = 0
		while np.linalg.norm(delx) > self.tol and np.linalg.norm(self.fx) > self.tol and k < self.max_iter:
			self.init_x = self.init_x + delx
			fx = self.f(self.init_x)
			delx = self.one_iter(self.init_x)
			k += 1

		if k == self.max_iter:
			raise Exception("Did not converge.")
		else:
			return self.init_x