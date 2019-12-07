import sys
import math
from collections import deque
from itertools import permutations

sys.path.append("../05/")
runner = __import__("05b")


class Program:
    def __init__(self, ints):
        self.current = 0
        self.ints = list(ints)
        self.inputs = deque()

    def add_input(self, value):
        self.inputs.append(value)

    def run_until_print_or_halt(self):
        outputs = []

        while self.ints[self.current] != 99:
            instruction = self.ints[self.current]
            opcode, modes = runner.extract_opcode_and_modes(instruction)
            self.current += 1

            operation = runner.OPERATIONS_DICT[opcode]
            self.current = operation(
                self.ints, self.inputs, outputs, self.current, modes)

            if outputs:
                return outputs[0]

        return None

    def run_until_halt(self):
        outputs = []
        output = self.run_until_print_or_halt()

        while output != None:
            outputs.append(output)
            output = self.run_until_print_or_halt()

        return outputs


if __name__ == "__main__":
    program = list(map(int, input().rstrip().split(",")))

    max_output = -math.inf
    max_output_phases = None

    for phases in permutations(range(5, 10)):
        amps = [Program(program) for _ in range(5)]

        for amp, phase in zip(amps, phases):
            amp.add_input(phase)

        last_output = 0

        while True:
            for amp in amps:
                amp.add_input(last_output)
                last_output = amp.run_until_print_or_halt()

            if last_output == None:
                break
            elif last_output > max_output:
                max_output = last_output
                max_output_phases = phases

    print(max_output, max_output_phases)
