import math
from collections import Counter


def decode_image(width, height, message):
    size = width * height
    image = ["2"] * size

    for i, char in enumerate(message):
        pos = i % size

        if image[pos] == "2":
            image[pos] = char

    return image


def print_image(width, height, image):
    for i, char in enumerate(image):
        end = "\n" if (i + 1) % width == 0 else " "

        if char == "1":
            print("#", end=end)
        else:
            print(" ", end=end)


if __name__ == "__main__":
    password = input().rstrip()
    width = 25
    height = 6

    image = decode_image(width, height, password)
    print_image(width, height, image)
