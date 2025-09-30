import numpy as np
import matplotlib.pyplot as plt

# Define the ODE function: dy/dt = y
def model(y, t):
    return y

# Initial conditions and parameters
t0 = 0
y0 = 1
h = 0.1
t_end = 2

# Create arrays for time and solution
t = np.arange(t0, t_end + h, h)
y_rk2 = np.zeros(len(t))
y_rk2[0] = y0

# The RK2 (Midpoint Method) calculation loop
for i in range(len(t) - 1):
    # Calculate k1 slope (slope at the start)
    k1 = h * model(y_rk2[i], t[i])

    # Calculate k2 slope (slope at the midpoint)
    k2 = h * model(y_rk2[i] + 0.5 * k1, t[i] + 0.5 * h)

    # Calculate the next y value
    y_rk2[i + 1] = y_rk2[i] + k2

plt.figure(figsize=(10, 8))
plt.plot(t, y_rk2, 'r.--', label = 'RK-2 Approximation')
# Plot the true solution for comparison 
plt.plot(t, np.exp(t), 'b-', label='True Solution (e^t)')
plt.xlabel('Time (t)')
plt.ylabel(r'$y(t)$')
plt.legend()
plt.grid(True)
plt.show()