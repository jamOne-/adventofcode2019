if __name__ == "__main__":
    digits = list(map(int, input().rstrip() * 10000))
    offset = int("".join(map(str, digits[:7])))

    assert(offset >= len(digits) / 2)

    for phase in range(100):
        print("phase={}".format(phase), end="\r")

        for i in range(len(digits) - 2, offset - 2, -1):
            digits[i] += digits[i + 1]
            digits[i + 1] = abs(digits[i + 1]) % 10

    print("".join(map(str, digits[offset:offset + 8])))
