from os.path import dirname, realpath
from collections import deque
from itertools import groupby

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[int]:
    return list(map(int, data))

def scanDisk(data: list[int]) -> list[int | None]:
    data: deque = deque(data)
    disk: list[int | None] = []
    count: int = 0
    while data:
        number: int = data.popleft()
        disk += [count] * number
        if data:
            empty: int = data.popleft()
            disk += [None] * empty
        count += 1
    return disk

def findBlock(disk: deque, size: int) -> int | None:
    for idx, d in enumerate(reversed(disk)):
        if type(d[1]) == int and d[2] <= size:
            return len(disk) - idx - 1
    return None

def partOne(data: list[int]) -> int:
    disk: list[int | None] = scanDisk(data)
    emptyBlocks: deque = deque(num for num, block in enumerate(disk) if block is None)
    while emptyBlocks:
        block: int | None = disk.pop()
        if block == None:
            continue
        idx: int = emptyBlocks.popleft()
        if idx >= len(disk):
            disk.append(block)
            break
        disk[idx] = block
    return sum(map(lambda x: x[0]*x[1], zip(disk, range(len(disk)))))

def partTwo(data: list[int]) -> int:
    disk: deque = deque([[idx, val, len(num)] for idx, (val, num) in enumerate((val, list(num)) for val, num in groupby(scanDisk(data)))])
    moved: deque = deque()
    while disk:
        _, val, num = disk.popleft()
        if val is not None:
            moved.extend([val] * num)
            continue
        while num:
            index: int = findBlock(disk, size=num)
            if index is None:
                moved.extend([val] * num)
                break
            i, value, number = disk[index]
            disk[index] = [i, None, number]
            moved.extend([value] * number)
            num = num - number
    return sum((x[0] if x[0] is not None else 0) * x[1] for x in zip(moved, range(len(moved))))

if __name__ == "__main__":
    data: list[int] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
