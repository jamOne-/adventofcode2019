import sys
sys.path.append("../intcode/")
icc = __import__("intcode_computer")


def run_computers(intcode, n):
    computers = [icc.IntcodeComputer(intcode) for _ in range(n)]
    NAT = None
    last_NAT_y = None

    for address, computer in enumerate(computers):
        computer.append_input(address)

    while True:
        packets = []

        for computer in computers:
            if computer.state == "WAITING_FOR_INPUT" and len(computer.inputs) == 0:
                computer.append_input(-1)
            outputs, _ = computer.run()

            for i in range(0, len(outputs), 3):
                address, x, y = outputs[i:i + 3]
                packets.append((address, x, y))

        if len(packets) == 0 and NAT != None:
            x, y = NAT

            if last_NAT_y == y:
                return y
            else:
                last_NAT_y = y
                computers[0].append_input(x)
                computers[0].append_input(y)

        for address, x, y in packets:
            if address == 255:
                NAT = x, y
                continue

            computers[address].append_input(x)
            computers[address].append_input(y)


if __name__ == "__main__":
    intcode = list(map(int, input().rstrip().split(",")))
    y = run_computers(intcode, 50)
    print(y)
