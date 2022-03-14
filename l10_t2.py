import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

a = 100
k1 = 0.3
k2 = 0.23
x = 0
y = 0
frames = 60
t = np.linspace(0, 5, frames)
z = x, y
def f(z, t):
    x, y = z
    dxdt = (a - x - y) * k1
    dydt = (a - x - y) * k2
    return dxdt, dydt


sol = odeint(f, z, t)

def solve_func(i, key):
    if key == 'point':
        xg = sol[i, 0]
        yg = sol[i, 1]
    else:
        xg = sol[:i, 0]
        yg = sol[:i, 1]
    return xg, yg

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([],[], '-', color='blue')
plt.plot(t, sol[:,0])
plt.plot(t, sol[:,1])
'''
def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))
ani = FuncAnimation(fig,
                   animate,
                   frames=frames,
                   interval=30)
edge = 100
ax.set_xlim(-edge, edge)
ax.set_ylim(0, edge)'''

plt.show()