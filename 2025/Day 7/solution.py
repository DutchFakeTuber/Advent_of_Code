from os.path import dirname, realpath
from collections import deque

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[list[str]]:
    return [[char for char in line] for line in data.splitlines()]

def partOne(data: list[list[str]]) -> int:
    splits: set[tuple[int]] = set()
    current: deque = [(row, col) for row in range(len(data)) for col, val in enumerate(data[row]) if val == 'S']
    while len(current):
        row, col = current.pop()
        if row+1 >= len(data): continue
        elif data[row+1][col] == '.':
            data[row+1][col] = '|'
            current.append((row+1, col))
        elif data[row+1][col] == '^':
            if col-1 < 0: continue
            if col+1 >= len(data[0]): continue
            for offset in [-1, 1]:
                data[row+1][col+offset] = '|'
                current.append((row+1, col+offset))
            splits.add((row+1, col))
    # for line in data:
    #     print(''.join(line))
    return len(splits)

def partTwo(data: list[list[str]]) -> int:
    return ...

if __name__ == "__main__":
    data: list[list[str]] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
