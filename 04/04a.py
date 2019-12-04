def is_password_correct(password):
    password_string = str(password)

    for i in range(1, 6):
        if password_string[i] < password_string[i - 1]:
            return False

    for i in range(1, 6):
        if password_string[i] == password_string[i - 1]:
            return True

    return False


def count_passwords_in_range(password_range):
    beg, end = password_range
    count = 0

    for password in range(beg, end + 1):
        if is_password_correct(password):
            count += 1

    return count


if __name__ == "__main__":
    password_range = tuple(map(int, input().rstrip().split("-")))

    print(count_passwords_in_range(password_range))
