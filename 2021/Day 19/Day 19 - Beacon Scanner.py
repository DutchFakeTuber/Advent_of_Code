from itertools import combinations, permutations, product
from Beacon_Scanner import DATA, TEST

class Orientation:
    XYZ: list[tuple] = list(set(permutations([1,1,1,-1,-1,-1], 3))) # Set is used to remove duplicates
    POS: list[tuple] = [(0,1,2), (1,2,0), (2,0,1)]

def getData(data: str) -> list:
    return [
        [eval(line) for line in beacons.splitlines() if len(line) != 0 and '--' not in line]
        for beacons in data.split('\n\n')
    ]

def partOne(data: list) -> int: ...


def partTwo(data: list) -> int: ...

def main() -> None:
    data = getData(DATA)
    print(list(product(Orientation.XYZ, Orientation.POS)))
    print(partOne(data))
    print(partTwo(data))

if __name__ == "__main__":
    main()