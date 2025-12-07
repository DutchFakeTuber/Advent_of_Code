from os.path import dirname, realpath
from copy import copy

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> tuple[list[list[int]], list[int]]:
    ranges, values = [], []
    for line in data.splitlines():
        if '-' in line: ranges.append(list(map(int, line.split('-'))))
        elif line.isalnum(): values.append(int(line))
    return ranges, values

def partOne(ranges: list[list[int]], values: list[int]) -> int:
    return len(set(tuple([val for start, end in ranges for val in values if start <= val <= end])))

def rangeExtender(data: list[list[int]]) -> list[list[int]]:
    def intersection(data: list[list[int]], value: list[int]):
        return set((pos for pos, (start, end) in enumerate(data) if (start <= value[0] <= end and value[0] <= end <= value[1]) or (value[0] <= start <= value[1] and start <= value[1] <= end) or (value[0] <= start and value[1] >= end) or (start <= value[0] and end >= value[1])))
    _data: list[list[int]] = copy(data)
    fresh: list[list[int]] = [_data.pop(0)]
    while len(_data):
        start, end = _data.pop(0)
        locations: list[int] = intersection(fresh, [start, end])
        if not len(locations):
            fresh.append([start, end])
            continue
        for loc in locations:
            fresh[loc] = [min(fresh[loc][0], start), max(fresh[loc][1], end)]
    return fresh

def partTwo(ranges: list[list[int]]) -> int:
    previous: list[list[int]] = []
    current: list[list[int]] = rangeExtender(ranges)
    while previous != current:
        previous = current
        current = rangeExtender(previous)
    return sum(end-start+1 for start, end in current)

if __name__ == "__main__":
    ranges, values = fetchData(DATA)
    print(partOne(ranges, values))
    print(partTwo(ranges))
