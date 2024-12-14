from os.path import dirname, realpath
from re import findall
from functools import reduce
from operator import mul
from scipy.stats import entropy
import numpy as np

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> dict[tuple, list[tuple[int]]]:
    robots: list[list[int]] = [list(map(int, findall(r'-?\d+', line))) for line in data.splitlines() if len(line)]
    field: dict[tuple, list[tuple[int]]] = dict()
    for robot in robots:
        field.setdefault((robot[0], robot[1]), []).append((robot[2], robot[3]))
    return field

def calculateQuadrants(field: dict[tuple, list[tuple[int]]], x: int, y: int) -> list[int]:
    position: function = lambda f: [0 <= f[0] < x//2 and 0 <= f[1] < y//2, 0 <= f[0] < x//2 and y//2+1 <= f[1] < y, x//2+1 <= f[0] < x and 0 <= f[1] < y//2, x//2+1 <= f[0] < x and y//2+1 <= f[1] < y, True].index(True)
    quadrant: list = [0, 0, 0, 0, 0] # Discard last number later
    for f, robots in field.items():
        quadrant[position(f)] += len(robots)
    return quadrant[:4]

def moveRobots(currentField: dict[tuple, list[tuple[int]]], X: int, Y: int) -> dict[tuple, list[tuple[int]]]:
    newField: dict[tuple, list[tuple[int]]] = dict()
    for coords, robots in currentField.items():
        for robot in robots:
            newField.setdefault(((X+coords[0]+robot[0])%X, (Y+coords[1]+robot[1])%Y), []).append(robot)
    return newField

def createField(robots: dict[tuple, list[tuple[int]]], X: int, Y: int) -> np.ndarray:
    field: np.ndarray = np.zeros((X, Y), dtype=np.int8)
    for (x, y), robot in robots.items():
        field[x, y] = len(robot)
    return field

def partOne(data: dict[tuple, list[tuple[int]]], seconds: int=100, size: list=[101, 103]) -> int:
    field: dict[tuple, list[tuple[int]]] = data
    for _ in range(seconds):
        field: dict[tuple, list[tuple[int]]] = moveRobots(field, *size)
    return reduce(mul, calculateQuadrants(field, *size))

def partTwo(data: dict[tuple, list[tuple[int]]], size=[101, 103]) -> int:
    robots: dict[tuple, list[tuple[int]]] = data
    measuredEntropy: list[float] = [0, float('inf')]
    for seconds in range(1, mul(*size)):
        robots: dict[tuple, list[tuple[int]]] = moveRobots(robots, *size)
        field: np.ndarray = createField(robots, *size).flatten()
        e: np.float64 = entropy(np.unique(field, return_counts=True)[1], base=None)
        if e < measuredEntropy[1]:
            measuredEntropy = [seconds, e]
    return measuredEntropy[0]

if __name__ == "__main__":
    data: dict[tuple, list[tuple[int]]] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
