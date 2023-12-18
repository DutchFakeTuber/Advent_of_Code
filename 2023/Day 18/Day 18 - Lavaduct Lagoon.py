from Lavaduct_Lagoon import TEST, DATA

def fetchData(data: str) -> list[str, int, str]:
    return [[line.split()[0], int(line.split()[1]), line.split()[2][1:-1]] for line in data.splitlines()]

def getCoord(previous: tuple[int, int], instruction: str, number: int) -> tuple:
    match instruction:
        case 'U': return (previous[0]-number, previous[1])
        case 'D': return (previous[0]+number, previous[1])
        case 'L': return (previous[0], previous[1]-number)
        case 'R': return (previous[0], previous[1]+number)

def calculate(c: list[tuple[int, int]]) -> int:
    # Get the area of the border.
    border: int = sum([abs(c[num-1][0]-row)+abs(c[num-1][1]-col) for num, (row, col) in enumerate(c[1:], start=1)])
    # Get the area using the Shoelace formula
    area: float = abs(sum([(c[num][0] * c[num+1][1]) - (c[num+1][0] * c[num][1]) for num in range(len(c)-1)])) / 2
    # Get the inside area using Picks' Theorem
    inside: float = abs(area*-1 + (border/2) - 1)
    return int(border+inside)

def partOne(instructions: list[str, int, str]) -> int:
    coordinates: list = [(0, 0)]
    for udlr, num, _ in instructions:
        coordinates.append(getCoord(coordinates[-1], udlr, num))
    return calculate(coordinates)

def partTwo(instructions: list[str, int, str]) -> int:
    coordinates: list = [(0, 0)]
    directions: dict = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}
    for _, _, rgb in instructions:
        coordinates.append(getCoord(
            previous=coordinates[-1],
            instruction=directions[int(rgb[-1])],
            number=int(rgb[1:-1], base=16)
        ))
    return calculate(coordinates)

if __name__ == "__main__":
    instructions: list[str, int, str] = fetchData(DATA)
    print(partOne(instructions))
    print(partTwo(instructions))
