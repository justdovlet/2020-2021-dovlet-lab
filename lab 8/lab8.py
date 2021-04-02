import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint

p_cr = 20
tau1 = 10
p1 = 9
tau2 = 16
p2 = 7
V = 10
q = 1

a1 = p_cr / (tau1 * tau1 * p1 * p1 * V * q)
a2 = p_cr / (tau2 * tau2 * p2 * p2 * V * q)
b = p_cr / (tau1 * tau1 * tau2 * tau2 * p1 * p1 * p2 * p2 * V * q)
c1 = (p_cr - p1) / (tau1 * p1)
c2 = (p_cr - p1) / (tau2 * p2)

t0 = 0
tmax = 30
dt = 0.01

t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)
v0 = [2, 1]


def f(x, t):
    dx1 = (c1 / c1) * x[0] - (a1 / c1) * x[0] * x[0] - (b / c1) * x[0] * x[1]
    dx2 = (c2 / c1) * x[1] - (a2 / c1) * x[1] * x[1] - (b / c1) * x[0] * x[1]
    return dx1, dx2


yf = odeint(f, v0, t)

plt.figure(figsize=(10, 10))
plt.plot(t, yf)
plt.show()
