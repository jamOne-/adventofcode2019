import sys
sys.path.append("../intcode/")
icc = __import__("intcode_computer")

TILES = {
    "block": 2
}


def count_blocks(outputs):
    count = 0

    for tile in outputs[2::3]:
        if tile == TILES["block"]:
            count += 1

    return count


if __name__ == "__main__":
    intcode = list(map(int, input().rstrip().split(",")))
    intcode_computer = icc.IntcodeComputer(intcode)
    outputs, _ = intcode_computer.run()

    print(count_blocks(outputs))
