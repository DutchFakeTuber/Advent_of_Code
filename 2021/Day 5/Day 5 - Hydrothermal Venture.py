import numpy
import sys
from Hydrothermal_Venture import DATA

def getData(data: str) -> tuple:
    return [[[int(number) for number in coordinates.split(',')] for coordinates in line.split(' -> ')] for line in data.split('\n')]

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
            if xStart > xEnd: xStart += 1
            else: xEnd += 1
            if yStart > yEnd: yStart += 1
            else: yEnd += 1

            xAxis = [x for x in range(xStart, xEnd, 1 if xStart < xEnd else -1)]
            yAxis = [y for y in range(yStart, yEnd, 1 if yStart < yEnd else -1)]
            for x, y in zip(xAxis, yAxis):
                grid[x ,y] += 1

    return numpy.count_nonzero(grid > 1)

def main() -> None:
    data: list = getData(DATA)
    # print(partOne(data, numpy.zeros((1000, 1000))))
    print(partTwo(data, numpy.zeros((1000, 1000))))

if __name__ == "__main__":
    main()