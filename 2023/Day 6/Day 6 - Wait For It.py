from math import floor, ceil
from Wait_For_It import TEST, DATA

def fetchData(data: str, partOne: bool=True) -> list[list[int]]:
    time: list = data.splitlines()[0].strip('Time:').split()
    distance: list = data.splitlines()[1].strip('Distance:').split()
    if partOne:
        return [[int(time), int(distance)] for time, distance in zip(time, distance)]
    return [[int(''.join(time)), int(''.join(distance))]]

def calculate(data: list[list[int]]) -> int:
    total: int = 1
    for time, distance in data:
        start: int = (-time + (time**2 - 4*distance)**.5)/-2
        start = ceil(start) + 1 if start == ceil(start) else ceil(start)
        end: int = (-time - (time**2 - 4*distance)**.5)/-2
        end = floor(end) - 1 if end == floor(end) else floor(end)
        total *= end - start + 1
    return total

if __name__ == "__main__":
    print(calculate(fetchData(DATA, partOne=True)))
    print(calculate(fetchData(DATA, partOne=False)))
