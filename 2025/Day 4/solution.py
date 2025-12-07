from os.path import dirname, realpath

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[list[str]]:
    return [[col for col in data.splitlines()[row]] for row in range(len(data.splitlines()))]

def rollRemover(puzzle: list[list[str]]) -> tuple[int, list[list[str]]]:
    COORDS: list[list] = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    LENGTH: int = len(puzzle)
    WIDTH: int = len(puzzle[0])
    removedRolls: list[list[int]] = []
    count: int = 0
    for row, col, val in [[r, c, v] for r in range(LENGTH) for c, v in enumerate(puzzle[r])]:
        if val != '@': continue
        neighbours: int = 0
        for r, c in COORDS:
            if 0 <= row + r < LENGTH and 0 <= col + c < WIDTH:
                if puzzle[row+r][col+c] == '@':
                    neighbours += 1
        if neighbours < 4:
            removedRolls.append([row, col])
            count += 1
    for r, c in removedRolls:
        puzzle[r][c] = 'x'
    return count, puzzle

def partOne(data: list[list[str]]) -> int:
    count, _ = rollRemover(data)
    return count

def partTwo(data: list[list[str]]) -> int:
    count: int = 0
    while True:
        c, data = rollRemover(data)
        count += c
        if not c: break
    return count

if __name__ == "__main__":
    print(partOne(fetchData(DATA)))
    print(partTwo(fetchData(DATA)))
