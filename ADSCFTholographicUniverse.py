import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define constants
R = 1  # radius of AdS space
L = 1  # AdS curvature scale

# Define coordinates
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)
theta, phi = np.meshgrid(theta, phi)
x = R*np.sin(theta)*np.cos(phi)
y = R*np.sin(theta)*np.sin(phi)
z = R*np.cos(theta)

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot AdS space
ax.plot_surface(x, y, z, color='blue', alpha=0.1)

# Define coordinates for CFT circle
t = np.linspace(0, 2*np.pi, 100)
xc = L*np.cos(t)
yc = L*np.sin(t)
zc = 0

# Plot CFT circle
ax.plot(xc, yc, zc, color='red', linewidth=2)

# Set axis limits and labels
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Show plot
plt.show()
