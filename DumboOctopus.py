import numpy as np
from itertools import count

if __name__ == '__main__':
    with open('day11.in') as f:
        lines = f.read().splitlines()

    octopuses = np.array([list(map(int, line)) for line in lines])
    rows, cols = octopuses.shape

    goal = np.zeros(octopuses.shape, dtype=int)
    flashes = 0

    for i in count():
        octopuses += 1
        while np.count_nonzero(octopuses > 9) > 0:
            flashes += np.count_nonzero(octopuses > 9)
            for x, y in zip(*(octopuses > 9).nonzero()):
                row1 = max(0, x - 1)
                row2 = min(rows - 1, x + 1)
                col1 = max(0, y - 1)
                col2 = min(cols - 1, y + 1)
                # print(octopuses[row1:row2+1, col1:col2+1])
                octopus_window = octopuses[row1:row2 + 1, col1:col2 + 1]
                octopus_window[octopus_window > 0] += 1
                octopuses[x, y] = 0
        if (octopuses == goal).all():
            print(octopuses)
            print(i+1)
            break

    # print(flashes)
