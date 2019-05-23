import pickle
import numpy as np
from quasi_newton_min import QNM

file1 = open("Measurement Files/outputNMOS.bin", "rb")
outputNMOS = pickle.load(file1)
file1.close()

def Id_ekv(x,a):
	Is = a[0]
	kap = a[1]
	Vth = a[2]
	Vgs = x[0]
	Vds = x[1]
	Vt = np.float64(26e-3)
	Id = Is*(np.log(1 + np.exp(kap*(Vgs-Vth)/(2*Vt))))**2 \
	- Is*(np.log(1 + np.exp((kap*(Vgs-Vth) - Vds)/(2*Vt))))**2
	return Id

p1*Power((Ln(1+Exp(p2*(x1-p3)/0.052))),2) - p1*(Power(Ln(1+Exp((p2*(x1-p3)-x2)/0.052),2)))

Is = 3e-8
kap = 0.5
Vth = 1
p = np.array([Is,kap,Vth])
v = 0
def V(param):
	v = np.float64(0)
	for i in outputNMOS:
		Ids = i[2]
		Idekv = Id_ekv(i[:-1],param)

		v+= (Idekv/Ids - 1)**2
	return v
Q = QNM(V, 3, p, 1e-14)
pe = Q.extractParam()
import matplotlib.pyplot as plt
outputNMOS2 = np.zeros_like(outputNMOS)

for i in range(outputNMOS.shape[0]):
	outputNMOS2[i,-1] = Id_ekv(outputNMOS[i,:-1],pe)
	outputNMOS2[i,:-1] = outputNMOS[i,:-1]

VgsN = np.unique(outputNMOS[:,0])
figN = plt.figure()
plt.title(r"$I_{D}$ vs $V_{DS}$ for NMOS")
for i in VgsN:
	sub = outputNMOS2[outputNMOS2[:,0] == i]
	y = sub[:,2].flatten()
	x = sub[:,1].flatten()
	plt.plot(x,y, label = r"$V_{GS}$ = " + str(i))

plt.xlabel(r"$V_{DS}$ (V)")
plt.ylabel(r"$I_{D}$ (A)")
plt.legend()
plt.show()
# for i in outputNMOS:
# 	Ids = i[2]
# 	Idekv = Id_ekv(i[:-1],p)
# 	# Idekv = Id_ekv([i[0],i[1]],p)
# 	# print (Idekv, Id_ekv([i[0],i[1]],p))
# 	print ("Vgs: {0}, Vds: {1}, Ids: {2}, Id_ekv: {3}".format(i[0],i[1],Ids,Idekv))
# 	v+= (Ids-Idekv)**2
# print (v)