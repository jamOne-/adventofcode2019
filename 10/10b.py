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


def transform_angle(angle):
    return (angle + math.pi / 2) % (2 * math.pi)


def get_200th_evaporated(grid, asteroids, station):
    angles = defaultdict(list)
    for asteroid in asteroids:
        angle = get_angle(station, asteroid)
        distance = math.sqrt((station[0] - asteroid[0]) ** 2 +
                             (station[1] - asteroid[1]) ** 2)

        heap = angles[angle]
        heapq.heappush(heap, (distance, asteroid))

    count = 0
    while angles:
        for angle in sorted(angles.keys(), key=transform_angle):
            heap = angles[angle]
            evaporated = heapq.heappop(heap)
            count += 1

            if count == 200:
                return evaporated[1]

            if len(heap) == 0:
                del angles[angle]


if __name__ == "__main__":
    grid = [line.rstrip() for line in sys.stdin]
    asteroids = extract_asteroids(grid)
    count, best_asteroid = find_best_asteroid(grid, asteroids)
    print("best: {}, count: {}".format(best_asteroid, count))

    asteroids.remove(best_asteroid)
    x, y = get_200th_evaporated(grid, asteroids, best_asteroid)

    print(x * 100 + y)
