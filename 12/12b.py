import re
import sys
import math
from functools import reduce
from collections import namedtuple

Vector3D = namedtuple("Vector3D", "x y z")
ZERO_VECTOR = Vector3D(0, 0, 0)


class Moon:
    def __init__(self, position):
        self.position = position
        self.velocity = ZERO_VECTOR

    def add_velocity(self, vector):
        self.velocity = add_vectors(self.velocity, vector)

    def update_position(self):
        self.position = add_vectors(self.position, self.velocity)


def cmp(x, y):
    return (x > y) - (x < y)


def lcm(xs):
    return reduce(lambda x, y: x * y // math.gcd(x, y), xs)


def add_vectors(v1, v2):
    return Vector3D(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)


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


def find_axis_cycle(original_moons, axis):
    moons = [Moon(moon.position) for moon in original_moons]
    step = 0

    while True:
        simulation(moons, 1)
        step += 1

        if all(
            map(
                lambda moon, original_moon:
                    moon.position[axis] == original_moon.position[axis] and moon.velocity[axis] == original_moon.velocity[axis],
                moons,
                original_moons
            )
        ):
            break

    return step


if __name__ == "__main__":
    moons = []

    for line in sys.stdin:
        x, y, z = tuple(map(int, re.findall("-?\d+", line)))
        position = Vector3D(x, y, z)
        moon = Moon(position)
        moons.append(moon)

    cycles = [find_axis_cycle(moons, axis) for axis in range(3)]
    print(cycles)
    print(lcm(cycles))
