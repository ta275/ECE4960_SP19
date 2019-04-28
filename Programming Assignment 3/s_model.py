"""
ECE 4960 SPRING 2019
Programming Assignment 3
S_model
Authors: Tejas Advait (TA275)

The S_model class provides a blueprint for instantiating a scalar model with
independent variables and parameters
"""
from matrix import FullMatrix
import numpy as np
import math

class S_model:
	"""
	An instance is a representation of the model for which parameter
	extraction needs to happen.
	"""

	def __init__(self, num_indep, num_param, S,param = np.empty(0)):
		"""
		num_indep: Number of independent variables
		num_param: Number of parameters
		S: Model function
		"""

		self.num_indep = num_indep
		self.num_param = num_param
		self.S = S
		if param.size == 0:
			self.param = np.zeros(num_param,dtype = np.float64)
		else:
			self.param = param

	def evaluate(self, indep, param = np.empty(0)):
		
		if param.size == 0:
			return self.S(indep,self.param)

		return self.S(indep,param)


	def evaluate_multiple(self, indeps, param = np.empty(0)):
		n = indeps.shape[0]
		Y = np.zeros((n,1))
		for i in range(n):
			x = indeps[i]
			y = self.evaluate(x,param)
			Y[i,0] = y

		return Y

	def gen_sample(self, num_sample, param = np.empty(0), indeps = np.empty(0),*, noise = True):
		"""
		Generates num_sample number of samples with random noise within 10-20% 
		from this model.
		"""

		if indeps.size == 0:
			indeps = np.array(np.random.rand(num_sample,self.num_indep)*10,dtype = np.float64)

		else:
			assert(indeps.shape[0] == num_sample)
			assert(indeps.shape[1] == self.num_indep)

		if param.size == 0:
			param = self.param
		
		else:
			assert(param.shape[0] == self.num_param)


		Y = self.evaluate_multiple(indeps,param)

		if noise:
			N = (np.random.rand(num_sample) + 1)/10
			
			for i in range(num_sample):
				l = np.random.random()
				if l >= 0.5:
					N[i] = 1 + N[i]
					Y[i,0] = Y[i,0]*N[i]

				else:
					N[i] = 1 - N[i]
					Y[i,0] = Y[i,0]*N[i]

		return np.append(indeps,Y,axis = 1)