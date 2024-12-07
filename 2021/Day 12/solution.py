import copy

TEST: str = open("test.txt")
DATA: str = open("input.txt")

def getData(data: str) -> list:
    return [line for line in data.splitlines() if len(line) != 0]

def paths(path: dict, position: str, visited: list) -> int:
    if position == 'end':
        print(visited)
        return 1
    else:
        options = [cave for cave in path[position] if cave not in visited]
        newVisited = copy.deepcopy(visited)
        if position.islower():
            newVisited.append(position)
        
        pathways: int = 0
        for option in options:
            pathways += paths(path, option, newVisited)
    return pathways

def pathsFull(path: dict, position: str, visited: list, allVisited: list) -> int:
    if position == 'end':
        newAllVisited = copy.deepcopy(allVisited)
        newAllVisited.append(position)
        print(newAllVisited)
        return 1
    else:
        if 'secondtime' not in visited and position not in visited:
            options = [cave for cave in path[position] if cave != 'start']
        else:
            options = [cave for cave in path[position] if cave not in visited and cave != 'start']

        newVisited = copy.deepcopy(visited)
        newAllVisited = copy.deepcopy(allVisited)
        if position in visited:
            newVisited.append('secondtime')
        if position.islower() and position != 'start':
            newVisited.append(position)
        newAllVisited.append(position)

        pathways: int = 0
        for option in options:
            pathways += pathsFull(path, option, newVisited, newAllVisited)
        return pathways

def partOne(data: list) -> int:
    path: dict = {}
    for line in data:
        cave_1, cave_2 = line.strip().split('-')
        if cave_1 not in path:
            path[cave_1] = []
        path[cave_1].append(cave_2)
        if cave_2 not in path:
            path[cave_2] = []
        path[cave_2].append(cave_1)
    return paths(path, 'start', [])

def partTwo(data: list) -> int:
    path: dict = {}
    for line in data:
        cave_1, cave_2 = line.strip().split('-')
        if cave_1 not in path:
            path[cave_1] = []
        path[cave_1].append(cave_2)
        if cave_2 not in path:
            path[cave_2] = []
        path[cave_2].append(cave_1)
    return pathsFull(path, 'start', [], [])

def main() -> None:
    data = getData(DATA)
    # Comment partOne to let partTwo function properly.
    print(partOne(data))
    print(partTwo(data))

if __name__ == "__main__":
    main()