import sys


def grid_to_biodiversity(grid):
    biodiversity = 0
    joined = "".join(grid)

    for char in reversed(joined):
        biodiversity <<= 1

        if char == "#":
            biodiversity += 1

    return biodiversity


def count_bugs(biodiversity, current, i):
    count = 0
    x, y = i % 5, i // 5

    masks = []
    if y > 0:
        masks.append(current >> 5)
    if y < 4:
        masks.append(current << 5)
    if x > 0:
        masks.append(current >> 1)
    if x < 4:
        masks.append(current << 1)

    for mask in masks:
        if biodiversity & mask == mask:
            count += 1

    return count


def simulate(biodiversity):
    seen = set()

    while biodiversity not in seen:
        seen.add(biodiversity)
        new_bio = biodiversity

        current = 1
        for i in range(25):
            bugs = count_bugs(biodiversity, current, i)

            if biodiversity & current == current and bugs != 1 or biodiversity & current == 0 and (bugs == 1 or bugs == 2):
                new_bio ^= current

            current <<= 1

        biodiversity = new_bio

    return biodiversity


if __name__ == "__main__":
    grid = [line.rstrip() for line in sys.stdin]
    biodiversity = grid_to_biodiversity(grid)
    repeated_biodiversity = simulate(biodiversity)

    print(repeated_biodiversity)
