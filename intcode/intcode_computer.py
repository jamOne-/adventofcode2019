from collections import defaultdict, deque

READ = 0
WRITE = 1

INPUT = 0
OUTPUT = 1
JUMP = 2
ADJUST_RELATIVE_BASE = 3


def extract_opcode_and_modes(instruction):
    opcode = instruction % 100
    instruction //= 100
    modes = []

    for _ in range(3):
        modes.append(instruction % 10)
        instruction //= 10

    return opcode, modes


OPERATIONS_DICT = {
    1: (lambda a, b: a + b, (READ, READ, WRITE), None),
    2: (lambda a, b: a * b, (READ, READ, WRITE), None),
    3: (lambda a: a, (WRITE,), INPUT),
    4: (lambda a: a, (READ,), OUTPUT),
    5: (lambda a, b: b if a != 0 else None, (READ, READ), JUMP),
    6: (lambda a, b: b if a == 0 else None, (READ, READ), JUMP),
    7: (lambda a, b: int(a < b), (READ, READ, WRITE), None),
    8: (lambda a, b: int(a == b), (READ, READ, WRITE), None),
    9: (lambda a: a, (READ,), ADJUST_RELATIVE_BASE)
}


class IntcodeComputer:
    def __init__(self, intcode):
        self.current = 0
        self.relative_base = 0
        self.inputs = deque()
        self.intcode = defaultdict(int, enumerate(intcode))
        self.state = "READY"

    def append_input(self, value):
        self.inputs.append(value)

    def extend_input(self, iterable):
        self.inputs.extend(iterable)

    def intcode_slice(self, start, end):
        return [self.intcode[i] for i in range(start, end)]

    def run(self):
        outputs = []

        while True:
            instruction = self.intcode[self.current]
            self.current += 1

            if instruction == 99:
                self.state = "STOPPED"
                break

            opcode, modes = extract_opcode_and_modes(instruction)
            operation, params_types, operation_type = OPERATIONS_DICT[opcode]
            params_values = self.intcode_slice(
                self.current, self.current + len(params_types))
            self.current += len(params_types)

            params_info = list(zip(params_values, params_types, modes))
            read_params = filter(
                lambda param_info: param_info[1] == READ, params_info)
            write_params = filter(
                lambda param_info: param_info[1] == WRITE, params_info)

            read_params = [[self.intcode[n], n, self.intcode[n +
                                                             self.relative_base]][mode] for n, _, mode in read_params]
            write_params = [[n, None, n + self.relative_base][mode]
                            for n, _, mode in write_params]

            if operation_type == INPUT:
                if len(self.inputs) == 0:
                    self.state = "WAITING_FOR_INPUT"
                    self.current -= 1 + len(params_types)
                    break

                read_params.append(self.inputs.popleft())

            result = operation(*read_params)

            for pos in write_params:
                self.intcode[pos] = result

            if operation_type == JUMP and result != None:
                self.current = result

            if operation_type == ADJUST_RELATIVE_BASE:
                self.relative_base += result

            if operation_type == OUTPUT:
                outputs.append(result)

        return outputs, self.state
