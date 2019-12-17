import numpy as np


def create_pattern_matrix(pattern, length):
    matrix = []

    for y in range(length):
        row = []

        for x in range(length):
            index = (x + 1) // (y + 1) % len(pattern)
            row.append(pattern[index])

        matrix.append(row)

    return np.array(matrix)


if __name__ == "__main__":
    digits = list(map(int, input().rstrip()))
    length = len(digits)

    digits_array = np.array(digits)
    pattern_matrix = create_pattern_matrix([0, 1, 0, -1], length)
    pattern_matrix = pattern_matrix.T

    # phases = 100
    # pattern_powered = np.power(pattern_matrix, phases)
    # result = np.dot(digits_array, pattern_powered)
    # result = abs(result)

    current = digits_array
    for phase in range(100):
        current = np.dot(current, pattern_matrix)
        current = abs(current) % 10

    result = current
    print("".join(map(lambda x: str(x % 10), result[:8])))
