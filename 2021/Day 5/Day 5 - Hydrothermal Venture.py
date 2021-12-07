import numpy
from Hydrothermal_Venture import DATA

def getData(data: str) -> tuple:
    return [[[int(number) for number in coordinates.split(',')] for coordinates in line.split(' -> ')] for line in data.split('\n')]

def createDiagonal(xStart: int, yStart: int, xEnd: int, yEnd: int):
    xCount = 1 if xStart < xEnd else -1
    yCount = 1 if yStart < yEnd else -1

    currentX, currentY = xStart, yStart
    while currentX != xEnd:
        yield currentX, currentY
        currentX += xCount
        currentY += yCount
    
    yield currentX, currentY

def partOne(data: list, grid: list) -> int:
    for row in data:
        xStart, yStart, xEnd, yEnd = row[0][0], row[0][1], row[1][0], row[1][1]
        if yStart == yEnd:
            if xStart > xEnd:
                xStart, xEnd = xEnd, xStart
            grid[xStart:xEnd + 1, yStart] += 1
        elif xStart == xEnd:
            if yStart > yEnd:
                yStart, yEnd = yEnd, yStart
            grid[xStart, yStart:yEnd + 1] += 1
    
    return numpy.count_nonzero(grid > 1)

def partTwo(data: list, grid: list) -> int:
    for row in data:
        xStart, yStart, xEnd, yEnd = row[0][0], row[0][1], row[1][0], row[1][1]
        if yStart == yEnd:
            if xStart > xEnd:
                xStart, xEnd = xEnd, xStart
            grid[xStart:xEnd + 1, yStart] += 1
        elif xStart == xEnd:
            if yStart > yEnd:
                yStart, yEnd = yEnd, yStart
            grid[xStart, yStart:yEnd + 1] += 1
        else:
            for x, y in createDiagonal(xStart, yStart, xEnd, yEnd):
                grid[x, y] += 1
            
    return numpy.count_nonzero(grid > 1)

def main() -> None:
    data: list = getData(DATA)
    print(partOne(data, numpy.zeros((1000, 1000))))
    print(partTwo(data, numpy.zeros((1000, 1000))))

if __name__ == "__main__":
    main()