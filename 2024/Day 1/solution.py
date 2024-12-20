from os.path import dirname, realpath
from collections import Counter

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[list[int, int]]:
    return [list(map(int, line.split('   '))) for line in data.splitlines() if len(line)]

def partOne(data: list[list[int, int]]) -> int:
    return sum([abs(l-r) for l, r in zip(sorted([num[0] for num in data]), sorted([num[1] for num in data]))])

def partTwo(data: list[list[int, int]]) -> int:
    appearance: Counter = Counter(location[1] for location in data)
    return sum(appearance[location[0]] * location[0] for location in data)

if __name__ == "__main__":
    data: list[list[int, int]] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
