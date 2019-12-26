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
    fields = defaultdict(int)
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

    return painted


if __name__ == "__main__":
    intcode = list(map(int, input().rstrip().split(",")))
    painted = paint_some(intcode)

    print(len(painted))
