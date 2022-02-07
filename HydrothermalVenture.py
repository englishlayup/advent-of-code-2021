import numpy as np


class Point:
    def __init__(self, x=0, y=0, str_repr=None):
        if str_repr:
            self.x, self.y = map(int, (str_repr.split(',')))
        else:
            self.x = x
            self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y) or (self.x == other.y and self.y == other.x)

    def __hash__(self):
        return hash((self.x, self.y))


class Line:
    def __init__(self, str_repr):
        start_str, end_str = str_repr.split(' -> ')
        self.p1 = Point(str_repr=start_str)
        self.p2 = Point(str_repr=end_str)

    def __repr__(self):
        return f'Start at {self.p1}; end at {self.p2}'

    def get_cover_sets(self):
        covered_set = set()
        if self.p1.x == self.p2.x:
            big = max(self.p1.y, self.p2.y)
            small = min(self.p1.y, self.p2.y)

            for i in range(small, big + 1):
                covered_set.add(Point(x=self.p1.x, y=i))
        elif self.p1.y == self.p2.y:
            big = max(self.p1.x, self.p2.x)
            small = min(self.p1.x, self.p2.x)

            for i in range(small, big + 1):
                covered_set.add(Point(x=i, y=self.p1.y))

        else:
            xs = ys = None
            if self.p1.x < self.p2.x and self.p1.y < self.p2.y:
                xs = range(self.p1.x, self.p2.x+1)
                ys = range(self.p1.y, self.p2.y+1)
            elif self.p1.x < self.p2.x and self.p1.y > self.p2.y:
                xs = range(self.p1.x, self.p2.x + 1)
                ys = range(self.p2.y, self.p1.y + 1).__reversed__()
            elif self.p1.x > self.p2.x and self.p1.y > self.p2.y:
                xs = range(self.p2.x, self.p1.x + 1)
                ys = range(self.p2.y, self.p1.y + 1)
            elif self.p1.x > self.p2.x and self.p1.y < self.p2.y:
                xs = range(self.p2.x, self.p1.x + 1)
                ys = range(self.p1.y, self.p2.y + 1).__reversed__()

            for x, y in zip(xs, ys):
                covered_set.add(Point(x=x, y=y))

        return covered_set


if __name__ == '__main__':
    with open('day5.in') as f:
        lines = [Line(x) for x in f.read().splitlines()]

    cover_sets = [x.get_cover_sets() for x in lines]
    overlap_set = set()

    for set1 in cover_sets:
        for set2 in cover_sets:
            if set1 is not set2:
                overlap_set.update(set1.intersection(set2))

    print(len(overlap_set))
