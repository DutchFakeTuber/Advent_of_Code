TEST: str = open("test.txt")
DATA: str = open("input.txt")

def getData() -> list[list]:
    func: function = lambda _str, _int=None: [str(_str), None if not _int else int(_int)]
    return [func(*line.split(' ')) for line in DATA.splitlines() if len(line) != 0]

def partOne() -> int:
    operations: list[list] = getData()
    ticks: list = [0]
    x: int = 1
    for op in operations:
        match op[0]:
            case 'noop':
                ticks += [x]
            case 'addx':
                ticks += [x, x]
                x += op[1]
    return sum([num*ticks[num] for num in [20, 60, 100, 140, 180, 220]])

def partTwo() -> int:
    beam: function = lambda t: [t//40, t%40]
    check: function = lambda b, s: '#' if b[1] in [s -1, s, s + 1] else '.'
    operations: list[list] = getData()
    screen: list = [['.'for _ in range(40)] for _ in range(6)]
    ticks: int = 0
    sprite: list = 1
    for op in operations:
        match op[0]:
            case 'noop':
                screen[beam(ticks)[0]][beam(ticks)[1]] = check(beam(ticks), sprite)
                ticks += 1
            case 'addx':
                for _ in range(2):
                    screen[beam(ticks)[0]][beam(ticks)[1]] = check(beam(ticks), sprite)
                    ticks += 1
                sprite = sprite + op[1]
    return ["".join(s) for s in screen]
    
def main() -> None:
    print(f'ANSWER PART ONE: {partOne()}')
    print(f'ANSWER PART TWO:')
    [print(s) for s in partTwo()]

if __name__ == "__main__":
    main()
