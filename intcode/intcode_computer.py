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


def add(ints, inputs, relative_base, current, modes):
    p1, p2, p3 = get_slice(ints, current, current + 3)
    a = read_with_mode(ints, relative_base, p1, modes[0])
    b = read_with_mode(ints, relative_base, p2, modes[1])
    pos = read_position(p3, relative_base, modes[2])

    ints[pos] = a + b
    return current + 3, relative_base, None


def multiply(ints, inputs, relative_base, current, modes):
    p1, p2, p3 = get_slice(ints, current, current + 3)
    a = read_with_mode(ints, relative_base, p1, modes[0])
    b = read_with_mode(ints, relative_base, p2, modes[1])
    pos = read_position(p3, relative_base, modes[2])

    ints[pos] = a * b
    return current + 3, relative_base, None


def read_input(ints, inputs, relative_base, current, modes):
    param = ints[current]
    position = read_position(param, relative_base, modes[0])
    ints[position] = inputs.popleft()
    return current + 1, relative_base, None


def print_value(ints, inputs, relative_base, current, modes):
    param = ints[current]
    value = read_with_mode(ints, relative_base, param, modes[0])
    return current + 1, relative_base, value


def jump_if_true(ints, inputs, relative_base, current, modes):
    p1, p2 = ints[current], ints[current + 1]
    a = read_with_mode(ints, relative_base, p1, modes[0])
    b = read_with_mode(ints, relative_base, p2, modes[1])

    if a != 0:
        return b, relative_base, None

    return current + 2, relative_base, None


def jump_if_false(ints, inputs, relative_base, current, modes):
    p1, p2 = ints[current], ints[current + 1]
    a = read_with_mode(ints, relative_base, p1, modes[0])
    b = read_with_mode(ints, relative_base, p2, modes[1])

    if a == 0:
        return b, relative_base, None

    return current + 2, relative_base, None


def less_than(ints, inputs, relative_base, current, modes):
    p1, p2, p3 = get_slice(ints, current, current + 3)
    a = read_with_mode(ints, relative_base, p1, modes[0])
    b = read_with_mode(ints, relative_base, p2, modes[1])
    pos = read_position(p3, relative_base, modes[2])

    ints[pos] = int(a < b)
    return current + 3, relative_base, None


def equals(ints, inputs, relative_base, current, modes):
    p1, p2, p3 = get_slice(ints, current, current + 3)
    a = read_with_mode(ints, relative_base, p1, modes[0])
    b = read_with_mode(ints, relative_base, p2, modes[1])
    pos = read_position(p3, relative_base, modes[2])

    ints[pos] = int(a == b)
    return current + 3, relative_base, None


def adjust_relative_base(ints, inputs, relative_base, current, modes):
    param = ints[current]
    a = read_with_mode(ints, relative_base, param, modes[0])

    return current + 1, relative_base + a, None


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


class IntcodeComputer:
    def __init__(self, intcode):
        self.current = 0
        self.relative_base = 0
        self.inputs = deque()
        self.intcode = defaultdict(int, enumerate(intcode))

    def append_input(self, value):
        self.inputs.append(value)

    def run_until_print_or_halt(self):
        while True:
            instruction = self.intcode[self.current]
            if instruction == 99:
                return None

            opcode, modes = extract_opcode_and_modes(instruction)
            self.current += 1

            operation = OPERATIONS_DICT[opcode]
            self.current, self.relative_base, output = operation(
                self.intcode, self.inputs, self.relative_base, self.current, modes)

            if output != None:
                return output

    def run_until_halt(self):
        outputs = []

        while True:
            output = self.run_until_print_or_halt(self)

            if output != None:
                outputs.append(output)
            else:
                return outputs
