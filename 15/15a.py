import sys
import heapq
sys.path.append("../intcode/")
icc = __import__("intcode_computer")

MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]
UNDO_MOVES = [None, 2, 1, 4, 3]


def explore(computer):
    grid = dict()
    grid[0, 0] = 1

    def aux(position):
        for move, (delta_x, delta_y) in enumerate(MOVES):
            new_position = position[0] + delta_x, position[1] + delta_y

            if new_position in grid:
                continue

            move += 1
            computer.append_input(move)
            outputs, _ = computer.run()
            status = outputs[0]

            grid[new_position] = status

            if status != 0:
                aux(new_position)

                computer.append_input(UNDO_MOVES[move])
                computer.run()

    aux((0, 0))
    return grid


def get_oxygen_pos(grid):
    for pos, field in grid.items():
        if field == 2:
            return pos


def astar(grid, start, target):
    def manhattan_dist(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    seen = set()
    seen.add(start)
    queue = [(manhattan_dist(start, target), 0, start)]

    while queue:
        _, steps, position = heapq.heappop(queue)

        for delta_x, delta_y in MOVES:
            new_position = position[0] + delta_x, position[1] + delta_y

            if new_position not in seen and grid[new_position] != 0:
                seen.add(new_position)
                new_steps = steps + 1

                if new_position == target:
                    return new_steps

                value = new_steps + manhattan_dist(new_position, target)
                heapq.heappush(queue, (value, new_steps, new_position))

    return None


def steps_to_oxygen(intcode):
    computer = icc.IntcodeComputer(intcode)
    grid = explore(computer)
    oxygen_pos = get_oxygen_pos(grid)
    return astar(grid, (0, 0), oxygen_pos)


if __name__ == "__main__":
    intcode = list(map(int, input().rstrip().split(",")))
    print(steps_to_oxygen(intcode))
