import numpy
from collections import deque
from Boiling_Boulders import INPUT

def getData() -> list[list[int]]:
    return [list(map(int, line.split(','))) for line in INPUT.splitlines() if len(line) != 0]

class Droplets:
    SIDES: list[list[int, int, int]] = [
        [-1, 0, 0], [1, 0, 0],
        [0, -1, 0], [0, 1, 0],
        [0, 0, -1], [0, 0, 1],
    ]
    def __init__(self, coords: list[list[int]]) -> None:
        counter: function = lambda n: [c[n] for c in coords]
        self.coords: list[list[int]] = coords
        self.cube: list[list[list[int]]] = numpy.zeros((max(counter(0)) + 3, max(counter(1)) + 3, max(counter(2)) + 3))
        self.offset: int = 1
        self.sides: int = 0
        self.queue: deque = deque([(0, 0, 0)])
        self.visited: set = set((0, 0, 0))
    
    def getGrid(self, p: bool=False) -> None:
        for x, y, z in self.coords:
            self.cube[x+self.offset][y+self.offset][z+self.offset] = 1
        if p:
            for x in self.cube:
                print(x)

    def countSides(self, val: int=0) -> None:
        for x in range(len(self.cube)):
            for y in range(len(self.cube[x])):
                for z in range(len(self.cube[x][y])):
                    if self.cube[x][y][z] == 1:
                        for _x, _y, _z in self.SIDES:
                            self.sides += 1 if self.cube[x+_x][y+_y][z+_z] == val else 0

    def breadthFirstSearch(self) -> None:
        while len(self.queue):
            x, y, z = self.queue.popleft()
            for _x, _y, _z in [[x+x_, y+y_, z+z_] for x_, y_, z_ in self.SIDES]:
                if not 0 <= _x < len(self.cube): continue
                elif not 0 <= _y < len(self.cube[_x]): continue
                elif not 0 <= _z < len(self.cube[_x][_y]): continue
                if (_x, _y, _z) in self.visited: continue
                value: int = self.cube[_x][_y][_z]
                if value == 1: continue
                self.visited.add((_x, _y, _z))
                self.queue.append((_x, _y, _z))
                self.cube[_x][_y][_z] = 2

def partOne() -> int:
    coords: list[list[int]] = getData()
    droplets: Droplets = Droplets(coords)
    droplets.getGrid()
    droplets.countSides(val=0)
    return droplets.sides

def partTwo() -> int:
    coords: list[list[int]] = getData()
    droplets: Droplets = Droplets(coords)
    droplets.getGrid()
    droplets.breadthFirstSearch()
    droplets.countSides(val=2)
    return droplets.sides

def main() -> None:
    print(f'ANSWER PART ONE: {partOne()}')
    print(f'ANSWER PART TWO: {partTwo()}')

if __name__ == "__main__":
    main()
