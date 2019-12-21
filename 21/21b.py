import sys
sys.path.append("../intcode/")
icc = __import__("intcode_computer")


if __name__ == "__main__":
    intcode = list(map(int, input().rstrip().split(",")))
    computer = icc.IntcodeComputer(intcode)

    instructions = [
        "NOT T T",
        "AND A T",
        "AND B T",
        "AND C T",
        "NOT T T",
        "AND D T",
        "AND H T",
        "NOT A J",
        "OR T J",
        "RUN"
    ]

    for instruction in instructions:
        computer.extend_input(map(ord, instruction + "\n"))

    outputs, _ = computer.run()
    print("".join(map(chr, outputs[:-1])))
    print(outputs[-1])
