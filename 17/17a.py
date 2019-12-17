import sys
sys.path.append("../intcode/")
icc = __import__("intcode_computer")


def get_grid_and_position(intcode):
    computer = icc.IntcodeComputer(intcode)
    outputs, _ = computer.run()

    grid = [[]]
    position, direction = None, None

    for output in outputs:
        if output == 10:
            grid.append([])
        else:
            char = chr(output)

            if char == "#" or char == ".":
                grid[-1].append(char)
            else:
                position = len(grid[-1]), len(grid)
                direction = char
                grid[-1].append("#")

    while not len(grid[-1]):
        grid.pop()

    return grid, position, direction


def find_intersections(grid):
    rows = len(grid)
    cols = len(grid[0])

    for y in range(1, rows - 1):
        for x in range(1, cols - 1):
            if grid[y][x] == "#" and grid[y - 1][x] == "#" and grid[y + 1][x] == "#" and grid[y][x - 1] == "#" and grid[y][x + 1] == "#":
                yield y, x


if __name__ == "__main__":
    intcode = list(map(int, input().rstrip().split(",")))
    grid, position, direction = get_grid_and_position(intcode)

    alignments = map(
        lambda intersection: intersection[0] * intersection[1], find_intersections(grid))
    total = sum(alignments)

    print(total)
