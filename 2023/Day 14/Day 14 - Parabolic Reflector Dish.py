from itertools import count
from Parabolic_Reflector_Dish import TEST, DATA
from time import perf_counter

def fetchData(data: str) -> tuple[str]:
    return tuple(data.splitlines())

def rotate(data: tuple[str], count: int = 1) -> tuple[str]:
    for _ in range(count):
        data: tuple[str] = tuple([''.join(row) for row in zip(*data)])
    return data

def tilt(data: tuple[str], reverseTilt: bool) -> tuple[str]:
    tilted: list = []
    for row in data:
        rowTilt = [sorted(fragment, reverse=reverseTilt) for fragment in row.split('#')]
        tilted.append('#'.join(map(''.join, rowTilt)))
    return tuple(tilted)

def partOne(data: tuple[str]) -> int:
    data: tuple[str] = rotate(data)
    data = tilt(data, True)
    data = rotate(data, count=3)
    return sum([row.count('O')*num for num, row in enumerate(data[::-1], start=1)])

def partTwo(data: tuple[str]) -> int:
    iterations: int = 1_000_000_000
    memory, order = {}, {}
    for counter in count(1):
        for orientation in [True, True, False, False]:
            data: tuple[str] = rotate(data)
            data: tuple[str] = tilt(data, reverseTilt=orientation)
        if data in memory:
            first, second = counter, memory[data]
            index: int = (iterations-first) % (second-first) + first
            return sum([row.count('O')*num for num, row in enumerate(order[index][::-1], start=1)])
        memory[data] = counter
        order[counter] = data
        counter += 1

if __name__ == "__main__":
    data: list[str] = fetchData(DATA)
    start = perf_counter()
    print(partOne(data))
    print(partTwo(data))
    print(perf_counter()-start)