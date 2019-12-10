import sys
import math
import heapq
from collections import defaultdict


def extract_asteroids(grid):
    asteroids = []

    for y, row in enumerate(grid):
        for x, field in enumerate(row):
            if field == "#":
                asteroids.append((x, y))

    return asteroids


def get_angle(p1, p2):
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])


def find_best_asteroid(grid, asteroids):
    best = -math.inf, None

    for asteroid in asteroids:
        angles = set()

        for asteroid2 in asteroids:
            if asteroid == asteroid2:
                continue

            angle = get_angle(asteroid, asteroid2)
            angles.add(angle)

        best = max(best, (len(angles), asteroid))

    return best


if __name__ == "__main__":
    grid = [line.rstrip() for line in sys.stdin]
    asteroids = extract_asteroids(grid)
    count, best_asteroid = find_best_asteroid(grid, asteroids)
    print("best: {}, count: {}".format(best_asteroid, count))
