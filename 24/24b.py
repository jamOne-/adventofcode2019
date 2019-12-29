# unfortunately contains bug somewhere... :'(

import sys
from collections import defaultdict as dd


def grid_to_biodiversity(grid):
    biodiversity = 0
    joined = "".join(grid)

    for char in reversed(joined):
        biodiversity <<= 1

        if char == "#":
            biodiversity += 1

    return biodiversity


def count_bugs(layers, layer_i, i):
    x, y = i % 5, i // 5

    positions = []

    # left
    if x == 0:
        positions.append((layer_i - 1, 1, 2))
    elif x == 3 and y == 2:
        positions.extend((layer_i + 1, 4, y_) for y_ in range(5))
    else:
        positions.append((layer_i, x - 1, y))

    # right
    if x == 1 and y == 2:
        positions.extend((layer_i + 1, 0, y_) for y_ in range(5))
    elif x == 4:
        positions.append((layer_i - 1, 3, 2))
    else:
        positions.append((layer_i, x + 1, y))

    # up
    if y == 0:
        positions.append((layer_i - 1, 2, 1))
    elif x == 2 and y == 3:
        positions.extend((layer_i + 1, x_, 4) for x_ in range(5))
    else:
        positions.append((layer_i, x, y - 1))

    # down
    if x == 2 and y == 1:
        positions.extend((layer_i + 1, x_, 0) for x_ in range(5))
    elif y == 4:
        positions.append((layer_i - 1, 2, 3))
    else:
        positions.append((layer_i, x, y + 1))

    count = 0
    for layer_i, x, y, in positions:
        mask = 1 << (y * 5 + x)
        count += int(layers[layer_i] & mask == mask)

    return count


def simulate(layers, minutes):
    for minute in range(minutes):
        new_layers = dd(int, layers)

        layers_items = list(layers.items())
        for layer_i, layer in layers_items:
            new_layer = layer

            for i in range(25):
                if i == 12:
                    continue

                bugs = count_bugs(layers, layer_i, i)
                current = 1 << i

                if layer & current == current and bugs != 1 or layer & current == 0 and (bugs == 1 or bugs == 2):
                    new_layer ^= current

            new_layers[layer_i] = new_layer

        for layer_i in layers.keys():
            if layer_i not in new_layers:
                new_layers[layer_i] = 0

        layers = new_layers

    return layers


def print_layers(layers):
    for layer_i in sorted(layers.keys()):
        print("Depth", layer_i)
        print_grid(layers[layer_i])
        print("\n")


def print_grid(biodiversity):
    for y in range(5):
        for x in range(5):
            char = "#" if biodiversity & 1 == 1 else "."
            char = "?" if x == 2 and y == 2 else char

            biodiversity >>= 1
            print(char, end="")

        print("")


if __name__ == "__main__":
    grid = [line.rstrip() for line in sys.stdin]
    biodiversity = grid_to_biodiversity(grid)

    layers = dd(int)
    layers[0] = biodiversity
    layers = simulate(layers, 100)
    # print_layers(layers)

    print(sum(map(lambda layer: bin(layer).count("1"), layers.values())))
