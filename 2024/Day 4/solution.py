from os.path import dirname, realpath
from itertools import product, chain

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[str]:
    return [line for line in data.splitlines() if len(line)]

def xmas(data: list[str], row: int, col: int, coords: list[list[int]]) -> int:
    if not all(map(lambda rc: (0 <= rc[0]+row < len(data) and 0 <= rc[1]+col < len(data[0])), coords)):
        return 0
    return 1 if ''.join([data[r+row][c+col] for r, c in coords]) == "XMAS" else 0

def partOne(data: list[str]) -> int:
    return sum(([xmas(data, row, col, coords) for coords in [[[n * x, n * y] for n in range(0, 4)] for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]] for row, col in product(range(len(data)), range(len(data))) if data[row][col] == "X"]))

def mas(data: list[str], row: int, col: int) -> int:
    coords: list[list[list[int]]] = [[[-1, -1], [0, 0], [1, 1]], [[-1, 1], [0, 0], [1, -1]]]
    if not all(map(lambda rc: (0 <= rc[0]+row < len(data) and 0 <= rc[1]+col < len(data[0])), chain.from_iterable(coords))):
        return 0
    return 1 if all(map(lambda x: x == ['M', 'A', 'S'] or x[::-1] == ['M', 'A', 'S'], [[data[r+row][c+col] for r, c in coords[0]], [data[r+row][c+col] for r, c in coords[1]]])) else 0

def partTwo(data: list[str]) -> int:
    return sum(mas(data, row, col) for row, col in product(range(len(data)), range(len(data))) if data[row][col] == "A")

if __name__ == "__main__":
    data: list[str] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
