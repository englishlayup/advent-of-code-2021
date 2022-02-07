import numpy as np
from functools import lru_cache


@lru_cache(maxsize=1000)
def get_count(n, days):

    # if days < 0:
    #     return 1 if n == -1 else 0

    fish_count = 0

    for i in range(1, days+1):
        n -= 1
        if n == -1:
            fish_count += 1
            fish_count += get_count(8, days - i)
            n = 6

    # if n > -1:
    #     return get_count(n-1, days-1)
    #
    # if n == -1:
    #     return 1 + get_count(6, days - 1) + get_count(8, days - 1)

    return fish_count


def count_fish(fishes, days):
    for i in range(days):
        fishes -= 1
        new_fishes_count = fishes[fishes == -1].size
        fishes[fishes == -1] = 6
        # if not new_fishes:
        if new_fishes_count > 0:
            fishes = np.concatenate((fishes, [8 for _ in range(new_fishes_count)]))

    return fishes.size


def count_fish_batch(fishes, days, batch_count=2):
    batches = np.array_split(fishes, batch_count)
    total = 0
    for batch in batches:
        total += count_fish(batch, days)
    return total


def main():
    with open('day6.txt') as f:
        fishes = np.array([int(x) for x in f.read().split(',')])

    # print(count_fish_batch(fishes, 256, 5))
    total_fish = fishes.size
    for fish in fishes:
        total_fish += get_count(fish, 256)

    print(total_fish)


if __name__ == '__main__':
    main()
