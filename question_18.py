import numpy as np
import matplotlib.pyplot as plt
import math

def model(y, t):
    return t * y

# Exact Solution: y = e^t^2

t0 = 0
y0 = 1
h = 0.5
t_end = 2

t = np.arange(t0, t_end + h, h)

# True Solution
y_true = np.zeros(len(t))
y_true[0] = y0
for i in range(len(t)):
    y_true[i] = math.exp((t[i]**2)/2)

# Forward Euler
y_euler = np.zeros(len(t))
y_euler[0] = y0

for i in range(len(t) - 1):
    y_euler[i + 1] = y_euler[i] + h * model(y_euler[i], t[i])

# RK2
y_rk2 = np.zeros(len(t))
y_rk2[0] = y0

for i in range(len(t) - 1):
    k1 = h * model(y_rk2[i], t[i])
    k2 = h * model(y_rk2[i] + k1/2, t[i] + h/2)
    y_rk2[i + 1] = y_rk2[i] + k2

# RK4
y_rk4 = np.zeros(len(t))
y_rk4[0] = y0

for i in range(len(t) - 1):
    k1 = h * model(y_rk4[i], t[i])
    k2 = h * model(y_rk4[i] + 0.5 * k1, t[i] + 0.5 * h)
    k3 = h * model(y_rk4[i] + 0.5 * k2, t[i] + 0.5 * h)
    k4 = h * model(y_rk4[i] + k3, t[i] + h)
    y_rk4[i + 1] = y_rk4[i] + 1/6 * ( k1 + 2 * k2 + 2 * k3 + k4)

plt.figure(figsize=(10, 8))
plt.plot(t, y_euler, 'g.--', label = 'Forward Euler Approximation')
plt.plot(t, y_rk2, 'y.--', label = 'RK-2 Approximation')
plt.plot(t, y_rk4, 'r.--', label = 'RK-4 Approximation')
# Plot the true solution for comparison 
plt.plot(t, y_true, 'b-', label=r'Plot of $y = e^{t^{2}}$')
plt.xlabel('Time (t)')
plt.ylabel(r'$y(t)$')
plt.legend()
plt.grid(True)
plt.show()

# Error Calculation 
euler_error = np.zeros(len(t))
for i in range(len(t)):
    euler_error[i] = y_true[i] - y_euler[i]
    
rk2_error = np.zeros(len(t))
for i in range(len(t)):
    rk2_error[i] = y_true[i] - y_rk2[i]

rk4_error = np.zeros(len(t))
for i in range(len(t)):
    rk4_error[i] = y_true[i] - y_rk4[i]
    
# Plot the errors
plt.figure(figsize=(10, 8))
plt.plot(t, euler_error, 'g.--', label = 'Forward Euler Error')
plt.plot(t, rk2_error, 'y.--', label = 'RK-2 Error')
plt.plot(t, rk4_error, 'r.--', label = 'RK-4 Error')
plt.xlabel('Time (t)')
plt.ylabel(r'Error')
plt.legend()
plt.grid(True)
plt.show()

