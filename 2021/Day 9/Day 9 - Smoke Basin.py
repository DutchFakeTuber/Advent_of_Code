from Smoke_Basin import DATA

def getData(data: str) -> list:
    return [[int(number) for number in line] for line in data.split('\n')]

def partOne(data: list) -> int: ...

def partTwo(data: list) -> int: ...

def main() -> None:
    data = getData(DATA)
    print(partOne(data))
    print(partTwo(data))

if __name__ == "__main__":
    main()