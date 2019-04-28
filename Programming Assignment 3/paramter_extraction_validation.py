"""
ECE 4960 SPRING 2019
Programming Assignment 3
Parameter Extraction Validation
Author: Tejas Advait (TA275)
"""

import numpy as np
from opes import OPES
from s_model import S_model


#Verification for a linear model.
def linear(x,a):
	return a[0]*x[0] + a[1]


p_est = np.array([0,0],dtype = np.float64)
tol = np.float64(10**-7)
step = np.float64(10**-5)
p = np.array([109,51],dtype = np.float64)
num_sample = 100
Linear = S_model(1,2,linear,p)
D1 = Linear.gen_sample(num_sample,noise = False)
D2 = Linear.gen_sample(num_sample,noise = True)


O_linear1 = OPES(Linear,D1,p_est,tol,step)
# print (O_linear1.extractParam())
# print (O_linear1.max_iter)
assert(np.linalg.norm(O_linear1.extractParam() - p) < 1e-3)

O_linear2 = OPES(Linear,D2,p_est,tol,step)
# print (O_linear2.extractParam())
# print (O_linear2.max_iter)
assert(np.linalg.norm(O_linear2.extractParam() - p) < 20)


"""
Verification for an exponential model is highly sensitive to the initial 
estimate of the parameters.
"""

def power(x,a):
	return a[0]*(x[0]**a[1])


p_est = np.array([5,0.5],dtype = np.float64)
tol = np.float64(10**-7)
step = np.float64(10**-6)
p = np.array([5,0.5],dtype = np.float64)
num_sample = 100

Power = S_model(1,2,power,p)
D1 = Power.gen_sample(num_sample,noise = False)
D2 = Power.gen_sample(num_sample,noise = True)

O_power1 = OPES(Power,D1,p_est,tol,step)

# print (O_power1.extractParam())
# print (O_power1.max_iter)
if O_power1.extractParam().size == 0:
	print ("Parameter search failed for O_power1")
else:
	assert(np.linalg.norm(O_power1.extractParam() - p) < 10)

O_power2 = OPES(Power,D2,p_est,tol,step)

# print (O_power2.extractParam())
# print (O_power2.max_iter)
if O_power2.extractParam().size == 0:
	print ("Parameter search failed for O_power2")
else:
	assert(np.linalg.norm(O_power1.extractParam() - p) < 100)
