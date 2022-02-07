import numpy as np


def find_fuel_cost(pos, le_crabs):
    n = np.abs(pos - le_crabs)
    fuel_cost = np.multiply(n, (n + 1)) / 2
    return np.sum(fuel_cost)


if __name__ == '__main__':
    with open('day7.txt') as f:
        crabs = np.array(f.read().split(','), dtype=int)

    possible_pos = np.arange(np.max(crabs))

    min_pos = min(possible_pos, key=lambda x: np.sum(np.abs(x - crabs)))

    print(np.sum(np.abs(min_pos - crabs)))

    min_pos = min(possible_pos, key=lambda x: find_fuel_cost(x, crabs))
    print(find_fuel_cost(min_pos, crabs))
