from collections import defaultdict, deque


def extract_opcode_and_modes(instruction):
    opcode = instruction % 100
    instruction //= 100
    modes = []

    for _ in range(3):
        modes.append(instruction % 10)
        instruction //= 10

    return opcode, modes


def read_with_mode(ints, relative_base, pos, mode):
    if mode == 0:
        return ints[pos]
    elif mode == 1:
        return pos
    else:
        return ints[relative_base + pos]


def read_position(pos, relative_base, mode):
    if mode == 0:
        return pos
    elif mode == 2:
        return pos + relative_base


def get_slice(source, start, end):
    return [source[i] for i in range(start, end)]


def add(ints, inputs, outputs, relative_base, current, modes):
    p1, p2, p3 = get_slice(ints, current, current + 3)
    a = read_with_mode(ints, relative_base, p1, modes[0])
    b = read_with_mode(ints, relative_base, p2, modes[1])
    pos = read_position(p3, relative_base, modes[2])

    ints[pos] = a + b
    return current + 3, relative_base


def multiply(ints, inputs, outputs, relative_base, current, modes):
    p1, p2, p3 = get_slice(ints, current, current + 3)
    a = read_with_mode(ints, relative_base, p1, modes[0])
    b = read_with_mode(ints, relative_base, p2, modes[1])
    pos = read_position(p3, relative_base, modes[2])

    ints[pos] = a * b
    return current + 3, relative_base


def read_input(ints, inputs, outputs, relative_base, current, modes):
    param = ints[current]
    position = read_position(param, relative_base, modes[0])
    ints[position] = inputs.popleft()
    return current + 1, relative_base


def print_value(ints, inputs, outputs, relative_base, current, modes):
    param = ints[current]
    value = read_with_mode(ints, relative_base, param, modes[0])
    outputs.append(value)
    return current + 1, relative_base


def jump_if_true(ints, inputs, outputs, relative_base, current, modes):
    p1, p2 = ints[current], ints[current + 1]
    a = read_with_mode(ints, relative_base, p1, modes[0])
    b = read_with_mode(ints, relative_base, p2, modes[1])

    if a != 0:
        return b, relative_base

    return current + 2, relative_base


def jump_if_false(ints, inputs, outputs, relative_base, current, modes):
    p1, p2 = ints[current], ints[current + 1]
    a = read_with_mode(ints, relative_base, p1, modes[0])
    b = read_with_mode(ints, relative_base, p2, modes[1])

    if a == 0:
        return b, relative_base

    return current + 2, relative_base


def less_than(ints, inputs, outputs, relative_base, current, modes):
    p1, p2, p3 = get_slice(ints, current, current + 3)
    a = read_with_mode(ints, relative_base, p1, modes[0])
    b = read_with_mode(ints, relative_base, p2, modes[1])
    pos = read_position(p3, relative_base, modes[2])

    ints[pos] = int(a < b)
    return current + 3, relative_base


def equals(ints, inputs, outputs, relative_base, current, modes):
    p1, p2, p3 = get_slice(ints, current, current + 3)
    a = read_with_mode(ints, relative_base, p1, modes[0])
    b = read_with_mode(ints, relative_base, p2, modes[1])
    pos = read_position(p3, relative_base, modes[2])

    ints[pos] = int(a == b)
    return current + 3, relative_base


def adjust_relative_base(ints, inputs, outputs, relative_base, current, modes):
    param = ints[current]
    a = read_with_mode(ints, relative_base, param, modes[0])

    return current + 1, relative_base + a


OPERATIONS_DICT = {
    1: add,
    2: multiply,
    3: read_input,
    4: print_value,
    5: jump_if_true,
    6: jump_if_false,
    7: less_than,
    8: equals,
    9: adjust_relative_base
}


def run_program(ints, inputs):
    current = 0
    relative_base = 0
    outputs = []

    while ints[current] != 99:
        instruction = ints[current]
        opcode, modes = extract_opcode_and_modes(instruction)
        current += 1

        operation = OPERATIONS_DICT[opcode]
        current, relative_base = operation(
            ints, inputs, outputs, relative_base, current, modes)

    return outputs


if __name__ == "__main__":
    program = input().rstrip()
    ints = list(map(int, program.split(",")))
    ints_dict = defaultdict(int, enumerate(ints))

    outputs = run_program(ints_dict, deque([2]))
    print(" ".join(map(str, outputs)))
