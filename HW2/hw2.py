#HW 2 ECE 4960 SPRING 2019
#TEJAS ADVAIT (TA275)

#PROB 1

from math import *
import matplotlib.pyplot as plt
def f1(x):
    return x**3 + 300.0*x

def f2(x):
    return x**3 + 300.0*x + 10**10

def df1(x,h,f):
    a = f(x+h) - f(x)
    return a/h

def df2(x,h,f):
    a = f(x+h) - f(x-h)
    return a/(2*h)

Gnd_truth = 600

rerrorsf11 = []
rerrorsf21 = []
rerrorsf12 = []
rerrorsf22 = []


logerrorsf11 = []
logerrorsf21 = []
logerrorsf12 = []
logerrorsf22 = []
H = []

fil1 = open("p1error.txt", "w")
fil2 = open("p1logerror.txt", "w")

header1 = "h" + ";" + "Error by Eq1 in f1" + ";" + "Error by Eq1 in f2" + ";" + "Error by Eq2 in f1" + ";" + "Error by Eq2 in f2" +"\n"
header2 = "h" + ";" + "Log Error by Eq1 in f1" + ";" + "Log Error by Eq1 in f2" + ";" + "Log Error by Eq2 in f1" + ";" + "Log Error by Eq2 in f2" +"\n"
fil1.write(header1)
fil2.write(header1)

for i in range(0,16):
    h = 10**(-1*i)
    H.append(-1*i)
    errf11 = (df1(10,h,f1) - Gnd_truth)/Gnd_truth
    errf21 = (df1(10,h,f2) - Gnd_truth)/Gnd_truth
    errf12 = (df2(10,h,f1) - Gnd_truth)/Gnd_truth
    errf22 = (df2(10,h,f2) - Gnd_truth)/Gnd_truth

    lerrf11 = log(fabs(errf11),10)
    lerrf21 = log(fabs(errf21),10)
    lerrf12 = log(fabs(errf12),10)
    lerrf22 = log(fabs(errf22),10)
    
    rerrorsf11.append(errf11)
    rerrorsf21.append(errf21)
    rerrorsf12.append(errf12)
    rerrorsf22.append(errf22)

    logerrorsf11.append(lerrf11)
    logerrorsf21.append(lerrf21)
    logerrorsf12.append(lerrf12)
    logerrorsf22.append(lerrf22)

    s1 = "10^-"+str(i)+";"+str(errf11)+";"+str(errf21)+";"+str(errf12)+";"+str(errf22)+"\n"
    s2 = "10^-"+str(i)+";"+str(lerrf11)+";"+str(lerrf21)+";"+str(lerrf12)+";"+str(lerrf22)+"\n"
    fil1.write(s1)
    fil2.write(s2)

fil1.close()
fil2.close()


plt.figure(1)
plt.plot(H,logerrorsf11, 'r--', label = "Log of relative error in " + r"$f'(x=10)$" + " by Eq. (1) with " + r"$f(x) = x^3 + 300x$")
plt.plot(H, logerrorsf21, 'b--', label = "Log of relative error in " + r"$f'(x=10)$" + " by Eq. (1) with " + r"$f(x) = x^3 + 300x + 10^{10}$")
plt.plot(H, logerrorsf12, 'g--', label = "Log of relative error in " + r"$f'(x=10)$" + " by Eq. (2) with " + r"$f(x) = x^3 + 300x$")
plt.plot(H,logerrorsf22, 'y--', label = "Log of relative error in " + r"$f'(x=10)$" + " by Eq. (2) with " + r"$f(x) = x^3 + 300x + 10^{10}$")
plt.ylabel(r'$log_{10}|error|$')
plt.xlabel(r'$log_{10}(h)$')
plt.title("log-log plot for Prob 1")
plt.legend()
plt.show()


#PROB 2
def f3(x):
    return x**3

def df3(x,h,f):
    return df1(x,h,f)

def df4(x,h,f):
    return df1(x,2*h,f)

def df5(x,h,f):
    a = (-0.5/h)*f(x+2*h)
    b = (-1.5/h)*f(x)
    c = (2/h)*f(x+h)
    return a+b+c

def rerr3(x,h,f,ground_truth):
    return (df3(x,h,f) - ground_truth)/ground_truth

def rerr4(x,h,f,ground_truth):
    return (df4(x,h,f)-ground_truth)/ground_truth

def rerr5(x,h,f,ground_truth):
    return (df5(x,h,f)-ground_truth)/ground_truth

def R6(x,h,f,ground_truth):
    try:
        return rerr4(x,h,f,ground_truth)/rerr3(x,h,f,ground_truth)
    except:
        nan

def R7(x,h,f):
    try:
        num = df3(x,4*h,f) - df3(x,2*h,f)
        den = df3(x,2*h,f) - df3(x,h,f)
        return num/den
    except:
        nan
rerrors3 = []
rerrors4 = []
rerrors5 = []
n6 = []
n7 = []
H2 = []

fil3 = open("p2table.txt", "w")
header3 = "h" + ";" + "Error by Eq1 in f3" + ";" + "Error by Eq4 in f3" + ";" + "Error by Eq5 in f3" + ";" + "n by Eq6" + ";" +"n by Eq7"+"\n"
fil3.write(header3)
for i in range (4, 41):
    H.append(-1*i)
    h = 2**(-1*i)
    rerrors3.append(rerr3(1,h,f3,3))
    rerrors4.append(rerr4(1,h,f3,3))
    rerrors5.append(rerr5(1,h,f3,3))
    n6.append(R6(1,h,f3,3))
    n7.append(R7(1,h,f3))

    s = "2^-"+str(i)+";"+str(rerrors3[i-4])+";"+str(rerrors4[i-4])+";"+str(rerrors5[i-4])+";"+str(n6[i-4])+";"+str(n7[i-4])+"\n"
    fil3.write(s)

fil3.close()






