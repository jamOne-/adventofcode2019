from collections import deque


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


def add(ints, inputs, outputs, current, modes):
    p1, p2, p3 = ints[current:current + 3]
    a = read_with_mode(ints, p1, modes[0])
    b = read_with_mode(ints, p2, modes[1])

    ints[p3] = a + b
    return current + 3


def multiply(ints, inputs, outputs, current, modes):
    p1, p2, p3 = ints[current:current + 3]
    a = read_with_mode(ints, p1, modes[0])
    b = read_with_mode(ints, p2, modes[1])

    ints[p3] = a * b
    return current + 3


def read_input(ints, inputs, outputs, current, modes):
    position = ints[current]
    ints[position] = inputs.popleft()
    return current + 1


def print_value(ints, inputs, outputs, current, modes):
    position = ints[current]
    outputs.append(ints[position])
    return current + 1


OPERATIONS_DICT = {
    1: add,
    2: multiply,
    3: read_input,
    4: print_value,
}


def run_program(ints, inputs):
    current = 0
    outputs = []

    while ints[current] != 99:
        instruction = ints[current]
        opcode, modes = extract_opcode_and_modes(instruction)
        current += 1

        operation = OPERATIONS_DICT[opcode]
        current = operation(ints, inputs, outputs, current, modes)

    return outputs


if __name__ == "__main__":
    program = input().rstrip()
    ints = list(map(int, program.split(",")))

    outputs = run_program(ints, deque([1]))
    print(" ".join(map(str, outputs)))
