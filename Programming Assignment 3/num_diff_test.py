"""
ECE 4960 SPRING 2019
Programming Assignment 3
Numerical Differentiation Test
Author: Tejas Advait (TA275)
"""
import numpy as np
from num_diff import *

def f(x):
	return x[0] + x[1]**3 + 4*x[0]*x[2] + 2*x[2]

def f_1(x):
	return 1 + 4*x[2]

def f_2(x):
	return 3*x[1]**2

def f_3(x):
	return 4*x[0] + 2

def f_11(x):
	return np.float64(0)

def f_12(x):
	return np.float64(0)

def f_13(x):
	return np.float(4)

def f_21(x):
	return f_12(x)

def f_22(x):
	return 6*x[1]

def f_23(x):
	return np.float64(0)

def f_31(x):
	return f_13(x)

def f_32(x):
	return f_23(x)

def f_33(x):
	return np.float(0)

num = 10
tol = 10**-1

X = np.array(np.random.randint(1,20,(num,3)), dtype = np.float64)

# F_1 = np.zeros((num,3))
# F_1 = np.zeros((num,3))
# F_1 = np.zeros((num,3))
# F_1 = np.zeros((num,3))
# F_1 = np.zeros((num,3))
# F_1 = np.zeros((num,3))
# F_1 = np.zeros((num,3))
# F_1 = np.zeros((num,3))
# F_1 = np.zeros((num,3))

for i in range (num):
	# for k in range(3):
	# 	print(k)
	# 	assert(abs(f_1(X[i]) - fd_diff1(f, X[i], k)) < tol)
	# 	assert(abs(f_1(X[i]) - bd_diff1(f, X[i], k)) < tol)
	# 	assert(abs(f_1(X[i]) - cd_diff1(f, X[i], k)) < tol)

	# print(f_2(X[i]))
	# print(fd_diff1(f, X[i], 1))
	
	assert(abs(f_1(X[i]) - fd_diff1(f, X[i], 0)) < tol)
	assert(abs(f_2(X[i]) - fd_diff1(f, X[i], 1)) < tol)

	assert(abs(f_3(X[i]) - fd_diff1(f, X[i], 2)) < tol)

	assert(abs(f_1(X[i]) - bd_diff1(f, X[i], 0)) < tol)
	assert(abs(f_2(X[i]) - bd_diff1(f, X[i], 1)) < tol)
	assert(abs(f_3(X[i]) - bd_diff1(f, X[i], 2)) < tol)

	assert(abs(f_1(X[i]) - cd_diff1(f, X[i], 0)) < tol)
	assert(abs(f_2(X[i]) - cd_diff1(f, X[i], 1)) < tol)
	assert(abs(f_3(X[i]) - cd_diff1(f, X[i], 2)) < tol)


for i in range(num):

	# print(f_11(X[i]), fd_diff2(f, X[i], 0, 0))
	# print(f_12(X[i]), fd_diff2(f, X[i], 0, 1))
	# print(f_13(X[i]), fd_diff2(f, X[i], 0, 2))

	# assert(abs(f_11(X[i]) - fd_diff2(f, X[i], 0, 0)) < tol)
	# assert(abs(f_12(X[i]) - fd_diff2(f, X[i], 0, 1)) < tol)
	# assert(abs(f_13(X[i]) - fd_diff2(f, X[i], 0, 2)) < tol)



	# assert(abs(f_11(X[i]) - bd_diff2(f, X[i], 0, 0)) < tol)
	# assert(abs(f_12(X[i]) - bd_diff2(f, X[i], 0, 1)) < tol)
	# assert(abs(f_13(X[i]) - bd_diff2(f, X[i], 0, 2)) < tol)

	assert(abs(f_11(X[i]) - cd_diff2(f, X[i], 0, 0)) < tol)
	assert(abs(f_12(X[i]) - cd_diff2(f, X[i], 0, 1)) < tol)
	assert(abs(f_13(X[i]) - cd_diff2(f, X[i], 0, 2)) < tol)


for i in range(num):
	# assert(abs(f_21(X[i]) - fd_diff2(f, X[i], 1, 0)) < tol)
	# assert(abs(f_22(X[i]) - fd_diff2(f, X[i], 1, 1)) < tol)
	# assert(abs(f_23(X[i]) - fd_diff2(f, X[i], 1, 2)) < tol)

	# assert(abs(f_21(X[i]) - bd_diff2(f, X[i], 1, 0)) < tol)
	# assert(abs(f_22(X[i]) - bd_diff2(f, X[i], 1, 1)) < tol)
	# assert(abs(f_23(X[i]) - bd_diff2(f, X[i], 1, 2)) < tol)

	assert(abs(f_21(X[i]) - cd_diff2(f, X[i], 1, 0)) < tol)
	assert(abs(f_22(X[i]) - cd_diff2(f, X[i], 1, 1)) < tol)
	assert(abs(f_23(X[i]) - cd_diff2(f, X[i], 1, 2)) < tol)


for i in range (num):
	# assert(abs(f_31(X[i]) - fd_diff2(f, X[i], 2, 0)) < tol)
	# assert(abs(f_32(X[i]) - fd_diff2(f, X[i], 2, 1)) < tol)
	# assert(abs(f_33(X[i]) - fd_diff2(f, X[i], 2, 2)) < tol)

	# assert(abs(f_31(X[i]) - bd_diff2(f, X[i], 2, 0)) < tol)
	# assert(abs(f_32(X[i]) - bd_diff2(f, X[i], 2, 1)) < tol)
	# assert(abs(f_33(X[i]) - bd_diff2(f, X[i], 2, 2)) < tol)

	assert(abs(f_31(X[i]) - cd_diff2(f, X[i], 2, 0)) < tol)
	assert(abs(f_32(X[i]) - cd_diff2(f, X[i], 2, 1)) < tol)
	assert(abs(f_33(X[i]) - cd_diff2(f, X[i], 2, 2)) < tol)