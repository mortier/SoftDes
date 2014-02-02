# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:49:50 2014

@author: dmichael
"""
x = 800.2
if type(x)==int and 0<= x <=100:
    print "Hello"
elif type(x)==int and 100 < x < 500:
    print "Goodbye"
elif type(x)==int and 600 <= x <=1000:
    print "Ciao"