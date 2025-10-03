import numpy as np
import matplotlib.pyplot as plt

def solution(t, y0, t0):
    """
    Calculates the solution y(t) for the initial value problem.

    The differetial equation is y' = (2/t) * y
    The initial condition is y(t0) = y0
    The solution is y(t) = (y0 / t0^2) * t^2
    
    Args:
    t: An array of time values.
    y0: The initial value of y at time t0.
    t0: The initial time.

    Returns:
    An array of y values corresponding to the t values.
    """
    # The original equation is undefined at t=0, and so t0 cannot be 0.
    if t0 == 0:
        raise ValueError("t0 cannot be zero.")
    
    # Calculate the constant C from the Initial Condition
    C = y0/(t0**2)

    return C * t**2

# --- Define plotting parameters ---

# Set the initial time. We can choose any non-zero value. (t0 != 0)
t0 = 1.0 

# Create a range of time values for our plot.
# The interval of existence is (0, infinity) since t0 > 0.
# We'll plot a segment of this interval.
t_values = np.linspace(0.1, 4, 500)

# A list of different initial y-values to plot
y0_values = [-3, -1.5, 1, 2.5, 4]

# --- Generate the plot ---

# Create a figure and axis for the plot
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 7))

# Plot the solution for each different value of y0
for y0 in y0_values:
  y_values = solution(t_values, y0, t0)
  ax.plot(t_values, y_values, label=f'$y_0 = {y0}$')

# --- Customize the plot ---

# Set titles and labels for clarity
ax.set_title(f'Solutions to $y\' = (2/t)y$ with $t_0={t0}$', fontsize=16)
ax.set_xlabel('t', fontsize=12)
ax.set_ylabel('y(t)', fontsize=12)

# Add a legend to identify the different lines
ax.legend(title='Initial Value ($y_0$)', fontsize=10)

# Set the limits for the axes to make the plot easy to read
ax.set_ylim(-20, 50)
ax.set_xlim(0, 4)

# Add horizontal and vertical lines at 0 for reference
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# Display the plot
plt.show()