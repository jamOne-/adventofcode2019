import sys
from collections import defaultdict


def sum_depths(nodes):
    def aux(node, depth):
        total = depth

        for child in nodes[node]:
            total += aux(child, depth + 1)

        return total

    return aux("COM", 0)


if __name__ == "__main__":
    nodes = defaultdict(list)

    for line in sys.stdin:
        obj, orbiter = line.rstrip().split(")")
        nodes[obj].append(orbiter)

    print(sum_depths(nodes))
