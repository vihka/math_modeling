import numpy as np
time_start = 0
time_stop = 5
x0 = 10
y0 = 6
v0x = 2
v0y = 15
steps = 10
coords = np.zeros((steps, 3))
for t in np.linspace(time_start, time_stop, steps):
  x = x0 + v0x*t
  y = y0 + v0y*t - (g*t**2)/2
  coords[current_step, 0] = t
  coords[current_step, 1] = x
  coords[current_step, 2] = y
  current_step += 1
print(coords)