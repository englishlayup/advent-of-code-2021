if __name__ == '__main__':
    with open('day1.in') as f:
        depths = list(map(int, f.read().splitlines()))

    print(len(list(filter(lambda x: x[0] < x[1], zip(depths[:-1], depths[1:])))))

    slice_1 = depths[:-2]
    slice_2 = depths[1:-1]
    slice_3 = depths[2:]

    assert len(slice_1) == len(slice_2) == len(slice_3)

    windows_sum = list(map(sum, zip(slice_1, slice_2, slice_3)))

    print(len(list(filter(lambda x: x[0] < x[1], zip(windows_sum[:-1], windows_sum[1:])))))
