import re
import sys


class Deck:
    def __init__(self, offset, increment, deck_size):
        self.offset = offset % deck_size
        self.increment = increment % deck_size
        self.deck_size = deck_size

    def change_offset(self, new_offset):
        self.offset = new_offset % self.deck_size

    def change_increment(self, new_increment):
        self.increment = new_increment % self.deck_size

    def deal_into_new_stack(self):
        self.change_offset(self.offset - self.increment)
        self.change_increment(-self.increment)

    def cut_n_cards(self, n):
        self.change_offset(self.offset + self.increment * n)

    def deal_with_increment(self, n):
        inv_n = pow(n, self.deck_size - 2, self.deck_size)
        self.change_increment(self.increment * inv_n)

    def card_at_nth_position(self, n):
        return (self.increment * n + self.offset) % self.deck_size


def shuffle_deck(deck, operations, times):
    for operation in operations:
        if operation == "deal into new stack":
            deck.deal_into_new_stack()
        elif operation.startswith("deal with increment"):
            n = int(re.findall("-?\d+", operation)[0])
            deck.deal_with_increment(n)
        else:
            n = int(re.findall("-?\d+", operation)[0])
            deck.cut_n_cards(n)

    offset_diff = deck.offset
    increment_mul = deck.increment
    deck_size = deck.deck_size

    last_offset = offset_diff * (1 - pow(increment_mul, times, deck_size)) * \
        pow(1 - increment_mul, deck_size - 2, deck_size)
    last_increment = pow(increment_mul, times, deck_size)

    return Deck(last_offset, last_increment, deck_size)


if __name__ == "__main__":
    operations = [line.rstrip() for line in sys.stdin]
    deck = Deck(0, 1, 119315717514047)
    deck = shuffle_deck(deck, operations, 101741582076661)
    print(deck.card_at_nth_position(2020))
