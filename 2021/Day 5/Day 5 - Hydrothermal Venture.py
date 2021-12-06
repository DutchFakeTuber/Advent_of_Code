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
    
    overlap: int = 0
    for line in grid:
        for column in line:
            if column > 1:
                overlap += 1
    return overlap

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
            if xStart > xEnd:
                xStart, xEnd = xEnd, xStart
            if yStart > yEnd:
                yStart, yEnd = yEnd, yStart
            print(f"xStart: {xStart}, xEnd: {xEnd}; yStart: {yStart}, yEnd: {yEnd}, length: {xEnd-xStart}, {yEnd-yStart}; range len: {len([x for x in range(0, (yEnd-yStart)+1)])}")
            for Axis in range(0, yEnd - yStart):
                grid[xStart+Axis,yStart+Axis] += 1

    return numpy.count_nonzero(grid > 1)

def main() -> None:
    data: list = getData(DATA)
    print(partOne(data, numpy.zeros((1000, 1000))))
    print(partTwo(data, numpy.zeros((1000, 1000))))

if __name__ == "__main__":
    main()