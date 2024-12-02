from Red_Nosed_Reports import TEST, DATA

def getData(data: str) -> list[list[str]]:
    return [list(map(int, line.split())) for line in data.splitlines() if len(line)]

def subtract(numbers: list[int]) -> list[int]:
    return [curr - prev for prev, curr in zip(numbers[:-1], numbers[1:])]

def compare(numbers: list[int]) -> tuple[list[bool], list[bool]]:
    return tuple([[1 <= n <= 3 and 1 <= n <= 3 for n in numbers], [-3 <= n <= -1 and -3 <= n <= -1 for n in numbers]])

def partOne(data: list[list[str]]) -> int:
    return sum([all(h) == (not all(l)) for h, l in [compare(subtract(n)) for n in data]])

def partTwo(data: list[list[str]]) -> int:
    check: function = lambda a, b: all(a) == (not all(b))
    safe: int = 0
    for numbers in data:
        if check(*compare(subtract(numbers))):
            safe += 1
            continue
        
        for pos in range(len(numbers)):
            if check(*compare(subtract(numbers[:pos] + numbers[pos+1:]))):
                safe += 1
                break

    return safe

if __name__ == "__main__":
    data: list[list[str]] = getData(DATA)
    print(partOne(data))
    print(partTwo(data))
