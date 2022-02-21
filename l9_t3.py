import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5, 5, 0.0001)

def diff(m, t):

	y, x = m
	dydt = x
	dxdt = np.sin(y) + np.cos(y)
	
	return dydt, dxdt

dy0dt = 0
y0 = 3

m0 = y0, dy0dt 

solve = odeint(diff, m0, t)
plt.plot(t, solve[:, 1])
plt.plot(t, solve[:, 0])
plt.show()