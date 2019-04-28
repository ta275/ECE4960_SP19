"""
ECE 4960 SPRING 2019
Programming Assignment 3
S_model Test
Author: Tejas Advait (TA275)
"""
from helper_test import *
import numpy as np
from s_model import S_model

tol = 10e-10

#Five S functions for testing
def S0(x,a):
	return a[0]*x[0] + a[1]*x[1] + x[2]

def S1(x,a):
	return a[0]*x[0] + a[2]*x[1] + 5*(x[2]**a[1])

def S2(x,a):
	return a[0]*x[0] + a[1]*x[1] + 5*(x[2]**a[3])

def S3(x,a):
	return a[1]*np.exp(x[0]) + a[0] - x[1] + a[2]**x[2]

def S4(x,a):
	return a[0]*(x[0]**a[1])

def S5(x,a):
	Is = a[0]
	kap = a[1]
	Vth = a[2]
	Vgs = x[0]
	Vds = x[1]
	Vt = np.float64(26*10-3)
	Id = Is*(np.log(1 + np.exp((kap*(Vgs-Vth))/(2*Vt))))**2 \
	- Is*(np.log(1 + np.exp((kap*(Vgs-Vth) - Vds)/(2*Vt))))**2
	return Id

#Five paramters for five models
P0 = np.random.rand(2)*10
P1 = np.random.rand(3)*13
P2 = np.random.rand(4)*12
P3 = np.random.rand(3)*112
P4 = np.random.rand(2)*11
P5 = np.random.rand(3)*7

#Instantiating five models from the S functions
M0 = S_model(3,2,S0,P0)
M1 = S_model(3,3,S1,P1)
M2 = S_model(3,4,S2,P2)
M3 = S_model(3,3,S3,P3)
M4 = S_model(1,2,S4,P4)
M5 = S_model(2,3,S5,P5)

#evaluate_multiple test
num_sample = 10000
X0 = np.random.rand(num_sample,3)*7
X1 = np.random.rand(num_sample,3)*5
X2 = np.random.rand(num_sample,3)*8
X3 = np.random.rand(num_sample,3)*17
X4 = np.random.rand(num_sample,1)*13
X5 = np.random.rand(num_sample,2)*10


Y0 = M0.evaluate_multiple(X0)
Y1 = M1.evaluate_multiple(X1)
Y2 = M2.evaluate_multiple(X2)
Y3 = M3.evaluate_multiple(X3)
Y4 = M4.evaluate_multiple(X4)
Y5 = M5.evaluate_multiple(X5)

YC0 = np.zeros((num_sample,1))
YC1 = np.zeros((num_sample,1))
YC2 = np.zeros((num_sample,1))
YC3 = np.zeros((num_sample,1))
YC4 = np.zeros((num_sample,1))
YC5 = np.zeros((num_sample,1))

for i in range(num_sample):
	y0 = S0(X0[i],P0)
	y1 = S1(X1[i],P1)
	y2 = S2(X2[i],P2)
	y3 = S3(X3[i],P3)
	y4 = S4(X4[i],P4)
	y5 = S5(X5[i],P5)
	YC0[i,0] = y0
	YC1[i,0] = y1
	YC2[i,0] = y2
	YC3[i,0] = y3
	YC4[i,0] = y4
	YC5[i,0] = y5

assert (np.linalg.norm(Y0-YC0)<tol)
assert (np.linalg.norm(Y1-YC1)<tol)
assert (np.linalg.norm(Y2-YC2)<tol)
assert (np.linalg.norm(Y3-YC3)<tol)
assert (np.linalg.norm(Y4-YC4)<tol)
assert (np.linalg.norm(Y5-YC5)<tol)

