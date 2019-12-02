import sys


def calculate_fuel(mass):
    return mass // 3 - 2


def solution(masses):
    return sum(map(calculate_fuel, masses))


if __name__ == "__main__":
    masses = [int(line.rstrip()) for line in sys.stdin]

    print(solution(masses))
