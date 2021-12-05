from Hydrothermal_Venture import DATA
import sys

def generateGrid(xAxis: int, yAxis: int) -> list:
    return [[0 for _ in range(0, xAxis)] for _ in range(0, yAxis)]

def getData(data: str) -> tuple:
    return [[[int(number) for number in coordinates.split(',')] for coordinates in line.split(' -> ')] for line in data.split('\n')]
    '''
    print(start[0]) # To get the pair of coordinates
    print(start[0][0]) # To get one coordinates (this case the first)
    print(start[0][0][0]) # To get a single number
    '''

def partOne(data: list, grid: list) -> int:
    for row in data:
        if row[0][0] == row[1][0]:
            for number in range(abs(row[0][0] - row[1][0])):
                grid[row[0][1]][number] += 1
        else:
            for number in range(abs(row[0][0] - row[1][0])):
                grid[row[0][1]][number] += 1
    
    overlap: int = 0
    for line in grid:
        for column in line:
            if column > 1:
                overlap += 1
    return overlap

def main() -> None:
    data: list = getData(DATA)
    grid: list = generateGrid(1000, 1000)
    print(partOne(data, grid))

if __name__ == "__main__":
    main()