# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:25:46 2014

@author: dmichael
"""

def hypotenuse(a,b):
    from math import *
    c=sqrt(a**2+b**2)
    print c

def right_justify(x):
    y=len(x)
    print (70-y)*" "+x
    
def do_twice(f,arg):
    f(arg)
    f(arg)
    
def mmmspam():
    print "I love SPAM"