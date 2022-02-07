import numpy as np

if __name__ == '__main__':

    with open('day4.in') as f:
        draw_numbers = list(map(int, f.readline().split(',')))
        boards = np.array(f.read().split(), dtype=int).reshape((2500//25, 5, 5))

    WIN_VAL = np.array([0, 0, 0, 0, 0])

    print(np.where((WIN_VAL == boards).all(axis=2)))

    for number in draw_numbers:
        boards[boards == number] = 0

        if (WIN_VAL == boards).all(axis=1).any() or (WIN_VAL == boards).all(axis=2).any():
            x, _ = np.where((WIN_VAL == boards).all(axis=1))
            print(boards[x])
            if not x.any():
                x, _ = np.where((WIN_VAL == boards).all(axis=2))
                print(boards[x])
                print(x)
            for idx in x:
                print(np.sum(np.sum(boards[idx])) * number)
            boards = np.delete(boards, x, axis=0)

