import numpy as np
import matplotlib.pyplot as plt

# Define the function to be continued
def f(z):
    return np.exp(z)

# Set up the initial plot
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])

# Define the start and end points for the analytic continuation
start = 0
end = 2 * np.pi

# Define the step size for the analytic continuation
step = 0.1

# Define the imaginary part of the starting point
imag_start = 0

# Define the number of points to plot
num_points = int((end - start) / step)

# Generate a list of points for the analytic continuation
points = np.linspace(start, end, num_points)

# Initialize the list of values for the analytic continuation
values = [f(complex(point, imag_start)) for point in points]

# Plot the initial values
ax.plot(np.real(values), np.imag(values), color='blue')

# Perform the analytic continuation
for i in range(1, int(imag_start / step) + 1):
    imag_part = i * step
    new_values = [f(complex(point, imag_part)) for point in points]
    values += new_values
    ax.plot(np.real(new_values), np.imag(new_values), color='blue')

# Plot the final result of the analytic continuation
ax.plot(np.real(values), np.imag(values), color='red')

# Display the plot
plt.show()
