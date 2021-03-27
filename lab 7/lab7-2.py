import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint


N = 777
x0 = 1

t0 = 0
tmax = 30
dt = 0.1

t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)

def k(t):
    return 0.000067


def p(t):
    return 0.38


def f(x, t):
    return (k(t) + p(t)*x)*(N-x)


yf = odeint(f, x0, t)


plt.figure(figsize=(10, 10))
plt.plot(t, yf, 'r', label='S(t)')
plt.show()
