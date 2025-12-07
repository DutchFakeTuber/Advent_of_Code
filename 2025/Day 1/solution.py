from os.path import dirname, realpath

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[int]:
    return [int(row[1:]) * -1 if row[0] == 'L' else int(row[1:]) for row in data.splitlines()]

def partOne(data: list[int], position: int=50, counter: int=0) -> int:
    for num in data:
        position = (position + num) % 100
        counter += position == 0
    return counter

def partTwo(data: list[int], position: int=50, counter: int=0) -> int:
    for num in data:
        pos = position + num
        counter += abs(pos) // 100 + (position and pos <= 0)
        position = pos % 100
    return counter

if __name__ == "__main__":
    data: list[int] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
