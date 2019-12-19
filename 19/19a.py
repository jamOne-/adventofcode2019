import sys
sys.path.append("../intcode/")
icc = __import__("intcode_computer")


def scan_area(intcode):
    grid = []
    for y in range(50):
        row = []

        for x in range(50):
            computer = icc.IntcodeComputer(intcode)
            computer.extend_input([x, y])
            outputs, _ = computer.run()
            output = outputs[0]
            row.append(output)

        grid.append(row)

    return grid


def calculate_affected_fields(grid):
    count = 0

    for y in range(50):
        for x in range(50):
            if grid[y][x] == 1:
                count += 1

    return count


def print_area(grid):
    for y in range(50):
        for x in range(50):
            char = "." if grid[y][x] == 0 else "#"
            print(char, end="")

        print("")


if __name__ == "__main__":
    intcode = list(map(int, input().rstrip().split(",")))
    grid = scan_area(intcode)
    print(calculate_affected_fields(grid))
    print_area(grid)
