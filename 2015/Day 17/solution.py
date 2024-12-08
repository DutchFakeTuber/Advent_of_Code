import os
from itertools import combinations

TEST: str = open(f"{os.path.dirname(os.path.realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{os.path.dirname(os.path.realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[int]:
    return [int(line) for line in data.splitlines() if len(line)]

def combination(data: list[int]) -> list[tuple[int]]:
    return [comb for amount in range(1, len(data) + 1) for comb in combinations(data, amount) if sum(comb) == 150]

def partOne(data: list[int]) -> int:
    return len(combination(data))

def partTwo(data: list[int]) -> int:
    combs: list[int] = list(map(lambda c: len(c), combination(data)))
    return sum(1 for c in combs if c == min(combs))

if __name__ == "__main__":
    data: list[int] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
