from heapq import heappop, heappush
from Chiton import DATA

def getData(data: str) -> list:
    return [[int(number) for number in line] for line in data.splitlines() if len(line) != 0]

def multiplyList(data: list, number: int=1) -> list:
    newData: list = [[0]*len(line)*number for line in data*number]
    for row in range(len(newData)):
        for col in range(len(newData[row])):
            newData[row][col] = (data[row % len(data)][col % len(data[0])] + row // len(data) + col // len(data[0]) - 1) % 9 + 1
    return newData

def isPresent(data: list, row: int, col: int) -> bool:
    return row >= 0 and row < len(data) and col >= 0 and col < len(data[0])

def riskCalc(data: list, visited: list) -> int:
    paths = [(0, 0, 0)]
    ROWS: list = [-1, 1, 0, 0]
    COLS: list = [0, 0, -1, 1]

    # Dijsktra's Algorithm
    while True:
        riskFactor, row, col = heappop(paths)
        if visited[row][col]: continue
        if row == len(data) - 1 and col == len(data[0]) - 1:
            break

        visited[row][col] = True
        for nR, nC in zip(ROWS, COLS):
            nextRow, nextCol = row + nR, col + nC
            if not isPresent(data, nextRow, nextCol): continue
            if visited[nextRow][nextCol]: continue
            heappush(paths, (riskFactor+data[nextRow][nextCol], nextRow, nextCol))

    return riskFactor

def partOne(data: list) -> int:
    data: list = multiplyList(data)
    visited: list = [[False for _ in range(len(data))] for _ in range(len(data[0]))]
    return riskCalc(data, visited)

def partTwo(data: list) -> int:
    newData: list = multiplyList(data, number=5)
    visited: list = [[False for _ in range(len(newData))] for _ in range(len(newData[0]))]
    return riskCalc(newData, visited)

def main() -> None:
    print(partOne(getData(DATA)))
    print(partTwo(getData(DATA)))

if __name__ == "__main__":
    main()