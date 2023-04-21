import random

# set up initial conditions
particles = [{'x': random.uniform(0, 1), 'y': random.uniform(0, 1), 'z': random.uniform(0, 1)}]
time = 0

# simulate branching universes
while time < 100:
    for particle in particles:
        # calculate new position for particle
        particle['x'] += random.uniform(-0.1, 0.1)
        particle['y'] += random.uniform(-0.1, 0.1)
        particle['z'] += random.uniform(-0.1, 0.1)

        # check if particle should branch into new universe
        if random.random() < 0.01:
            new_particle = {'x': particle['x'], 'y': particle['y'], 'z': particle['z']}
            particles.append(new_particle)

    time += 1

# output final particle positions
for particle in particles:
    print(f"x: {particle['x']}, y: {particle['y']}, z: {particle['z']}")
