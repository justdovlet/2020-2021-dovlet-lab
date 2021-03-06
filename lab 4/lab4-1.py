import numpy as np
import math
import matplotlib.pyplot as plt

from scipy.integrate import odeint

w = 8
g = 0.00

t0 = 0
tmax = 45
dt = 0.05

t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)


def p(t):
    #return (math.sin(t*0.5))
    return 0


def syst(x, t):
    return x[1], -w * w * x[0] - g * x[1] - p(t)


v0 = (-1, 0)

yf = odeint(syst, v0, t)

x = []
y = []

for i in range(len(yf)):
    x.append(yf[i][0])
    y.append(yf[i][1])

plt.figure(figsize=(10, 10))
plt.plot(x, y, 'r', label='x')
plt.show()
