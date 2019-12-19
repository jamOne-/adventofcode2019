import sys
sys.path.append("../intcode/")
icc = __import__("intcode_computer")


def scan_position(intcode, position):
    computer = icc.IntcodeComputer(intcode)
    computer.extend_input(position)
    outputs, _ = computer.run()
    output = outputs[0]

    return output


def find_last_x_in_row(intcode, row, beg=0, end=None):
    if end == None:
        end = row

    while beg <= end:
        mid = (beg + end) // 2

        if scan_position(intcode, (mid, row)) == 0:
            left_x = find_last_x_in_row(intcode, row, beg, mid - 1)

            if scan_position(intcode, (left_x, row)) == 1:
                return left_x
            else:
                return find_last_x_in_row(intcode, row, mid + 1, end)
        else:
            beg = mid + 1

    return end


def find_rectangle(intcode):
    y = 1000

    while True:
        x = find_last_x_in_row(intcode, y)

        if scan_position(intcode, (x - 99, y)) == 1 and scan_position(intcode, (x - 99, y + 99)) == 1:
            break
        else:
            y *= 2

    min_y, max_y = y // 2, y

    while min_y <= max_y:
        y = (min_y + max_y) // 2
        x = find_last_x_in_row(intcode, y)

        if scan_position(intcode, (x - 99, y)) == 1 and scan_position(intcode, (x - 99, y + 99)) == 1:
            max_y = y - 1
        else:
            min_y = y + 1

    x = find_last_x_in_row(intcode, min_y) - 99
    return x, min_y


if __name__ == "__main__":
    intcode = list(map(int, input().rstrip().split(",")))
    x, y = find_rectangle(intcode)
    print(x, y)
    print(x * 10000 + y)
