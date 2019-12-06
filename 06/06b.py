import sys
from collections import defaultdict, deque


def distance(nodes, start, target):
    queue = deque()
    visited = dict()

    queue.append((start, 0, start))
    queue.append((target, 0, target))
    visited[start] = (0, start)
    visited[target] = (0, target)

    while queue:
        node, dist, path_id = queue.popleft()

        for neighbour in nodes[node]:
            if neighbour in visited:
                d, id2 = visited[neighbour]

                if path_id != id2:
                    return dist + 1 + d

            else:
                queue.append((neighbour, dist + 1, path_id))
                visited[neighbour] = (dist + 1, path_id)


if __name__ == "__main__":
    nodes = defaultdict(list)

    for line in sys.stdin:
        obj, orbiter = line.rstrip().split(")")
        nodes[obj].append(orbiter)
        nodes[orbiter].append(obj)

    print(distance(nodes, "YOU", "SAN") - 2)
