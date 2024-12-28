from os.path import dirname, realpath
from collections import deque
from itertools import product
from copy import deepcopy
from time import perf_counter_ns

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

class RaceCondition:
    def __init__(self, data: list[list[str]], cheatLength: int=2) -> None:
        self.cheatLength = cheatLength
        self.data: list[list[str]] = deepcopy(data)
        self.start, self.end = [[(row, col) for row in range(len(data)) for col in range(len(data[row])) if data[row][col] == char][0] for char in ['S', 'E']]
        self.data: list[list[str]] = [[self.data[row][col] if self.data[row][col] not in ('S', 'E') else '.' for col in range(len(self.data[row]))] for row in range(len(self.data))]
        self.walls: set = {(r, c) for r in range(len(data)) for c in range(len(data)) if data[r][c] == '#'}
        self.distance: list[tuple[int]] = [(row, col) for row, col in product(range(-self.cheatLength, self.cheatLength + 1), repeat=2) if abs(row) + abs(col) <= self.cheatLength]
        self.borders: list = [len(data), len(data[0])]
        self.shortcuts: dict[int, int] = dict()
    
    def cheatLessPath(self) -> None:
        todo: deque = deque([(self.start, {self.start: 0})])
        visited: set = set(tuple([self.start]))
        while todo:
            (row, col), path = todo.popleft()
            if (row, col) == self.end:
                self.path: dict = path
            for r, c in [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]:
                if (r, c) in self.walls or (r, c) in visited: continue
                visited.add((r, c))
                todo.append(((r, c), path | {(r, c): path[(row, col)] + 1}))

    def _manhattan(self, coords: tuple[int]) -> set:
        coordinates: set = set()
        row, col = coords
        for dx, dy in self.distance:
            if not (0 <= dx+row < self.borders[0] and 0 <= dy+col < self.borders[1]): continue
            if (dx+row, dy+col) in self.walls: continue
            if self.path[(row, col)] >= self.path[(dx+row, dy+col)]: continue
            coordinates.add((dx+row, dy+col))
        return coordinates

    def getShortcuts(self, length: int) -> None:
        for key, val in self.path.items():
            for sc in self._manhattan(key):
                shortcut: int = (self.path[sc] - val) - (abs(key[0]-sc[0]) + abs(key[1]-sc[1]))
                if shortcut < length: continue
                self.shortcuts.setdefault(shortcut, 0)
                self.shortcuts[shortcut] += 1

def fetchData(data: str) -> list[list[str]]:
    return [[char for char in line] for line in data.splitlines() if len(line)]

def parts(data: list[list[str]], cheatLength: int=20, shortcutLength: int=50) -> int:
    raceCondition: RaceCondition = RaceCondition(data, cheatLength=cheatLength)
    raceCondition.cheatLessPath()
    raceCondition.getShortcuts(shortcutLength)
    return sum(val for val in raceCondition.shortcuts.values())

if __name__ == "__main__":
    start = perf_counter_ns()
    data = fetchData(DATA)
    print(parts(data, cheatLength=2, shortcutLength=100))
    print(parts(data, cheatLength=20, shortcutLength=100))
    print((perf_counter_ns()-start)/1e9)
