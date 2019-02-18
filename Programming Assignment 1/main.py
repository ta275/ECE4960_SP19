#ECE 4960 Spring 2019
#Programming Assignment 1
#Author: Tejas Advait (ta275)
#Date of Creation: Feb 12 2019
#Last updated: Feb 18 2019


import integer_exception
import float_inf_ninf_nan
import float_under_over
import signed_zero
import spigot_pi
from common import *
import queue
import random


f = open("detailed_log.txt","w")
ieee = open("ieee_compliance_report.txt","w")

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

def dump_log(title, module):
	addsub(title,f)
	module.main()
	while (not result.empty()):
		a = result.get()
		if a[1]:
			iq.append(a[0])
			a = a[0] + "*****IEEE VIOLATION*****"
		else:
			a = a[0] + "\n"
		f.write(a)

def ieee_report(v):
	addsub("IEEE Compliance Report", ieee)
	ieee.write("***Total Number of Violations : {0} *** \n".format(len(v)))
	ieee.write("\n")
	ieee.write("10 Violations Reported Below. Look at the detailed log file for more details. \n")
	ieee.write("\n")
	v = random.sample(v,10)
	for i in range (0,10):
		ieee.write(str(i+1)+". "+v[i]+"\n")

dump_log("Integer Exception Handling", integer_exception)
dump_log("Floating-Point Overflow and Underflow", float_under_over)
dump_log("Floating-Point Operations of INF, NINF, and NAN", float_inf_ninf_nan)
dump_log("Signed-Zero Handling", signed_zero)
dump_log("Calculation of Pi", spigot_pi)
ieee_report(iq)
f.close()
ieee.close()