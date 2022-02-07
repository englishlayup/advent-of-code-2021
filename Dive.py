if __name__ == '__main__':
    depth = horizontal = aim = 0

    with open('day2.in') as f:
        commands = f.read().splitlines()

    for command in commands:
        direction, units = command.split()

        if direction == 'forward':
            horizontal += int(units)
            depth += aim * int(units)
        if direction == 'down':
            aim += int(units)
        if direction == 'up':
            aim -= int(units)

    print(depth * horizontal)
