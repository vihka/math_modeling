import numpy as np
import math as mt
import matplotlib.pyplot as plt

phi0 = 0.01
phi1 = 8 * np.pi
N = int(input('введи как минимум 1000: '))
amogus = int(input('пожалуйста введите: 1 для логарифмической спирали 2 для арихмедовой спирали 3 для спирали жезл 4 для розы '))
phi = np.linspace(phi0 , phi1, N)

b = 0.02
if amogus == 1:
  r = np.exp(b*phi)
elif amogus == 2:
  k = float(input('введите число: '))
  r = k * phi
elif amogus == 3:
  k = float(input('введите число: '))
  r = k / np.sqrt(phi)
elif amogus == 4:
  k = float(input('введите число(пж не вводи отрицательное): '))
  k = abs(k)
  r = np.sin(k * phi)

x = []
y = []

for i in range(N):
  x.append(r[i]*np.cos(phi[i]))
  y.append(r[i]*np.sin(phi[i]))

plt.plot(x,y)
plt.show()