import heapq
import sys
from collections import deque


def find_start_and_keys(grid):
    rows, cols = len(grid), len(grid[0])
    keys_count = 0

    for y in range(rows):
        for x in range(cols):
            if 'a' <= grid[y][x] <= 'z':
                keys_count += 1
            elif grid[y][x] == "@":
                position = x, y
                row = grid[y]
                new_row = row[:x] + "." + row[x + 1:]

    return position, keys_count, grid


def change_grid_to_part_b(grid, position):
    x, y = position
    positions = (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)

    grid[y - 1] = grid[y - 1][:x - 1] + ".#." + grid[y-1][x + 2:]
    grid[y] = grid[y][:x - 1] + "###" + grid[y][x + 2:]
    grid[y + 1] = grid[y + 1][:x - 1] + ".#." + grid[y + 1][x + 2:]

    return positions, grid


def find_reachable_keys(grid, position, keys):
    rows, cols = len(grid), len(grid[0])
    visited = set([position])
    queue = deque([(position, 0)])

    while queue:
        position, steps = queue.popleft()

        for x_delta, y_delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = position[0] + x_delta, position[1] + y_delta
            new_position = x, y
            new_steps = steps + 1

            if not(0 <= x < cols and 0 <= y < rows):
                continue

            field = grid[y][x]

            if field == "#" or ("A" <= field <= "Z" and field.lower() not in keys):
                continue

            if new_position not in visited:
                visited.add(new_position)

                if 'a' <= field <= 'z' and field not in keys:
                    yield new_position, new_steps, field
                else:
                    queue.append((new_position, new_steps))


def find_shortest_path_length(grid, positions, keys_count):
    rows, cols = len(grid), len(grid[0])
    visited = set([])
    queue = [(0, positions, frozenset())]

    while queue:
        steps, positions, keys = heapq.heappop(queue)

        if (positions, keys) in visited:
            continue

        if len(keys) == keys_count:
            return steps

        visited.add((positions, keys))

        for position_i, position in enumerate(positions):
            for key_position, key_distance, key in find_reachable_keys(grid, position, keys):
                new_keys = keys.union([key])
                new_steps = steps + key_distance
                new_positions = positions[:position_i] + \
                    (key_position, ) + positions[position_i + 1:]

                if (new_positions, new_keys) not in visited:
                    heapq.heappush(queue, (new_steps, new_positions, new_keys))


if __name__ == "__main__":
    grid = [line.rstrip() for line in sys.stdin]
    position, keys_count, grid = find_start_and_keys(grid)
    positions, grid = change_grid_to_part_b(grid, position)
    print(find_shortest_path_length(grid, positions, keys_count))
