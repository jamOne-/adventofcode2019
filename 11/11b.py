import sys
from collections import defaultdict
sys.path.append("../intcode/")
icc = __import__("intcode_computer")


def move(position, direction):
    if direction == 0:
        delta = 0, 1
    elif direction == 1:
        delta = 1, 0
    elif direction == 2:
        delta = 0, -1
    else:
        delta = -1, 0

    return position[0] + delta[0], position[1] + delta[1]


def paint_some(intcode):
    fields = defaultdict(lambda: 1)
    painted = set()
    computer = icc.IntcodeComputer(intcode)
    current_pos = 0, 0
    direction = 0

    while True:
        field = fields[current_pos]
        computer.append_input(field)

        outputs, state = computer.run()
        if state == "STOPPED":
            break

        color, rotation = outputs
        fields[current_pos] = color
        painted.add(current_pos)

        direction = (direction + rotation * 2 - 1) % 4
        current_pos = move(current_pos, direction)

    return painted, fields


def print_indentifier(painted, fields):
    xs = list(map(lambda pos: pos[0], painted))
    ys = list(map(lambda pos: pos[1], painted))
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            field = fields[x, y]
            char = "#" if field == 1 else " "

            print(char, end="")

        print("")


if __name__ == "__main__":
    intcode = list(map(int, input().rstrip().split(",")))
    painted, fields = paint_some(intcode)
    print_indentifier(painted, fields)
