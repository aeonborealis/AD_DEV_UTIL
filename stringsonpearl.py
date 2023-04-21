import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Set up initial conditions
num_particles = 1000
x = np.zeros(num_particles)
y = np.zeros(num_particles)
z = np.zeros(num_particles)
vx = np.random.randn(num_particles)
vy = np.random.randn(num_particles)
vz = np.random.randn(num_particles)

# Set up branching probability
branch_prob = 0.01

# Set up time and step size
t = 0
dt = 0.01

# Initialize arrays for storing data
xs = np.zeros((num_particles, 1000))
ys = np.zeros((num_particles, 1000))
zs = np.zeros((num_particles, 1000))
times = np.zeros(1000)

# Run simulation
for i in range(1000):
    # Update positions
    x += vx * dt
    y += vy * dt
    z += vz * dt
    
    # Update velocities
    vx += np.random.randn(num_particles) * dt
    vy += np.random.randn(num_particles) * dt
    vz += np.random.randn(num_particles) * dt
    
    # Check if particles branch off into new universes
    for j in range(num_particles):
        if np.random.rand() < branch_prob:
            # Branch off into new universe with a new set of velocities
            vx[j] = np.random.randn()
            vy[j] = np.random.randn()
            vz[j] = np.random.randn()
    
    # Store positions and time for visualization
    xs[:, i] = x
    ys[:, i] = y
    zs[:, i] = z
    times[i] = t
    
    # Update time
    t += dt

# Plot 3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(num_particles):
    ax.plot(xs[i], ys[i], zs[i])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
