import re
import sys


def deal_into_new_stack(cards, pos):
    return cards - 1 - pos


def deal_with_increment(cards, pos, n):
    return (pos * n) % cards


def cut(cards, pos, n):
    return (pos - n) % cards


def perform_operations(cards, operations, pos):
    for operation in operations:
        if operation == "deal into new stack":
            pos = deal_into_new_stack(cards, pos)
        elif operation.startswith("deal with increment"):
            n = int(re.findall("-?\d+", operation)[0])
            pos = deal_with_increment(cards, pos, n)
        else:
            n = int(re.findall("-?\d+", operation)[0])
            pos = cut(cards, pos, n)

    return pos


if __name__ == "__main__":
    operations = [line.rstrip() for line in sys.stdin]
    position = perform_operations(10007, operations, 2019)
    print(position)
