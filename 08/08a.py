import math
from collections import Counter


def fewest0layer(width, height, password):
    fewest_layer, fewest_count = None, math.inf
    size = width * height
    layers = math.ceil(len(password) / size)

    for layer_i in range(layers):
        layer = password[layer_i * size:(layer_i + 1) * size]
        counter = Counter(layer)

        if counter["0"] < fewest_count:
            fewest_layer, fewest_count = layer, counter["0"]

    return fewest_layer


if __name__ == "__main__":
    password = input().rstrip()
    width = 25
    height = 6

    layer = fewest0layer(width, height, password)
    counter = Counter(layer)
    print(counter["1"] * counter["2"])
