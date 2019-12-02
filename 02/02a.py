def run_program(ints):
    current = 0

    while ints[current] != 99:
        opcode, i1, i2, i3 = ints[current], ints[current +
                                                 1], ints[current + 2], ints[current + 3]

        if opcode == 1:
            ints[i3] = ints[i1] + ints[i2]
        else:
            ints[i3] = ints[i1] * ints[i2]

        current += 4


if __name__ == "__main__":
    program = input().rstrip()
    ints = list(map(int, program.split(",")))

    ints[1] = 12
    ints[2] = 2

    run_program(ints)
    print(ints[0])
