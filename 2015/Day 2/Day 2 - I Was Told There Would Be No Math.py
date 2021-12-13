from I_Was_Told_There_Would_Be_No_Math import DATA
from math import prod

def getData(data: str) -> list:
    for line in data.splitlines():
        if len(line) == 0: continue
        x, y, z = line.strip().split('x')
        yield [int(x), int(y), int(z)]

def partOne(data: list) -> int:
    total: int = 0
    for length, width, height in data:
        areaPaper: int = 2*length*width + 2*width*height + 2*length*height
        extraPaper: int = prod([side for number, side in enumerate(sorted([length, width, height])) if number != 2])
        total += areaPaper + extraPaper
    return total

def partTwo(data: list) -> int:
    total: int = 0
    for measurements in data:
        lengthRibbon: int = sum([side for number, side in enumerate(sorted(measurements)) if number != 2]) * 2
        bowRibbon: int = prod(measurements)
        total += lengthRibbon + bowRibbon
    return total

def main() -> None:
    print(partOne(getData(DATA)))
    print(partTwo(getData(DATA)))

if __name__ == "__main__":
    main()