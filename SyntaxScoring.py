SYNTAX_ERROR_TABLE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

COMPLETION_TABLE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

PAIR_TABLE = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

if __name__ == '__main__':
    with open('day10.in') as f:
        lines = f.read().splitlines()

    chunk = list()
    syntax_error_points = 0
    incomplete_lines = lines.copy()

    print(incomplete_lines is lines)

    for line in lines:
        for char in line:
            if char in '([{<':
                chunk.append(char)
            else:
                expected = PAIR_TABLE[chunk.pop()]
                if expected != char:
                    # print(f'Expected {expected}, but found {char} instead')
                    incomplete_lines.remove(line)
                    syntax_error_points += SYNTAX_ERROR_TABLE[char]

    print(syntax_error_points)

    chunk = list()
    completion_points = list()
    for line in incomplete_lines:
        completion_point = 0
        for char in line:
            if char in '([{<':
                chunk.append(char)
            else:
                expected = PAIR_TABLE[chunk.pop()]
                if expected != char:
                    print(f'Expected {expected}, but found {char} instead')

        while chunk:
            completion_point *= 5
            completion_point += COMPLETION_TABLE[PAIR_TABLE[chunk.pop()]]
        completion_points.append(completion_point)
    print(completion_points)
    print(sorted(completion_points)[len(completion_points)//2])
