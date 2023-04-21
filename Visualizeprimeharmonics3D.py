import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate primes using the code from before
# ...

# Create a 3D scatter plot of the primes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(primes, primes_harmonic, primes_analytic, c=primes, cmap='coolwarm')
ax.set_xlabel('Primes')
ax.set_ylabel('Prime Harmonics')
ax.set_zlabel('Analytic Continuation')

plt.show()
