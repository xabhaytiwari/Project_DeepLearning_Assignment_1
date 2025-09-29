import numpy as np
import matplotlib.pyplot as plt

def model(y, t):
    return 2 * t

t0 = 0
y0 = 1

h = 0.5
t_end = 0.5

t = np.arange(t0, t_end + h, h)

y = np.zeros(len(t))
y[0] = y0

for i in range(len(t) - 1):
    y[i + 1] = y[i] + h * model(y[i], t[i])

print(y)
