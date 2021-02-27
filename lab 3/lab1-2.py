import numpy as np
import pandas as pd
import scipy as sp
import math
import matplotlib.pyplot as plt

from scipy.integrate import odeint

x0 = 50000
y0 = 69000
t0 = 0

a = 0.12
b = 0.51
c = 0.30
h = 0.61

tmax = 5
dt = 0.05

t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)

def p(t):
    return (math.sin(t*20))

def q(t):
    return (math.cos(t*13))

def syst(f,t):
    x = f[0]
    y = f[1]
    dxdt = -a*x - b*y + p(t)
    dydt = -c*x*y - h*y + q(t)
    return (dxdt,dydt)

v0 = (x0, y0)

yf = odeint(syst, v0, t)

x = []
y = []

for i in range(len(yf)):

    x.append(yf[i][0])
    y.append(yf[i][1])



zero = []
for i in range (len(t)):
    zero = np.append(zero,0)


plt.figure(figsize = (20, 15))
plt.plot(t, zero, 'b')
plt.plot(t, x, 'r', label = 'x')
plt.plot(t, y, 'g', label = 'y')
print (y)
plt.ylabel('Численность армии')
plt.xlabel('Время')
plt.title('Модель боевых действий №1')
plt.legend(loc ='upper right')


plt.show()
