"""
ECE 4960 SPRING 2019
Programming Assignment 5
Newton-Raphson Solver
Author: Tejas Advait (TA275)
"""

import numpy as np

class NRSolver:

	def __init__(self,f,init_x, step = 1e-8,tolerance = 1e-10,max_iter = 10):
		self.f = f
		self.init_x = np.float64(init_x)
		self.h = np.float64(step)
		self.tol = np.float64(tolerance)
		self.max_iter = max_iter

	def df_dx(self,x0):
		"""
		Central differentiation scheme to calculate the derivative of f w.r.t x
		at x = x0.
		"""
		return (self.f(x0 + 0.5*self.h) - self.f(x0 - 0.5*self.h))/self.h

	def solve(self):

		fx = self.f(self.init_x)
		delx = -1*fx/self.df_dx(self.init_x)

		k = 0
		while np.abs(delx) > self.tol and np.abs(fx) > self.tol and k < self.max_iter:
			self.init_x = self.init_x + delx
			fx = self.f(self.init_x)
			delx = -1*fx/self.df_dx(self.init_x)
			k += 1

		if k == self.max_iter:
			raise Exception("Did not converge.")
		else:
			return self.init_x