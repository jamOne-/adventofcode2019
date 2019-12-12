import re
import sys
from collections import namedtuple

Vector3D = namedtuple("Vector3D", "x y z")
ZERO_VECTOR = Vector3D(0, 0, 0)


class Moon:
    def __init__(self, position):
        self.position = position
        self.velocity = ZERO_VECTOR

    def add_velocity(self, vector):
        self.velocity = add_vectors(self.velocity, vector)

    def energy(self):
        return vector_length(self.position) * vector_length(self.velocity)

    def update_position(self):
        self.position = add_vectors(self.position, self.velocity)


def cmp(x, y):
    return (x > y) - (x < y)


def add_vectors(v1, v2):
    return Vector3D(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)


def vector_length(vector):
    return abs(vector.x) + abs(vector.y) + abs(vector.z)


def calculate_gravity(moon1, moon2):
    x1 = cmp(moon2.position.x, moon1.position.x)
    y1 = cmp(moon2.position.y, moon1.position.y)
    z1 = cmp(moon2.position.z, moon1.position.z)

    return Vector3D(x1, y1, z1), Vector3D(-x1, -y1, -z1)


def simulation(moons, steps):
    for step in range(steps):
        for i, moon in enumerate(moons):
            for moon2 in moons[i + 1:]:
                grav1, grav2 = calculate_gravity(moon, moon2)
                moon.add_velocity(grav1)
                moon2.add_velocity(grav2)

            moon.update_position()


def total_energy(moons):
    return sum(map(lambda moon: moon.energy(), moons))


if __name__ == "__main__":
    moons = []

    for line in sys.stdin:
        x, y, z = tuple(map(int, re.findall("-?\d+", line)))
        position = Vector3D(x, y, z)
        moon = Moon(position)
        moons.append(moon)

    simulation(moons, 1000)
    print(total_energy(moons))
