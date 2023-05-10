def run_simulation():
    # Define constants
    G = 6.674e-11  # Gravitational constant
    c = 2.998e8  # Speed of light

    # Define simulation parameters
    num_particles = 1000  # Number of particles to simulate
    sim_time = 3600  # Length of simulation in seconds
    time_step = 1  # Time step for simulation in seconds

    # Define initial conditions
    positions = np.random.uniform(-1e9, 1e9, (num_particles, 3))  # Random positions
    velocities = np.zeros((num_particles, 3))  # Zero initial velocities
    masses = np.random.uniform(1e10, 1e15, num_particles)  # Random masses

    # Initialize simulation
    time = 0
    while time < sim_time:
        # Compute pairwise gravitational forces
        accelerations = np.zeros((num_particles, 3))
        for i in range(num_particles):
            for j in range(i + 1, num_particles):
                r = np.linalg.norm(positions[i] - positions[j])
                f = G * masses[i] * masses[j] / r**2
                a = f / masses[i]
                accelerations[i] += a * (positions[j] - positions[i]) / r
                accelerations[j] -= a * (positions[j] - positions[i]) / r

        # Update velocities and positions
        velocities += accelerations * time_step
        positions += velocities * time_step

        # Advance time
        time += time_step

    # Output final positions and velocities
    print("Final positions:")
    print(positions)
    print("Final velocities:")
    print(velocities)

if __name__ == "__main__":
    run_simulation()
