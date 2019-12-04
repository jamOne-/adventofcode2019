def is_password_correct(password):
    password_string = str(password)

    for i in range(1, 6):
        if password_string[i] < password_string[i - 1]:
            return False

    current_length = 1

    for i in range(1, 6):
        if password_string[i] == password_string[i - 1]:
            current_length += 1
        else:
            if current_length == 2:
                return True

            current_length = 1

    return current_length == 2


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
