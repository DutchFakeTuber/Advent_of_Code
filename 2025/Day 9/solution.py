from os.path import dirname, realpath
from dataclasses import dataclass
from itertools import combinations

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()


@dataclass
class Coordinate:
    x: int
    y: int

class Raycasting:
    def __init__(self, data: list[Coordinate]) -> None:
        self.coords: list[Coordinate] = data
        # self.corners: int = len(self.coords)
        self.vertical: list = []
        self.horizontal: list = []
        
        for c1, c2 in zip(self.coords, [*self.coords[1:], self.coords[0]]):
            if c1.x == c2.x:
                y_min, y_max = min(c1.y, c2.y), max(c1.y, c2.y)
                self.vertical.append((c1.x, y_min, y_max))
            else:
                x_min, x_max = min(c1.x, c2.x), max(c1.x, c2.x)
                self.horizontal.append((c1.y, x_min, x_max))
    
    def isInside(self, x: float, y: float) -> bool:
        intersections: int = 0
        for cx, cy_min, cy_max in self.vertical:
            if cx <= x: continue
            if cy_min <= y < cy_max:
                intersections += 1
        return bool(intersections % 2)

    def intersect(self, x_min: int, y_min: int, x_max: int, y_max: int) -> bool:
        for cx, cy_min, cy_max in self.vertical:
            if x_min < cx < x_max:
                if max(cy_min, y_min) < min(cy_max, y_max):
                    return True
        for cy, cx_min, cx_max in self.horizontal:
            if y_min < cy < y_max:
                if max(cx_min, x_min) < min (cx_max, x_max):
                    return True
        return False

def fetchData(data: str) -> list[Coordinate]:
    return [Coordinate(*map(int, line.split(','))) for line in data.splitlines()]

def partOne(data: list[Coordinate]) -> int:
    return max([(1+abs(one.x-two.x))*(1+abs(one.y-two.y)) for one in data for two in data])

def partTwo(data: list[Coordinate]) -> int:
    raycasting: Raycasting = Raycasting(data)
    area: int = 0
    for c1, c2 in combinations(raycasting.coords, 2):
        new_area: int = (abs(c1.x - c2.x) + 1) * (abs(c1.y - c2.y) + 1)
        if max(area, new_area) == area: continue
        x_min, x_max, y_min, y_max = min(c1.x, c2.x), max(c1.x, c2.x), min(c1.y, c2.y), max(c1.y, c2.y)
        if raycasting.isInside(x_min + 0.5, y_min + 0.5):
            if not raycasting.intersect(x_min, y_min, x_max, y_max):
                area = new_area
    return area

if __name__ == "__main__":
    data: list[Coordinate] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
