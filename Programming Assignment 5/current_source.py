"""
ECE 4960 SPRING 2019
Programming Assignment 5
Current Sources
Author: Tejas Advait (TA275)
"""
import numpy as np
def large_signal(t):
	"""
	Large Signal Transient as shown in figure 6.
	Unit of t is s.
	Returned current is in A.
	"""
	t = t*1e9
	
	if t < 0:
		raise Exception("t cannot be less than 0.")
	else:
		r = t%20
		if r <= 1:
			return 3e-4*r

		if 1<r and r <= 10:
			return 3e-4

		if 10<r and r <= 11:
			return -1e-4*r + 11e-4

		return 0

def Id_ekv(x,Is,kap,Vth):
	Vgs = x[0,0]
	Vds = x[1,0]
	Vt = 26e-3
	Id = Is*(np.log(1 + np.exp(kap*(Vgs-Vth)/(2*Vt))))**2 \
	- Is*(np.log(1 + np.exp((kap*(Vgs-Vth) - Vds)/(2*Vt))))**2
	return Id

# def AC_Current


#Uncomment the following lines to see the plot of the transient large signal
# from matplotlib import pyplot as plt
# t = 0
# T = []
# I = []

# while t <= 100e-9:
# 	T.append(t)
# 	I.append(large_signal(t))
# 	t += 0.2e-9

# fig = plt.figure()

# plt.plot(T,I)
# plt.show()
