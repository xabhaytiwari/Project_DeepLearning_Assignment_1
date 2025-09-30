import numpy as np
import matplotlib.pyplot as plt

def model(y, t):
    return (t**2 + 1) * y 

t0 = 0
y0 = 1
h = 0.1
t_end = 2

t = np.arange(t0, t_end + h, h)
y_rk4 = np.zeros(len(t))
y_rk4[0] = y0

for i in range(len(t) - 1):
    k1 = h * model(y_rk4[i], t[i])
    k2 = h * model(y_rk4[i] + 0.5 * k1, t[i] + 0.5 * h)
    k3 = h * model(y_rk4[i] + 0.5 * k2, t[i] + 0.5 * h)
    k4 = h * model(y_rk4[i] + k3, t[i] + h)
    y_rk4[i + 1] = y_rk4[i] + 1/6 * ( k1 + 2 * k2 + 2 * k3 + k4)

plt.figure(figsize=(10, 8))
plt.plot(t, y_rk4, 'r.--', label = 'RK-4 Approximation')
# Plot the true solution for comparison 
plt.xlabel('Time (t)')
plt.ylabel(r'$y(t)$')
plt.legend()
plt.grid(True)
plt.show()