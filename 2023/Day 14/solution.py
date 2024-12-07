TEST: str = open("test.txt")
DATA: str = open("input.txt")

def fetchData(data: str) -> tuple[str]:
    return tuple(data.splitlines())

def rotate(data: tuple[str]) -> list[str]:
        return list(map(''.join, zip(*data)))

def tilt(data: list[str], reverseTilt: bool) -> tuple[str]:
    return tuple(['#'.join(map(''.join, [sorted(fragment, reverse=reverseTilt) for fragment in row.split('#')])) for row in data])

def partOne(data: tuple[str]) -> int:
    data: tuple[str] = rotate(data)
    data = tilt(data, True)
    for _ in range(3):
        data = rotate(data)
    return sum([row.count('O')*num for num, row in enumerate(data[::-1], start=1)])

def partTwo(data: tuple[str]) -> int:
    iterations: int = 1_000_000_000
    memory, order = {}, {}
    for counter in range(iterations):
        for orientation in [True, True, False, False]:
            data: tuple[str] = tilt(rotate(data), reverseTilt=orientation)
        if data in memory:
            first, second = counter, memory[data]
            index: int = (iterations-first) % (second-first) + first
            return sum([row.count('O')*num for num, row in enumerate(order[index][::-1], start=1)])
        memory[data] = counter
        order[counter] = data

if __name__ == "__main__":
    data: list[str] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
