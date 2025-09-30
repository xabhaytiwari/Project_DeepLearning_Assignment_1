import numpy as np
import matplotlib.pyplot as plt

def model(y, t):
    return y * t

t0 = 0
y0 = 1

h = 0.1
t_end = 2

t = np.arange(t0, t_end + h, h)
y = np.zeros(len(t))

y[0] = y0 

for i in range(len(t) - 1):
    y[i + 1] = y[i] + h * model(y[i], t[i])
print(y)

plt.figure(figsize=(8, 6))
plt.plot(t, y, 'r.--', label='Euler Approximation')
plt.xlabel(r'Time ($t$)')
plt.ylabel(r'$y(t)$')
plt.title('Euler method Approximation')
plt.legend()
plt.grid(True)
plt.show()