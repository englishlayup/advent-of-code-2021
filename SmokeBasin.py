import numpy as np


def count_basins(height_map, i, j):
    rows, cols = height_map.shape
    # print(height_map)
    if i >= rows or j >= cols or i < 0 or j < 0:
        return 0

    if height_map[i][j] == 9:
        return 0

    if height_map[i][j] != 9:
        height_map[i][j] = 9
        down = count_basins(height_map, i + 1, j)
        up = count_basins(height_map, i - 1, j)
        left = count_basins(height_map, i, j - 1)
        right = count_basins(height_map, i, j + 1)
        return 1 + down + up + left + right


def main():
    with open('day9.in') as f:
        lines = f.read().splitlines()

    height_map = list()
    for line in lines:
        height_map.append(list(map(int, line)))

    height_map = np.array(height_map)
    risk_level = 0
    # print(height_map.shape)
    rows, cols = height_map.shape

    low_points = list()

    for i in range(rows):
        for j in range(cols):
            to_compare = list()
            if i + 1 < rows:
                # if height_map[i + 1, j] != height_map[i, j]:
                to_compare.append(height_map[i + 1, j])
            if i - 1 >= 0:
                # if height_map[i - 1, j] != height_map[i, j]:
                to_compare.append(height_map[i - 1, j])
            if j + 1 < cols:
                # if height_map[i, j + 1] != height_map[i, j]:
                to_compare.append(height_map[i, j + 1])
            if j - 1 >= 0:
                # if height_map[i, j - 1] != height_map[i, j]:
                to_compare.append(height_map[i, j - 1])

            if min(*to_compare, height_map[i, j]) == height_map[i, j] and height_map[i, j] not in to_compare:
                risk_level += height_map[i, j] + 1
                low_points.append((i, j))

    print(low_points)
    basin_sizes = list()
    for point in low_points:
        basin_sizes.append(count_basins(height_map, *point))

    print(sorted(basin_sizes, reverse=True)[:3])
    print(105*102*100)


if __name__ == '__main__':
    main()
