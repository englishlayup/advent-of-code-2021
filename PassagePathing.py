def count_paths(cave_map, visited, node, path_count):
    visited[node] = True
    if node == 'end':
        return path_count + 1

    for adj in cave_map[node]:
        if adj.isupper() or not visited[adj]:
            path_count += count_paths(cave_map, visited, adj)
        # if adj == 'end':
        #     path_count += 1
    visited[node] = False
    return path_count


def main():
    with open('day12.in') as f:
        lines = f.read().splitlines()

    cave_map = dict()

    for line in lines:
        if line.split('-')[0] not in cave_map:
            cave_map[line.split('-')[0]] = [line.split('-')[1]]
        else:
            cave_map[line.split('-')[0]].append(line.split('-')[1])

        if line.split('-')[1] not in cave_map:
            cave_map[line.split('-')[1]] = [line.split('-')[0]]
        else:
            cave_map[line.split('-')[1]].append(line.split('-')[0])

    visited = dict()
    for cave in cave_map:
        visited[cave] = False
    print(count_paths(cave_map, visited, node='start', path_count=0))


if __name__ == '__main__':
    main()
