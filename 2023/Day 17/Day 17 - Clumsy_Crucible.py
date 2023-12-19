from Clumsy_Crucible import TEST, DATA
from heapq import heappush, heappop

def fetchData(data: str) -> list[list[int]]:
    return [[int(num) for num in line] for line in data.splitlines()]

class Crucible:
    def __init__(self, city: list[list[int]], start: tuple[int]=(0, 0), required: tuple[int]=(0, 3)) -> None:
        self.city: list[list[int]] = city
        self.visited: set = set()
        self.queue: list = []
        # (HeatLoss, (nextRow, nextCol), direction, steps)
        self.queue.append((city[start[0]+1][start[1]], (start[0]+1, start[1]), 'v', 1))
        self.queue.append((city[start[0]][start[1]+1], (start[0], start[1]+1), '>', 1))
        self.borders: tuple[tuple[int]] = ((-1, len(city)), (-1, len(city[0])))
        self.nextMove: dict = {(-1, 0): '^', (1, 0): 'v', (0, -1): '<', (0, 1): '>'}
        self.stop = (len(city)-1, len(city[0])-1)
        self.required: tuple[int] = required

    def within(self, row: int, col: int) -> bool:
        withinRow: bool = self.borders[0][0] < row < self.borders[0][1]
        withinCol: bool = self.borders[1][0] < col < self.borders[1][1]
        return True if withinRow and withinCol else False
    
    def moves(self, move: str) -> tuple[tuple[int]]:
        match move:
            case '^': return ((-1, 0), (0, -1), (0, 1))
            case '>': return ((-1, 0), (1, 0), (0, 1))
            case 'v': return ((1, 0), (0, -1), (0, 1))
            case '<': return ((-1, 0), (1, 0), (0, -1))
            case _: return ((-1, 0), (1, 0), (0, -1), (0, 1))
    
    def path(self) -> int:
        while len(self.queue):
            (heatLoss, (row, col), direction, steps) = heappop(self.queue)
            if self.stop == (row, col):
                return heatLoss
            if ((row, col), direction, steps) in self.visited:
                continue
            self.visited.add(((row, col), direction, steps))
            
            for r, c in self.moves(direction):
                if not self.within(row+r, col+c):
                    continue
                _nextMove = self.nextMove[(r, c)]
                if _nextMove == direction and steps < self.required[1]:
                    heappush(self.queue, (heatLoss + self.city[row+r][col+c], (row+r, col+c), direction, steps+1))
                elif _nextMove != direction and self.required[0] <= steps <= self.required[1]:
                    heappush(self.queue, (heatLoss + self.city[row+r][col+c], (row+r, col+c), _nextMove, 1))

def partOne(city: list[list[int]]) -> int:
    crucible: Crucible = Crucible(city, start=(0, 0), required=(0, 3))
    return crucible.path()

def partTwo(city: list[list[int]]) -> int:
    crucible: Crucible = Crucible(city, start=(0, 0), required=(4, 10))
    return crucible.path()

if __name__ == "__main__":
    data: list[list[int]] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
