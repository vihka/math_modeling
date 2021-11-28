import numpy as np
import math
N = 4
M = 5
arr = np.zeros((N, M))
for (i, j), value in np.ndenumerate(arr):
  result = math.sin(N*(i+1) + M*(j+1))
  if (result < 0):
    result = 0
  arr[i, j] = result
print(arr)