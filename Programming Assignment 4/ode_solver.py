"""
ECE 4960 SPRING 2019
Programming Assignment 4
ODE Solvers
Author: Tejas Advait (TA275)
"""

import numpy as np
# from matrix import FullMatrix


class ODESolver(object):

	def __init__(self,init_t,end_t,init_x,f,step):
		"""
		Input:
			init_t: Initial value of t [np.float64]
			end_t: End value of t [np.float64]
			init_x: Initial value of x [numpy array]
			f: Function f [python function with two parameters, t and x]
			step: Step size [np.float64]

		The ODE is solved for the range [init_t,end_t] with a step size step, and
		init_x as the initial value of x, i.e, x(init_t) = init_x. f is the function
		on the right hand side of the ODE.

		The solution at all the steps (including the initial time) is stored in a 
		numpy matrix called solution. Each entry of this matrix is the value of x
		extended by the value of time at that time step, i.e, each entry is the
		vector x extended by one dimension to contain the value of time at that
		time step.
		"""
		self.init_t = init_t
		self.end_t = end_t
		self.init_x = init_x
		self.f = f
		self.step = step

		# self.num_steps = int((end_t - init_t)/step) #Number of total steps for non-adaptive methods

		self.solution = np.zeros((init_x.shape[0]+1,1),dtype = np.float64)
		self.solution[:-1,0] = init_x
		self.solution[-1,0] = init_t

		# self.solution = np.zeros((init_x.shape[0]+1,self.num_steps+1),dtype = np.float64)
		# self.solution[:-1,0] = init_x
		# self.solution[-1,0] = init_t
	
	def phi(self,x,t):
		"""
		Returns the increment.
		"""
		raise NotImplementedError()

	def h(self,x,t):
		"""
		Returns the time step.
		"""
		raise NotImplemntedError()


	def solve(self):
		"""
		Solve the ODE at all time steps in the range of t and update
		the entries of solution.
		"""
		xold = self.init_x
		told = self.init_t

		while told < self.end_t:
			
			xnew = xold + self.phi(xold,told)*self.h(xold,told)
			told += self.step
			xold = xnew
			sol = np.append(xnew,[[told]],axis = 0)
			self.solution = np.append(self.solution,sol,axis = 1)


class ForwardEuler(ODESolver):

	def __init__(self,init_t,end_t,init_x,f,step):

		super().__init__(init_t,end_t,init_x,f,step)

	def phi(self,x,t):
		return self.f(x,t)

	def h(self,x,t):
		return self.step

	def solve(self):
		super().solve()
			
			

class RK34(ODESolver):
	def __init__(self,init_t,end_t,init_x,f,step):

		super().__init__(init_t,end_t,init_x,f,step)

	def k(self,x,t):
		k1 = self.f(x,t)
		k2 = self.f(x + k1*self.step/2,t + self.step/2)
		k3 = self.f(x+3*k2*self.step/4, t + 3*self.step/4)
		k4 = self.f(x + k3*self.step, t + self.step)
		return [k1,k2,k3,k4]

	def phi(self,x,t):
		k = self.k(x,t)
		k1 = k[0]
		k2 = k[1]
		k3 = k[2]
		k4 = k[3]
		return (7*k1 + 6*k2 + 8*k3 + 3*k4)/24

	def h(self,x,t):
		return self.step

	def solve(self):
		super().solve()



class AdaptiveRK34(RK34):
	def __init__(self,init_t,end_t,init_x,f,step):

		super().__init__(init_t,end_t,init_x,f,step)

	def k(self,x,t):
		return super().k(x,t)

	def phi(self,x,t):
		return super().phi(x,t)

	def h(self,x,t):
		eR = np.float64(10**-7)
		eA = np.float64(10**-14)
		
		k = self.k(x,t)
		k1 = k[0]
		k2 = k[1]
		k3 = k[2]
		k4 = k[3]

		enew = np.linalg.norm((1/72)*(-5*k1+6*k2+8*k3-9*k4)*self.step)
		xnew = np.linalg.norm(x + self.step*(7*k1 + 6*k2 + 8*k3 + 3*k4)/24)
		hnew = self.step*(np.power(eR/(enew/(xnew+eA)),1/3))
		self.step = hnew
		return hnew


	def solve(self):
		super().solve()



def f(x,t):
	return np.array([4*np.exp(0.8*t)-0.5*x[0]],dtype = np.float64).reshape(1,1)

def x(t):
	ans = (4/1.3)*(np.exp(0.8*t) - np.exp(-0.5*t))+2*np.exp(-0.5*t)
	return np.array([ans],dtype = np.float64).reshape(1,1)

FE = ForwardEuler(0,5,np.array([2],dtype=np.float64),f,1)
FE.solve()

RKNA = RK34(0,5,np.array([2],dtype=np.float64),f,1)
RKNA.solve()

RKA = AdaptiveRK34(0,5,np.array([2],dtype=np.float64),f,1)
RKA.solve()
# print (ODE.solution)
# for i in range (FE.solution.shape[1]):
# 	print ("FE: {0}, RKNA: {1}, GT: {2}, ".format(FE.solution[0,i],RKNA.solution[0,i],x(i)[0,0]))

for i in range (RKA.solution.shape[1]):
	print ("RKA: {0}, GT: {1}, ".format(RKA.solution[0,i],x(RKA.solution[1,i])[0,0]))