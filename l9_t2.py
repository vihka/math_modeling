import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.0001)

def diff(m, t):

	x, y = m
	
	dxdt = 3 * x - 2 * y + (np.exp(3 * t)) / (np.exp(t) + 1)
	dydt = x - (np.exp(3 * t)) / (np.exp(t) + 1)
	
	return dxdt, dydt

x0 = 5
y0 = -7

m0 = x0, y0

solve = odeint(diff, m0, t)
plt.plot(t, solve[:, 1])
plt.plot(t, solve[:, 0])
plt.show()