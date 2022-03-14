import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

g = 9.81
m = 0.5
frames = 60
t = np.linspace(0, 5, frames)

v = 20
F = 0.1
M = F / (m * v)
k = F / (m * v ** 2)

def telo(z, t):
    v, y = z    
    dvdt_y = -g - M * v
    dydt = v
    
    return dvdt_y, dydt


def telo2(z1, t):
    v, y = z1
    dvdt_y = -g - k * v ** 2
    dydt = v
    
    return dvdt_y, dydt

v = 20
y0 = 0
z = v, y0
z1 = v, y0

x = np.zeros((frames, ))

sol = odeint(telo, z, t)
#sol1 = odeint(telo2, z1, t)
def solve_func(i, key):
    if key == 'point':
        xg = x[i]
        yg = sol[i, 1]
    else:
        xg = x[:i]
        yg = sol[:i, 1]
    return xg, yg

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([],[], '-', color='blue')

def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))
ani = FuncAnimation(fig,
                   animate,
                   frames=frames,
                   interval=30)
edge = 40
ax.set_xlim(-edge, edge)
ax.set_ylim(0, edge)

plt.show()