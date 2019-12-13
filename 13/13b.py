import os
import sys
import time
import keyboard
from collections import defaultdict
sys.path.append("../intcode/")
icc = __import__("intcode_computer")

TILES = {
    0: " ",
    1: "#",
    2: "x",
    3: "–",
    4: "o"
}


def cmp(x, y):
    return (x > y) - (x < y)


def update_display(display, output):
    paddle, ball = None, None

    for i in range(0, len(output), 3):
        x, y, tile = output[i:i + 3]
        display[x, y] = tile

    for (x, y), tile in display.items():
        if tile == 3:
            paddle = x, y
        elif tile == 4:
            ball = x, y

    return paddle, ball


def draw_game(display):
    os.system("cls")

    xs = list(map(lambda key: key[0], display.keys()))
    ys = list(map(lambda key: key[1], display.keys()))
    max_x = max(xs)
    max_y = max(ys)

    print("Highscore: ", display[-1, 0])

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            tile = display[x, y]
            print(TILES[tile], end="")

        print("")


def get_joystick_move():
    key = keyboard.read_key()
    time.sleep(0.2)

    if key == "left":
        return -1
    if key == "right":
        return 1
    else:
        return 0


def get_paddle_move(paddle, ball):
    return cmp(ball[0], paddle[0])


def play_game(intcode):
    intcode[0] = 2
    intcode_computer = icc.IntcodeComputer(intcode)
    state = intcode_computer.state
    display = defaultdict(int)

    while state != "STOPPED":
        output, state = intcode_computer.run()
        paddle, ball = update_display(display, output)
        draw_game(display)
        # move = get_joystick_move()
        move = get_paddle_move(paddle, ball)
        intcode_computer.append_input(move)
        time.sleep(1 / 60)

    print("Highscore: ", display[-1, 0])


if __name__ == "__main__":
    intcode = list(map(int, input().rstrip().split(",")))
    play_game(intcode)
