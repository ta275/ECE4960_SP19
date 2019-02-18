#ECE 4960 Spring 2019
#Programming Assignment 1
#Digits of Pi in Python 3.7.0
#Author: Tejas Advait (ta275)
#Date of Creation: Feb 12 2019
#Last updated: Feb 18 2019

#Based on "Unbounded Spigot Algorithms for the Digits of Pi" by Jeremy Gibbons
#The paper can be found at http://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf
from common import *

pi = "3.141592653589793238462643383279"

def make_pi(m):
        q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
        for i in range (0,m):
                if 4 * q + r - t < n * t:
                        yield n
                        q, r, t, k, n, l = 10*q, 10*(r-n*t), t, k, (10*(3*q+r))//t - 10*n, l
                else:
                        q, r, t, k, n, l = q*k, (2*q+r)*l, t*l, k+1, (q*(7*k+2)+r*l)//(t*l), l+2



def n_digits(n):
        digits = "3."
        l = 0
        for i in make_pi(n*5):

                if l != 0:
                        digits += str(i)
                l += 1
        return digits[:n+1]

def main():
        result.put(("First 31 digits of pi           : "+pi,False))
        result.put(("First 31 digits of pi calculated: "+n_digits(31),False))
