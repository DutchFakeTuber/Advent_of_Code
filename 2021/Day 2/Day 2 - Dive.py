from Dive import DATA

def getData(data: str) -> list:
    return [line.split() for line in data.split("\n")]

def partOne(data: list) -> int:
    submarine: dict = {
        'forward': 0,
        'depth': 0,
    }
    for instruction in data:
        if instruction[0] != 'forward':
            if instruction[0] == 'down':
                submarine['depth'] += int(instruction[1])
            else: submarine['depth'] -= int(instruction[1])
        else:
            submarine[instruction[0]] += int(instruction[1])
    return submarine['forward'] * submarine['depth']

def partTwo(data: list) -> int:
    submarine: dict = {
        'forward': 0,
        'depth': 0,
        'aim': 0,
    }
    for instruction in data:
        if instruction[0] != 'forward':
            if instruction[0] == 'down':
                submarine['aim'] += int(instruction[1])
            else: submarine['aim'] -= int(instruction[1])
        else:
            submarine[instruction[0]] += int(instruction[1])
            submarine['depth'] = submarine['depth'] + (int(instruction[1]) * submarine['aim'])
    return submarine['forward'] * submarine['depth']


def main() -> None:
    data: list = getData(DATA)
    print(partOne(data))
    print(partTwo(data))

if __name__ =="__main__":
    main()