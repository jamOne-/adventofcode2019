import sys
sys.path.append("../intcode/")
icc = __import__("intcode_computer")


if __name__ == "__main__":
    intcode_file = open("25.in")
    intcode = list(map(int, intcode_file.readline().rstrip().split(",")))
    intcode_file.close()

    computer = icc.IntcodeComputer(intcode)

    while True:
        outputs, state = computer.run()
        print("".join(map(chr, outputs)))

        if state == "STOPPED":
            break

        instruction = input("instruction: ")
        computer.extend_input(map(ord, instruction + "\n"))
