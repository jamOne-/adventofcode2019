import sys
sys.path.append("../intcode/")
icc = __import__("intcode_computer")


if __name__ == "__main__":
    intcode = list(map(int, input().rstrip().split(",")))
    computer = icc.IntcodeComputer(intcode)
    computer.append_input(2)

    outputs, _ = computer.run()
    print(" ".join(map(str, outputs)))
