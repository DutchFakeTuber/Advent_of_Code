from Historian_Hysteria import TEST, DATA

def fetchData(data: str) -> list[list[int, int]]:
    return [list(map(int, line.split('   '))) for line in data.splitlines() if len(line)]

def partOne(data: list[list[int, int]]) -> int:
    return sum([abs(l-r) for l, r in zip(sorted([num[0] for num in data]), sorted([num[1] for num in data]))])

def partTwo(data: list[list[int, int]]) -> int:
    appearance: dict = {location[0]: sum([1 if location[0] == loc[1] else 0 for loc in data]) for location in data}
    return sum(appearance[location[0]] * location[0] for location in data)

if __name__ == "__main__":
    data: list[list[int, int]] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
