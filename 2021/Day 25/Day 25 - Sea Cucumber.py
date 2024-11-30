import copy
from itertools import product
from Sea_Cucumber import INPUT, TEST

def getData(data: str) -> list[list[str]]:
    return [[char for char in line] for line in data.splitlines() if len(line) != 0]

def moveCucumbers(seafloor: list[list[str]], direction: str = ">") -> list[list[str]]:
    maxRow = len(seafloor)
    maxCol = len(seafloor[0])
    if direction == ">":
        check: function = lambda row, col: (row, 0) if (col + 1) == maxCol else (row, col + 1)
    else:
        check: function = lambda row, col: (0, col) if (row + 1) == maxRow else (row + 1, col)
    steps: dict = dict()
    for row, col in product(range(maxRow), range(maxCol)):
        if seafloor[row][col] == direction:
            r, c = check(row, col)
            if seafloor[r][c] == '.':
                steps[(row, col)] = (r, c)

    for originalPos, moveTo in steps.items():
        seafloor[originalPos[0]][originalPos[1]] = '.'
        seafloor[moveTo[0]][moveTo[1]] = direction
    
    if direction == ">":
        seafloor = moveCucumbers(seafloor, "v")
    return seafloor

def partOne(seafloor: list[list[str]]) -> int:
    counter: int = 0
    prevSeafloor: list[list[str]] = [[""]]
    while prevSeafloor != seafloor:
        prevSeafloor = copy.deepcopy(seafloor)
        seafloor: list[list[str]] = moveCucumbers(seafloor, direction=">")
        # seafloor: list[list[str]] = moveSouth(seafloor)
        counter += 1
    return counter

if __name__ == "__main__":
    seafloor: list[list[str]] = getData(INPUT)
    print(partOne(seafloor))
    print("Part Two: 50 STARS!")
