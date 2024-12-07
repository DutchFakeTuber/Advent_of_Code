TEST: str = open("test.txt")
DATA: str = open("input.txt")

def fetchData(data: str) -> dict[list[dict[str, int]]]:
    return {int(line.split(':')[0].strip('Game ')): [{''.join(x for x in c if x.isalpha()): int(''.join(x for x in c if x.isnumeric())) for c in cube} for cube in [l.split(',') for l in line.split(':')[1].replace(' ', '').split(';')]] for line in data.splitlines()}

def partOne(data: dict[list[dict[str, int]]], inHand: dict[str, int]) -> int:
    return sum(num for num, game in data.items() if all(all(False if inHand[color] < amount else True for color, amount in round.items()) for round in game))

def partTwo(data: dict[list[dict[str, int]]]) -> int:
    return sum(max([r.get('red', 0) for r in game])*max([r.get('green', 0) for r in game])*max([r.get('blue', 0) for r in game]) for game in data.values())

if __name__ == "__main__":
    data: dict[list[dict[str, int]]] = fetchData(DATA)
    print(partOne(data, inHand={'red': 12, 'green': 13, 'blue': 14}))
    print(partTwo(data))
