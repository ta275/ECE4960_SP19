"""
ECE 4960 SPRING 2019
Programming Assignment 3
Optimal Parameter Extraction for Scalar Models
Authors: Tejas Advait (TA275)

The OPES class provides a blueprint for setting up an optimal paramter extraction
problem for scalar models.
"""

from s_model import S_model
from quasi_newton_min import QNM
import numpy as np



class OPES:
	"""
	An instance is a representation of the optimal parameter extraction problem
	for scalar models.
	"""

	def __init__(self, model, measured, init_param = np.empty(0), tol=10**-7, step =np.float64(10**-5), max_iter=10**2):
		"""
		model: Model [S_model] 
		init_param: Initial guess of parameters [np.ndarray]
		tol: Tolerance [float]
		step: Step size for calculating derivatives [np.float64]
		max_iter: Number of maximum iterations [int]
		"""

		self.model = model
		if init_param.size == 0:
			self.init_param = np.zeros(model.num_param)
		else:
			self.init_param = init_param
		self.tol = tol
		self.step = step
		self.max_iter = max_iter
		self.measured = measured
		self.Q = QNM(self.objective, self.model.num_param, self.init_param, self.tol,
			self.step, self.max_iter)

		self.residues = []
		self.quad_conv = True

	def objective(self,param):
		"""
		Objective function to minimize.
		"""
		v = np.float64(0)
		for i in self.measured:
			v += (self.model.evaluate(i[:-1],param) - i[-1])**2

		return v

	def extractParam(self):
		self.Q.updateParam()
		self.quad_conv = self.Q.quad_conv
		self.residues = self.Q.residues
		self.max_iter = self.Q.max_iter
		self.init_param = self.Q.init_param
		return self.init_param