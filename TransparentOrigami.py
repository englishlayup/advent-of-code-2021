import numpy as np


def fold(arr, x=None, y=None):
    if y:
        top_half = arr[:y]
        bottom_half = np.flipud(arr[y+1:])
        return top_half + bottom_half
    if x:
        left_half = arr[:, :x]
        right_half = np.fliplr(arr[:, x+1:])
        return left_half + right_half


def main():
    with open('day13.in') as f:
        lines = f.read().splitlines()

    coordinates = list()
    for line in lines[:883]:
        coordinates.append(list(map(int, line.split(','))))

    coord_arr = np.array(coordinates)
    fold_instructions = lines[884:]

    xmax, ymax = coord_arr.max(axis=0)

    transparent_paper = np.array([[False for _ in range(xmax + 1)] for _ in range(ymax + 1)])

    for coord in coord_arr:
        x, y = coord
        transparent_paper[y, x] = True

    folded = fold(transparent_paper, x=665)
    # print(folded)
    # print()
    # print(fold(folded, x=5))


if __name__ == '__main__':
    main()
