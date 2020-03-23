"""
 * main.py
 *
 * Date Created: 12-Feb-2019
 * Author : Tejas Advait (ta275)
 *
 * Description: Generate compliance reports for Python 3.7
 """


import integer_exception
import float_inf_ninf_nan
import float_under_over
import signed_zero
import spigot_pi
from common import *
import queue
import random
import os


f = open(os.path.join("reports", "detailed_log.txt"),"w")
ieee = open(os.path.join("reports","ieee_compliance_report.txt"), "w")
p = open(os.path.join("reports", "digits_of_pi.txt") ,"w")

iq = []

def addsub(title,fl):
	temp = queue.Queue()
	page_break = "################################################################################"
	temp.put("")
	temp.put(page_break)
	temp.put(title)
	temp.put(page_break)
	temp.put("")
	while (not temp.empty()):
		a = temp.get() + "\n"
		fl.write(a)

def dump_log(title, module,fl):
	addsub(title,fl)
	module.main()
	while (not result.empty()):
		a = result.get()
		if a[1]:
			iq.append(a[0])
			a = a[0] + "   *****IEEE VIOLATION*****" +"\n"
		else:
			a = a[0] + "\n"
		fl.write(a)

def ieee_report(v):
	addsub("IEEE Compliance Report", ieee)
	ieee.write("***Total Number of Violations : {0} *** \n".format(len(v)))
	ieee.write("\n")
	ieee.write("10 Violations Reported Below. Look at the detailed log file for more details. \n")
	ieee.write("\n")
	v = random.sample(v,10)
	for i in range (0,10):
		ieee.write(str(i+1)+". "+v[i]+"\n")

dump_log("Integer Exception Handling", integer_exception,f)
dump_log("Floating-Point Overflow and Underflow", float_under_over,f)
dump_log("Floating-Point Operations of INF, NINF, and NAN", float_inf_ninf_nan,f)
dump_log("Signed-Zero Handling", signed_zero,f)
dump_log("Calculation of Pi", spigot_pi,p)
ieee_report(iq)
f.close()
ieee.close()
p.close()
