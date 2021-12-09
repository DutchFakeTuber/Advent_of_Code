from Smoke_Basin import DATA

def getData(data: str) -> list:
    return [[int(number) for number in line] for line in data.split('\n')]
    """
    100 Rows
    100 Columns
    """

def getCoords(data: list, row: int, column: int) -> tuple:
    try: left: int = data[row][column - 1]
    except: left: int = None

    try: right: int = data[row][column + 1]
    except: right: int = None

    try: up: int = data[row - 1][column]
    except: up: int = None

    try: down: int = data[row + 1][column]
    except: down: int = None

    return  left, right, up, down

def partOne(data: list) -> int:
    lowPoints: list = []
    for row in range(len(data)):
        for column, number in enumerate(data[row]):
            if row == 0:
                if column == 0:
                    _, right, _, down = getCoords(data, row, column)
                    if number < right and number < down: lowPoints.append(number)

                elif column == len(data[row]) - 1:
                    left, _, _, down = getCoords(data, row, column)
                    if number < left and number < down: lowPoints.append(number)
                
                else:
                    left, right, _, down = getCoords(data, row, column)
                    if number < left and number < right and number < down: lowPoints.append(number)
                    
            elif row == len(data[row]) - 1: ...
            else: ...
    print(lowPoints)

def partTwo(data: list) -> int: ...

def main() -> None:
    data = getData(DATA)
    print(partOne(data))
    print(partTwo(data))

if __name__ == "__main__":
    main()