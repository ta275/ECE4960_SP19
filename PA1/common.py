"""
 * common.py
 *
 * Date Created: 12-Feb-2019
 * Author : Tejas Advait (ta275)
 *
 * Description: Common functions to be used by other scripts
 """

import math
import queue
result = queue.Queue()
ninf = float('-inf')
inf = float('inf')
nan = float('nan')

def apply_2arg(a,b,f,name):
	r = []
	d = []

	desc = "%f "+ name + " %f"
	d.append(desc%(a,a))
	d.append(desc%(b,b))
	d.append(desc%(a,b))
	d.append(desc%(b,a))


	try:
		r.append(f(a,a))
	except Exception as e:
		r.append(e)

	try:
		r.append(f(b,b))
	except Exception as e:
		r.append(e)

	try:
		r.append(f(a,b))
	except Exception as e:
		r.append(e)
	
	try:
		r.append(f(b,a))
	except Exception as e:
		r.append(e)

	return (r,d)

def apply_1arg(a,f,name):
	desc = name + "(%f)"%a

	try:
		r = f(a)
	except Exception as e:
		r = e

	return (r,desc)

	

def basic_ops(a,b):
	r = []
	d = []
	r1,d1 =apply_2arg(a,b,(lambda c,d : c+d), "+" )
	r.extend(r1)
	d.extend(d1)
	r1,d1 =apply_2arg(a,b,(lambda c,d : c-d), "-" )
	r.extend(r1)
	d.extend(d1)
	r1,d1 =apply_2arg(a,b,(lambda c,d : c*d), "*" )
	r.extend(r1)
	d.extend(d1)
	r1,d1 =apply_2arg(a,b,(lambda c,d : c/d), "/" )
	r.extend(r1)
	d.extend(d1)
	return (r,d)




def single_ops(a):
	r = []
	d = []
	r1,d1 = apply_1arg(a, (lambda x : 1.0/x), "1/")
	r.append(r1)
	d.append(d1)
	r1,d1 = apply_1arg(a, math.sin, "sin")
	r.append(r1)
	d.append(d1)
	r1,d1 = apply_1arg(a, math.exp, "exp")
	r.append(r1)
	d.append(d1)
	r1,d1 = apply_1arg(a, math.log, "log")
	r.append(r1)
	d.append(d1)
	return (r,d)

def add_to_result(calc, r,exp):
	a = "Result of " + calc + " : " + str(r)
	
	if math.isnan(exp):
		try:
			if math.isnan(r):
				result.put((a,False))
		except:
			result.put((a,True))
	else:
		if r == exp:
			result.put((a,False))
		else:
			result.put((a,True))

def add_to_result_list(calc,r,exp):
	for i in range (0, len(calc)):
		add_to_result(calc[i],r[i],exp[i])

def basic_ops_result(a,b,exp):
	r,d = basic_ops(a,b)
	add_to_result_list(d,r,exp)

def single_ops_result(a,exp):
	r,d = single_ops(a)
	add_to_result_list(d,r,exp)
