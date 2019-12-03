def closest_crossing(wire1points, wire2points):
    crossings = set(wire1points.keys()) & set(wire2points.keys())
    times = map(lambda point: wire1points[point]
                + wire2points[point], crossings)
    return min(times)


def path_to_points(path):
    current = 0, 0
    time = 1
    points = dict()

    for step in path:
        direction = step[0]
        steps = int(step[1:])

        if direction == "U":
            delta = 0, 1
        elif direction == "D":
            delta = 0, -1
        elif direction == "L":
            delta = -1, 0
        else:
            delta = 1, 0

        for _ in range(steps):
            current = current[0] + delta[0], current[1] + delta[1]

            if current not in points:
                points[current] = time

            time += 1

    return points


if __name__ == "__main__":
    path1, path2 = input().rstrip().split(","), input().rstrip().split(",")
    points1, points2 = path_to_points(path1), path_to_points(path2)

    print(closest_crossing(points1, points2))
