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
            for offset in [-1, 1]:
                data[row+1][col+offset] = '|'
                current.append((row+1, col+offset))
            splits.add((row+1, col))
    return len(splits)

def partTwo(data: list[list[str]]) -> int:
    data.append([0] * len(data[0]))
    splitters: dict = {(row, col): 0 if val == '^' else 1 for row in range(len(data)) for col, val in enumerate(data[row]) if val in ['^', 'S']}
    for row in range(0, len(data)):
        for col in range(0, len(data[row])):
            if splitters.get((row, col), None) == None: continue
            offset: list = [0, -1, 1]
            for o in [offset[0]] if data[row][col] == 'S' else offset[1:]:
                counter: int = 0
                while True:
                    counter += 1
                    if data[row+counter][col+o] == '^':
                        splitters[(row+counter, col+o)] += splitters[(row, col)]
                        break
                    elif isinstance(data[row+counter][col+o], int):
                        data[row+counter][col+o] += splitters[(row, col)]
                        break
    return sum(data[-1])

if __name__ == "__main__":
    print(partOne(fetchData(DATA)))
    print(partTwo(fetchData(DATA)))
