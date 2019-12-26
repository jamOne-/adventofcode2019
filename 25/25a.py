import sys
sys.path.append("../intcode/")
icc = __import__("intcode_computer")


if __name__ == "__main__":
    intcode = list(map(int, input().rstrip().split(",")))
    computer = icc.IntcodeComputer(intcode)
    state = None

    while state != "STOPPED":
        outputs, state = computer.run()
        print("".join(map(chr, outputs)))
        instruction = input("instruction: ")
        computer.extend_input(map(ord, instruction + "\n"))
