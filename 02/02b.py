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

    for noun in range(100):
        for verb in range(100):
            new_ints = list(ints)
            new_ints[1] = noun
            new_ints[2] = verb

            run_program(new_ints)

            if new_ints[0] == 19690720:
                print(
                    "Found! noun={}, verb={}, 100*noun+verb={}".format(noun, verb, 100*noun+verb))
                break
