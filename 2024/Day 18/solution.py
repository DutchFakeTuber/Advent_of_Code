from os.path import dirname, realpath
from collections import deque

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[list[int]]:
    return [tuple(map(int, line.split(','))) for line in data.splitlines() if len(line)]

def traverse(data: list[list[int]], grid: tuple[int]=(0, 70)) -> int:
    start, end = (grid[0], grid[0]), (grid[1], grid[1])
    data: set = set([(r, c) for r, c in data])
    todo: deque = deque([(0, *start)])
    visited: set = set()
    while todo:
        steps, x, y = todo.popleft()
        if (x, y) in visited: continue
        visited.add((x, y))
        if (x, y) == end:
            return steps
        for X, Y in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
            if (X, Y) in visited or (X, Y) in data: continue
            if grid[0] <= X <= grid[1] and grid[0] <= Y <= grid[1]:
                todo.append((steps + 1, X, Y))
    return None

def partOne(data: list[list[int]], grid: tuple[int]=(0, 70)) -> int:
    return traverse(data, grid)

def partTwo(data: list[list[int]], grid=(0, 70)) -> str:
    low, high = 0, len(data) - 1
    while low < high:
        checkUntil: int = (low + high) // 2
        result: int | None = traverse(data[:checkUntil+1], grid)
        if result is None:
            high = checkUntil
        else:
            low = checkUntil + 1
    return f'{data[low][0]},{data[low][1]}'

if __name__ == "__main__":
    data: list[list[int]] = fetchData(DATA)
    print(partOne(data[:12], grid=(0, 70)))
    print(partTwo(data, grid=(0, 70)))
