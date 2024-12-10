from os.path import dirname, realpath
from collections import deque
from itertools import product

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[list[int]]:
    return [list(map(int, line)) for line in data.splitlines() if len(line)]

def traverse(topo: list[list[int]], start: list[int, int], uniqueTops: bool=True) -> int:
    visited: set | int = set() if uniqueTops else 0
    positions: deque = deque([[topo[start[0]][start[1]], *start]]) # Value, Row, Column
    while positions:
        val, row, col = positions.popleft()
        if val == 9:
            if uniqueTops:
                visited.add((val, row, col))
            else:
                visited += 1
            continue
        for r, c in [[0, -1], [0, 1], [-1, 0], [1, 0]]: # LRUD
            if 0 <= row+r < len(topo) and 0 <= col+c < len(topo[0]):
                if val + 1 == topo[row+r][col+c]:
                    positions.append([topo[row+r][col+c], row+r, col+c])
    if uniqueTops:
        return len(visited)
    return visited

def partOne(data: list[list[int]]) -> int:
    return sum([traverse(data, [row, col]) for row, col in product(range(len(data)), range(len(data[0]))) if data[row][col] == 0])

def partTwo(data: list[list[int]]) -> int:
    return sum([traverse(data, [row, col], False) for row, col in product(range(len(data)), range(len(data[0]))) if data[row][col] == 0])

if __name__ == "__main__":
    data: list[list[int]] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
