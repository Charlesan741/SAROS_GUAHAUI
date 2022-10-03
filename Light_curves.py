# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 00:13:54 2022

@author: nicor
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
import random

x = np.arange(0, 15, 0.2)
phase=0
p=5
pi=math.pi
plt.plot(x, 0.418*(np.sin(2*pi*x/(p)+phase-20.76))+0.1419*np.sin(2*(2*pi*x/(p)+phase)-63.76)+0.0664*np.sin(3*(2*pi*x/(p)+phase)-91.57)+0.0354*np.sin(4*(2*pi*x/(p)+phase)-112.62)+0.020*np.sin(5*(2*pi*x/p+phase)-129.46),'r--', label='Cepheid')

plt.xlabel('TIme')
plt.ylabel('Apparent Brightness')

plt.title("Light Curve")
plt.legend()
plt.show()

#======================
phase1=0
p1=5
u=np.arange(0,20,0.2)
plt.plot(u,0.25*np.sin(2*pi*u/p1+phase1),'m--',label='Scuti')

plt.xlabel('TIme')
plt.ylabel('Apparent Brightness')

plt.title("Light Curve")
plt.legend()
plt.show()
#=======================
f=random.random()

t= np.arange(0,15,0.2)
phase2=0
p2=5
plt.plot(t,(-0.5*np.cos(2*(pi*t/p2+phase2))*(1-f*np.cos(pi*t/p2+phase2)))/(1+f/2),'g--',label='ACV')

plt.xlabel('TIme')
plt.ylabel('Apparent Brightness')

plt.title("Light Curve")
plt.legend()
plt.grid()
plt.show()


#======================== Exoplanet model ====
def df(r1,r2):
    if r1>r2:
        return print('The radius of the star must be greater than the radius of the planet')
    else:
        return (r1/r2)**2
    