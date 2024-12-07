TEST: str = open("test.txt")
DATA: str = open("input.txt")

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
