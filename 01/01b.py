import sys


def calculate_fuel(mass):
    fuel = mass // 3 - 2

    if fuel <= 0:
        return 0

    return fuel + calculate_fuel(fuel)


def solution(masses):
    return sum(map(calculate_fuel, masses))


if __name__ == "__main__":
    masses = [int(line.rstrip()) for line in sys.stdin]

    print(solution(masses))
