import sys
sys.path.append("../intcode/")
icc = __import__("intcode_computer")


def print_grid(intcode):
    computer = icc.IntcodeComputer(intcode)
    outputs, _ = computer.run()
    print("".join(map(chr, outputs)))


def collect_dust(intcode):
    # solved by hand...
    main_routine = "A,A,B,B,C,B,C,B,C,A"
    A = "L,10,L,10,R,6"
    B = "R,12,L,12,L,12"
    C = "L,6,L,10,R,12,R,12"
    video_feed = "n"

    intcode = list(intcode)
    intcode[0] = 2
    computer = icc.IntcodeComputer(intcode)

    for input_line in [main_routine, A, B, C, video_feed]:
        input_line += "\n"
        computer.extend_input(map(ord, input_line))

    outputs, _ = computer.run()
    return outputs[-1]


if __name__ == "__main__":
    intcode = list(map(int, input().rstrip().split(",")))
    # print_grid(intcode)
    print(collect_dust(intcode))
