import sys
sys.path.append("../intcode/")
icc = __import__("intcode_computer")


if __name__ == "__main__":
    intcode = list(map(int, input().rstrip().split(",")))
    computer = icc.IntcodeComputer(intcode)

    instructions = [
        "NOT C T",
        "AND D T",
        "NOT A J",
        "OR T J",
        "WALK"
    ]

    for instruction in instructions:
        computer.extend_input(map(ord, instruction + "\n"))

    outputs, _ = computer.run()
    print("".join(map(chr, outputs[:-1])))
    print(outputs[-1])
