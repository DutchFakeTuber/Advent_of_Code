from os.path import dirname, realpath

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> ...:
    return ...

def partOne(data: ...) -> int:
    return ...

def partTwo(data: ...) -> int:
    return ...

if __name__ == "__main__":
    data: ... = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
