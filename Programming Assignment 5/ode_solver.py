"""
ECE 4960 SPRING 2019
Programming Assignment 5
ODE Solvers
Author: Tejas Advait (TA275)
"""

import numpy as np
import time
from nrsolver import NRSolver
# from matrix import FullMatrix

# np.seterr(all='raise')
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
		
		self.increment = 0		
		self.solution = [[init_x,init_t]]
	
	def phi(self,x,t):
		"""
		Updates the increment.
		"""
		raise NotImplementedError()

	def h(self,x,t):
		"""
		Updates the time step.
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
		
			self.phi(xold,told)
			self.h(xold,told)
			xnew = xold + self.increment*self.step
			
			told += self.step
			xold = xnew
			
			sol = [xnew,told]
			self.solution.append(sol)

class ForwardEuler(ODESolver):

	def __init__(self,init_t,end_t,init_x,f,step):

		super().__init__(init_t,end_t,init_x,f,step)

	def phi(self,x,t):
		self.increment = self.f(x,t)

	def h(self,x,t):
		pass

	def solve(self):
		super().solve()
			
			

class RK34(ODESolver):
	def __init__(self,init_t,end_t,init_x,f,step):

		super().__init__(init_t,end_t,init_x,f,step)
		self.k = []

	def K(self,x,t):
		k1 = self.f(x,t)
		k2 = self.f(x + k1*self.step/2,t + self.step/2)
		k3 = self.f(x + 3*k2*self.step/4, t + 3*self.step/4)
		k4 = self.f(x + k3*self.step, t + self.step)
		self.k = [k1,k2,k3,k4]

	def phi(self,x,t):
		self.K(x,t)
		k1 = self.k[0]
		k2 = self.k[1]
		k3 = self.k[2]
		k4 = self.k[3]
		self.increment = (7*k1 + 6*k2 + 8*k3 + 3*k4)/24
		

	def h(self,x,t):
		pass

	def solve(self):
		super().solve()



class AdaptiveRK34(RK34):
	def __init__(self,init_t,end_t,init_x,f,step):

		super().__init__(init_t,end_t,init_x,f,step)

	def K(self,x,t):
		super().K(x,t)

	def phi(self,x,t):
		super().phi(x,t)

	def h(self,x,t):
		eR = np.float64(1e-7)
		eA = np.float64(1e-14)
		k1 = self.k[0]
		k2 = self.k[1]
		k3 = self.k[2]
		k4 = self.k[3]
		
		er = (1/72)*(-5*k1+6*k2+8*k3-9*k4)*self.step
		xnew = x + self.step*self.increment

		enew_mag = np.sqrt(np.dot(er.flatten(), er)[0])
		xnew_mag = np.sqrt(np.dot(xnew.flatten(), xnew)[0])
		hnew = self.step*(np.power(eR/(enew_mag/(xnew_mag+eA)),1/3))
		self.step = hnew
		return hnew


	def solve(self):
		super().solve()

class TRBDF2(ODESolver):
	def __init__(self,init_t,end_t,init_x,f,step):
		super().__init__(init_t,end_t,init_x,f,step)
		self.gam = 2 - np.sqrt(np.float64(2))
		self.num_param = self.init_x.shape[0]
		self.a = 1 - self.gam
		self.b = self.a + 1

	def phi(self,x,t):
		pass

	def h(self,x,t):
		pass

	def solve(self):
		x_old = self.init_x
		t_old = self.init_t
		while t_old < self.end_t:

			f_tr = lambda xgam: xgam - x_old - \
			(self.gam*self.step/2)*(self.f(x_old,t_old) + self.f(xgam,t_old+self.gam*self.step))
			NR_tr = NRSolver(f_tr,self.num_param,x_old)
			x_gam = NR_tr.solve()

			f_bdf2 = lambda xnew: xnew + x_old*((self.a**2)/(self.gam*self.b))\
			- x_gam/(self.gam*self.b) - (self.step*self.a*self.f(xnew,t_old + self.step)/self.b)

			NR_bdf2 = NRSolver(f_bdf2, self.num_param,-1*x_old*((self.a**2)/(self.gam*self.b)\
			+ x_gam/(self.gam*self.b)))

			x_new = NR_bdf2.solve()
			
			t_old += self.step
			x_old = x_new
			
			sol = [x_new,t_old]
			self.solution.append(sol)


# class AdaptiveTRBDF2(TRBDF2):
# 	def __init__(self,init_t,end_t,init_x,f,step):
# 		super().__init__(init_t,end_t,init_x,f,step)

# 	def phi(self,x,t):
# 		pass

# 	def h(self,x,t):
# 		eR = np.float64(1e-7)
# 		eA = np.float64(1e-14)

		

# 		f_tr = lambda xgam: xgam - x - \
# 		(self.gam*self.step/2)*(self.f(x,t) + self.f(xgam,t+self.gam*self.step))
# 		NR_tr = NRSolver(f_tr,self.num_param,x)
# 		x_gam = NR_tr.solve()

# 		f_bdf2 = lambda xnew: xnew + x*((self.a**2)/(self.gam*self.b))\
# 		- x_gam/(self.gam*self.b) - (self.step*self.a*self.f(xnew,t + self.step)/self.b)

# 		NR_bdf2 = NRSolver(f_bdf2, self.num_param,-1*x*((self.a**2)/(self.gam*self.b)\
# 		+ x_gam/(self.gam*self.b)))

# 		x_new = NR_bdf2.solve()

# 		er = ((3*(self.gam**2)-4*self.gam+2)/(6*(self.gam-2)))*(self.f(x,t)/self.gam -\
# 		 self.f(x_gam,t+self.step*self.gam)/(self.gam*self.a) + self.f(x_new,t+self.step)/self.gam)

# 		enew_mag = np.sqrt(np.dot(er.flatten(), er)[0])
# 		xnew_mag = np.sqrt(np.dot(x_new.flatten(), x_new)[0])
# 		hnew = self.step*(np.power(eR/(enew_mag/(xnew_mag+eA)),1/3))
# 		self.step = hnew
# 		return hnew

# 	def solve(self):
# 		x_old = self.init_x
# 		t_old = self.init_t
# 		while t_old < self.end_t:
# 			self.h(x_old,t_old)

# 			f_tr = lambda xgam: xgam - x_old - \
# 			(self.gam*self.step/2)*(self.f(x_old,t_old) + self.f(xgam,t_old+self.gam*self.step))
# 			NR_tr = NRSolver(f_tr,self.num_param,x_old)
# 			x_gam = NR_tr.solve()

# 			f_bdf2 = lambda xnew: xnew + x_old*((self.a**2)/(self.gam*self.b))\
# 			- x_gam/(self.gam*self.b) - (self.step*self.a*self.f(xnew,t_old + self.step)/self.b)

# 			NR_bdf2 = NRSolver(f_bdf2, self.num_param,-1*x_old*((self.a**2)/(self.gam*self.b)\
# 			+ x_gam/(self.gam*self.b)))

# 			x_new = NR_bdf2.solve()
			
# 			t_old += self.step
# 			x_old = x_new
			
# 			sol = [x_new,t_old]
# 			self.solution.append(sol)
# 	