import sys
import math
from itertools import permutations

sys.path.append("../05/")
runner = __import__("05b")


if __name__ == "__main__":
    program = list(map(int, input().rstrip().split(",")))

    max_output = -math.inf
    max_output_phases = None

    for phases in permutations(range(5)):
        last_output = 0

        for amp_i in range(5):
            inputs = [last_output, phases[amp_i]]
            program_copy = list(program)
            outputs = runner.run_program(program_copy, inputs)

            assert(len(outputs) == 1)
            last_output = outputs[0]

        if last_output > max_output:
            max_output = last_output
            max_output_phases = phases

    print(max_output, max_output_phases)
