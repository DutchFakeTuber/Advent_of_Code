from os.path import dirname, realpath
import heapq
from collections import deque

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[list[str]]:
    return [[char for char in line] for line in data.splitlines() if len(line)]

def findStartEnd(data: list[list[str]], start: str, end: str) -> list[list[int], list[int]]:
    return [[(row, col) for row in range(len(data)) for col in range(len(data[row])) if data[row][col] == char][0] for char in [start, end]]

def dijkstra_2d_with_path(data: list[list[int]], start: tuple[int], target: tuple[int], returnMap: bool=False):
    check: dict[str, list[list[int]]] = {'^': [['<', 0, -1], ['^', -1, 0], ['>', 0, 1]], '>': [['^', -1, 0], ['>', 0, 1], ['v', 1, 0]], 'v': [['>', 0, 1], ['v', 1, 0], ['<', 0, -1]], '<': [['v', 1, 0], ['<', 0, -1], ['^', -1, 0]]}
    data = [[float('inf') if data[row][col] == '#' else 0 for col in range(len(data[row]))] for row in range(len(data))]
    heap: list[tuple[int | str]] = [(0, start[0], start[1], '>')]
    visited: set = set()
    while heap:
        points, row, col, direction = heapq.heappop(heap)
        if (row, col) == target:
            break
        visited.add((row, col, direction))
        for d, r, c in check[direction]:
            ROW, COL = row+r, col+c
            if (ROW, COL, d) in visited: continue
            if data[ROW][COL] == float('inf'): continue
            newPoints: int = points + (1 if direction == d else 1001)
            if newPoints < (data[ROW][COL] if data[ROW][COL] != 0 else float('inf')):
                data[ROW][COL] = newPoints
                heapq.heappush(heap, (newPoints, ROW, COL, d))
                visited.add((ROW, COL, d))
    if returnMap:
        return data
    return points

def partOne(data: list[list[str]]) -> int:
    return dijkstra_2d_with_path(data, *findStartEnd(data, 'S', 'E'), returnMap=False)
    
def partTwo(data: list[list[str]]) -> int:
    start, end = findStartEnd(data, 'S', 'E')
    data: list[list[int]] = dijkstra_2d_with_path(data, start, end, returnMap=True)
    # Add padding
    data = [[*data[0], float('inf'), float('inf')]] + [[float('inf'), *data[num], float('inf')] for num in range(len(data))] + [[*data[-1], float('inf'), float('inf')]]
    start, end = (start[0]+1, start[1]+1), (end[0]+1, end[1]+1)
    visited: set = set()
    todo: deque = deque([end])
    while todo:
        row, col = todo.popleft()
        visited.add((row, col))
        if (row, col) == start: break
        for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if data[row][col] == data[row+r][col+c] + 1 or data[row][col] == data[row+r][col+c] + 1001:
                todo.append((row+r, col+c))
            if data[row][col] == data[row+r][col+c] + 1001:
                if data[row][col] == data[row+(r*2)][col+(c*2)] + 2:
                    todo.append((row+(r*2), col+(c*2)))
    return len(visited)

if __name__ == "__main__":
    data: list[list[str]] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
