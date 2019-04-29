"""
ECE 4960 SPRING 2019
Programming Assignment 4
Current Sources
Author: Tejas Advait (TA275)
"""

def large_signal(t):
	"""
	Large Signal Transient as shown in figure 6.
	Unit of t is ns.
	Returned current is in A.
	"""
	if t < 0:
		raise Exception("t cannot be less than 0.")
	else:
		r = t%20
		if r <= 1:
			return 1e-4*r

		if 1<r and r <= 10:
			return 1e-4

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

# t = 0
# T = []
# I = []

# while t <= 100:
# 	T.append(t)
# 	I.append(large_signal(t))
# 	t += 0.2

# fig = plt.figure()

# plt.plot(T,I)
# plt.show()
