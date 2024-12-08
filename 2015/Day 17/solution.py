import os
TEST: str = open(f"{os.path.dirname(os.path.realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{os.path.dirname(os.path.realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[int]:
    return [int(line) for line in data.splitlines() if len(line)]

def partOne(data: list[int]) -> int:
    ...

def partTwo(data: list[int]) -> int:
    ...

if __name__ == "__main__":
    data: list[int] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
