import numpy as np
import matplotlib.pyplot as plt



# dy/dt = y, y(t) = e^t
def model(y, t):
    return y

# Initial conditions
t0 = 0
y0 = 1

# Parameters 
h = 0.001 # Step size
t_end = 2 # End Time

# Create an array to store time steps
# We use np.arange to create a sequence of numbers from t0 to t_end with a step of h
t = np.arange(t0, t_end + h, h)
print(t)

# Create an empty array to store the solution y
y = np.zeros(len(t))
y[0] = y0 # The first value is our initial condition

# The Euler method calculation loop 
for i in range(len(t) - 1): # The loop runs up to len(t) - 1 because inside the loop, we calculate y[i + 1]. If we went all the way to the end, we'd try to calculate a value that is outside the array, causing an error.
    y[i + 1] = y[i] + h * model(y[i], t[i])

# Plotting the results 
plt.figure(figsize=(8, 6)) 

# Plot the Euler method approximation 
plt.plot(t, y, 'r.--', label='Euler Method Approximation')

# Plot the true solution for comparison 
plt.plot(t, np.exp(t), 'b-', label='True Solution (e^t)')

# Add labels and a title for clarity
plt.xlabel('Time (t)')
plt.ylabel(r'$y(t)$')
plt.title('Euler method Approximation vs. True Solution')
plt.legend() # Show the legend
plt.grid(True) # Add a grid
plt.show() # Display the plot