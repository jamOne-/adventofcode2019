import sys
import heapq
from collections import defaultdict, deque


class Portal:
    def __init__(self, id, position, is_outer):
        self.id = id
        self.position = position
        self.is_outer = is_outer
        self.warps_to = None


def find_closest_portal(maze, point):
    deltas = None

    for x_delta, y_delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = point[0] + x_delta, point[1] + y_delta

        if "A" <= maze[y][x] <= "Z":
            deltas = x_delta, y_delta

    if deltas == None:
        return None

    portal_name = ""
    x, y = point

    for _ in range(2):
        x += deltas[0]
        y += deltas[1]

        portal_name += maze[y][x]

    if deltas[0] < 0 or deltas[1] < 0:
        portal_name = portal_name[::-1]

    return portal_name


def find_portals(maze):
    rows, cols = len(maze), len(maze[0])
    portals = dict()
    point_to_portal = dict()

    for y in range(rows):
        for x in range(cols):
            if maze[y][x] == ".":
                point = x, y
                portal_name = find_closest_portal(maze, point)

                if portal_name != None:
                    portal_id = portal_name if portal_name not in portals else portal_name + "'"
                    is_outer = x == 2 or x == cols - 3 or y == 2 or y == rows - 3
                    portal = Portal(portal_id, point, is_outer)

                    if portal_name in portals:
                        warps_to = portals[portal_name]
                        portal.warps_to = warps_to
                        warps_to.warps_to = portal

                    portals[portal_id] = portal
                    point_to_portal[point] = portal

    return portals, point_to_portal


def find_portal_connections(maze, portals, point_to_portal):
    connections = defaultdict(list)

    for portal_id, portal in portals.items():
        visited = set([portal.position])
        queue = deque([(portal.position, 0)])

        while queue:
            position, steps = queue.popleft()
            new_steps = steps + 1

            for x_delta, y_delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = position[0] + x_delta, position[1] + y_delta
                new_position = x, y

                if new_position not in visited and maze[y][x] == ".":
                    visited.add(new_position)

                    if new_position in point_to_portal:
                        portal2 = point_to_portal[new_position]
                        connections[portal_id].append((portal2, new_steps))
                    else:
                        queue.append((new_position, new_steps))

    return connections


def find_path_to_ZZ(maze, connections):
    visited = set()
    queue = [(0, "AA", 0)]

    while queue:
        steps, portal_id, level = heapq.heappop(queue)

        if (portal_id, level) in visited:
            continue

        if portal_id == "ZZ":
            return steps

        visited.add((portal_id, level))

        for portal, distance in connections[portal_id]:
            new_steps = steps + distance + 1

            if portal.id == "ZZ":
                if level == 0:
                    heapq.heappush(
                        queue, (new_steps - 1, portal.id, level))

                continue

            if portal.id == "AA" or portal.is_outer and level == 0:
                continue

            new_level = level - 1 if portal.is_outer else level + 1
            new_portal_id = portal.warps_to.id

            if (new_portal_id, new_level) not in visited:
                heapq.heappush(queue, (new_steps, new_portal_id, new_level))


if __name__ == "__main__":
    maze = list(line[:-1] for line in sys.stdin)
    portals, point_to_portal = find_portals(maze)
    connections = find_portal_connections(maze, portals, point_to_portal)
    print(find_path_to_ZZ(maze, connections))
