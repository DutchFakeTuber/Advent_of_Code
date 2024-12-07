from functools import cache
from multiprocessing import Pool

TEST: str = open("test.txt")
DATA: str = open("input.txt")

def fetchData(data: str) -> list[list[str, tuple[int]]]:
    return [[line.split()[0], eval(f"({line.split()[1]})")] for line in data.splitlines()]

@cache
def pattern(patt: str, clues: tuple[int], size: int=0) -> None:
    if not patt:
        if ((len(clues) == 1 and clues[0] == size) or (len(clues) == 0 and size == 0)):
            return 1
        return 0
    curr = patt[0]
    patt = patt[1:]
    clue, *new_clues = clues or [0]
    new_clues = tuple(new_clues)
    if curr == '?':
        return pattern('.' + patt, clues, size) + pattern('#' + patt, clues, size)
    if curr == '#':
        return 0 if size > clue else pattern(patt, clues, size + 1)
    if curr == '.':
        if size == 0:
            return pattern(patt, clues, 0)
        elif size == clue:
            return pattern(patt, new_clues, 0)
        return 0

def process(data: list[str, tuple[int]]) -> int:
    return pattern(patt=data[0], clues=data[1], size=0)

def partOne(data: list[list[list[str], list[int]]]) -> int:
    with Pool(processes=None) as pool:
        arrangements: map = pool.map_async(process, data)
        arrangements: list[int] = arrangements.get()
    return sum(arrangements)

def partTwo(data: list[list[list[str], list[int]]]) -> int:
    data: list[list[str, list[int]]] = [['?'.join([chars]*5), match*5] for chars, match in data]
    with Pool(processes=None) as pool:
        arrangements: map = pool.map_async(process, data)
        arrangements: list[int] = arrangements.get()
    return sum(arrangements)

if __name__ == "__main__":
    data: list[list[list[str], list[int]]] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
