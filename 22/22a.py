import re
import sys


def deal_into_new_stack(cards):
    return cards[::-1]


def deal_with_increment(cards, n):
    new_cards = [0] * len(cards)

    for i, card in enumerate(cards):
        new_cards[(i * n) % len(cards)] = card

    return new_cards


def cut(cards, n):
    left = cards[:n]
    right = cards[n:]

    return right + left


def perform_operations(cards, operations):
    for operation in operations:
        if operation == "deal into new stack":
            cards = deal_into_new_stack(cards)
        elif operation.startswith("deal with increment"):
            n = int(re.findall("-?\d+", operation)[0])
            cards = deal_with_increment(cards, n)
        else:
            n = int(re.findall("-?\d+", operation)[0])
            cards = cut(cards, n)

    return cards


if __name__ == "__main__":
    operations = [line.rstrip() for line in sys.stdin]
    cards = list(range(10007))
    cards = perform_operations(cards, operations)

    for position, card in enumerate(cards):
        if card == 2019:
            print(position)
            break
