import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.0001)

def diff(m, x):

	y, z = m
	
	dydx = y ** 2 * z
	dzdx = (z / x) - y * z ** 2
	
	return dydx, dzdx

y0 = 1
z0 = -3

m0 = y0, z0

solve = odeint(diff, m0, x)
plt.plot(x, solve[:, 1])
plt.plot(x, solve[:, 0])
plt.show()