#gen_sample test (without noise)
D0 = M0.gen_sample(num_sample,noise = False)
D1 = M1.gen_sample(num_sample,noise = False)
D2 = M2.gen_sample(num_sample,noise = False)
D3 = M3.gen_sample(num_sample,noise = False)
D4 = M4.gen_sample(num_sample,noise = False)
D5 = M5.gen_sample(num_sample,noise = False)
YC0 = np.zeros((num_sample,1))
YC1 = np.zeros((num_sample,1))
YC2 = np.zeros((num_sample,1))
YC3 = np.zeros((num_sample,1))
YC4 = np.zeros((num_sample,1))
YC5 = np.zeros((num_sample,1))
for i in range(num_sample):
	y0 = S0(D0[i,:-1],P0)
	y1 = S1(D1[i,:-1],P1)
	y2 = S2(D2[i,:-1],P2)
	y3 = S3(D3[i,:-1],P3)
	y4 = S4(D4[i,:-1],P4)
	y5 = S5(D5[i,:-1],P5)
	YC0[i,0] = y0
	YC1[i,0] = y1
	YC2[i,0] = y2
	YC3[i,0] = y3
	YC4[i,0] = y4
	YC5[i,0] = y5

assert (np.linalg.norm(D0[:,-1:]-YC0)<tol)
assert (np.linalg.norm(D1[:,-1:]-YC1)<tol)
assert (np.linalg.norm(D2[:,-1:]-YC2)<tol)
assert (np.linalg.norm(D3[:,-1:]-YC3)<tol)
assert (np.linalg.norm(D4[:,-1:]-YC4)<tol)
assert (np.linalg.norm(D5[:,-1:]-YC5)<tol)

#gen_sample test (with noise)
D0 = M0.gen_sample(num_sample,noise = True)
D1 = M1.gen_sample(num_sample,noise = True)
D2 = M2.gen_sample(num_sample,noise = True)
D3 = M3.gen_sample(num_sample,noise = True)
D4 = M4.gen_sample(num_sample,noise = True)
D5 = M5.gen_sample(num_sample,noise = True)
Y0 = D0[:,-1:]
Y1 = D1[:,-1:]
Y2 = D2[:,-1:]
Y3 = D3[:,-1:]
Y4 = D4[:,-1:]
Y5 = D5[:,-1:]

YC0 = np.zeros((num_sample,1))
YC1 = np.zeros((num_sample,1))
YC2 = np.zeros((num_sample,1))
YC3 = np.zeros((num_sample,1))
YC4 = np.zeros((num_sample,1))
YC5 = np.zeros((num_sample,1))
for i in range(num_sample):
	y0 = S0(D0[i,:-1],P0)
	y1 = S1(D1[i,:-1],P1)
	y2 = S2(D2[i,:-1],P2)
	y3 = S3(D3[i,:-1],P3)
	y4 = S4(D4[i,:-1],P4)
	y5 = S5(D5[i,:-1],P5)
	YC0[i,0] = y0
	YC1[i,0] = y1
	YC2[i,0] = y2
	YC3[i,0] = y3
	YC4[i,0] = y4
	YC5[i,0] = y5

R0 = np.divide(abs(Y0-YC0),YC0)
R1 = np.divide(abs(Y1-YC1),YC1)
R2 = np.divide(abs(Y2-YC2),YC2)
R3 = np.divide(abs(Y3-YC3),YC3)
R4 = np.divide(abs(Y4-YC4),YC4)
R5 = np.divide(abs(Y5-YC5),YC5)
CL = np.ones((num_sample,1))*0.1
CU = np.ones((num_sample,1))*0.2

R0 = np.logical_and(R0 >= CL, R0 <= CU)
R1 = np.logical_and(R1 >= CL, R1 <= CU)
R2 = np.logical_and(R2 >= CL, R2 <= CU)
R3 = np.logical_and(R3 >= CL, R3 <= CU)
R4 = np.logical_and(R4 >= CL, R4 <= CU)
R5 = np.logical_and(R5 >= CL, R5 <= CU)

assert (np.all(R0,axis = 0)[0])
assert (np.all(R1,axis = 0)[0])
assert (np.all(R2,axis = 0)[0])
assert (np.all(R3,axis = 0)[0])
assert (np.all(R4,axis = 0)[0])
assert (np.all(R5,axis = 0)[0])

print ("All tests passed. Testing of S_model complete.")