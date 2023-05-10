import numpy as np

class Body:
    def __init__(self, pos, vel, mass):
        self.pos = pos
        self.vel = vel
        self.mass = mass

class Node:
    def __init__(self, mass, pos, size):
        self.mass = mass
        self.pos = pos
        self.size = size
        self.children = None
        self.body = None

def insert(node, body):
    if node.body is None:
        node.body = body
        return

    if node.children is None:
        node.children = [Node(node.mass, node.pos - 0.25 * node.size, 0.5 * node.size),
                         Node(node.mass, node.pos - np.array([node.size[0]/4, -node.size[1]/4]), 0.5 * node.size),
                         Node(node.mass, node.pos - np.array([-node.size[0]/4, node.size[1]/4]), 0.5 * node.size),
                         Node(node.mass, node.pos + 0.25 * node.size, 0.5 * node.size)]

    i = 0
    if body.pos[0] > node.pos[0]:
        i += 1
    if body.pos[1] > node.pos[1]:
        i += 2

    insert(node.children[i], body)

    node.mass += body.mass

def build_tree(bodies, pos_min, pos_max):
    size = pos_max - pos_min
    pos = pos_min + 0.5 * size
    node = Node(0, pos, size)

    for body in bodies:
        insert(node, body)

    return node

def calc_force(node, body, theta):
    s = node.size / np.sqrt(np.sum((node.pos - body.pos)**2))

    if node.children is None:
        if node.body is not body:
            force = node.mass * body.mass * (node.pos - body.pos) / np.sum((node.pos - body.pos)**2)
            return force
        else:
            return np.zeros(2)

    if s < theta:
        force = node.mass * body.mass * (node.pos - body.pos) / np.sum((node.pos - body.pos)**2)
        return force
    else:
        force = np.zeros(2)
        for child in node.children:
            force += calc_force(child, body, theta)
        return force

def step(bodies, dt, theta):
    nodes = build_tree(bodies, np.min([body.pos for body in bodies], axis=0),
                       np.max([body.pos for body in bodies], axis=0))

    for body in bodies:
        force = calc_force(nodes, body, theta)
        body.vel += force * dt / body.mass
        body.pos += body.vel * dt

def simulate(num_bodies, dt, steps):
    bodies = [Body(np.random.randn(2), np.zeros(2), 1) for _ in range(num_bodies)]

    for i in range(steps):
        step(bodies, dt, 0.5)

    return bodies
