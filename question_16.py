import numpy as np
import matplotlib.pyplot as plt
import math

def model(y, t):
    return (math.exp(t) + math.pow(t, 4) + math.sin(t)) * t

t0 = 0
y0 = 1
h = 0.1
t_end = 2

t = np.arange(t0, t_end + h, h)
y_rk2 = np.zeros(len(t))
y_rk2[0] = y0

for i in range(len(t) - 1):
    k1 = h * model(y_rk2[i], t[i])
    k2 = h * model(y_rk2[i] + k1/2, t[i] + h/2)
    y_rk2[i + 1] = y_rk2[i] + k2

plt.figure(figsize=(10, 8))
plt.plot(t, y_rk2, 'r.--', label = 'RK-2 Approximation')
plt.xlabel('Time (t)')
plt.ylabel(r'$y(t)$')
plt.legend()
plt.grid(True)
plt.show()