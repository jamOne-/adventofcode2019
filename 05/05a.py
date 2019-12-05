def extract_opcode_and_modes(instruction):
    opcode = instruction % 100
    instruction //= 100
    modes = []

    for _ in range(3):
        modes.append(instruction % 10)
        instruction //= 10

    return opcode, modes


def read_with_mode(ints, pos, mode):
    if mode == 0:
        return ints[pos]
    else:
        return pos


def add(ints, inputs, current, modes):
    p1, p2, p3 = ints[current:current + 3]
    a = read_with_mode(ints, p1, modes[0])
    b = read_with_mode(ints, p2, modes[1])

    ints[p3] = a + b
    return current + 3


def multiply(ints, inputs, current, modes):
    p1, p2, p3 = ints[current:current + 3]
    a = read_with_mode(ints, p1, modes[0])
    b = read_with_mode(ints, p2, modes[1])

    ints[p3] = a * b
    return current + 3


def read_input(ints, inputs, current, modes):
    position = ints[current]
    ints[position] = inputs.pop()
    return current + 1


def print_value(ints, inputs, current, modes):
    position = ints[current]
    print(ints[position], end=" ")
    return current + 1


OPERATIONS_DICT = {
    1: add,
    2: multiply,
    3: read_input,
    4: print_value,
}


def run_program(ints, inputs):
    current = 0

    while ints[current] != 99:
        instruction = ints[current]
        opcode, modes = extract_opcode_and_modes(instruction)
        current += 1

        operation = OPERATIONS_DICT[opcode]
        current = operation(ints, inputs, current, modes)


if __name__ == "__main__":
    program = input().rstrip()
    ints = list(map(int, program.split(",")))

    run_program(ints, [1])
