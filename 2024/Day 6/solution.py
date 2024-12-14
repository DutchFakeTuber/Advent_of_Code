from os.path import dirname, realpath
from multiprocessing import Pool, cpu_count
from itertools import repeat

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[str]:
    return [line for line in data.splitlines() if len(line)]

class Guard:
    def __init__(self, field: list[str], startPosition: str='^', enableLoopDetect: bool=False) -> None:
        self.field: list[str] = field
        self.rows, self.cols = len(field), len(field[0])
        self.position: list[complex, str] = [complex(0, 0), startPosition] # [(row, col), direction]
        self.direction: dict[str, str] = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
        self.move: dict[str, complex] = {'^': complex(-1, 0), '>': complex(0, 1), 'v': complex(1, 0), '<': complex(0, -1)}
        self.outOfBounds: bool = False
        self.history: set[tuple[complex, str]] = set()
        self.coords: set[complex] = set()
        self.obstructions: set[complex] = set()
        # Used for Part Two
        self.enableLoopDetect: bool = enableLoopDetect
        self.loopDetected: bool = False # Return if loop is detected
    
    def __repr__(self) -> list[str]:
        field = ['.'*len(self.field[1]) for _ in range(len(self.field))]
        for row, col in list(set(map(lambda x: (int(x[0].real), int(x[0].imag)), self.history))):
            field[row] = field[row][:col] + '0' + field[row][col+1:]
        for row, col in list(set(map(lambda x: (int(x.real), int(x.imag)), self.obstructions))):
            field[row] = field[row][:col] + '#' + field[row][col+1:]
        for f in field:
            print(f)
        return "SUCCESS!"
    
    def getInformation(self, newObstruction: complex=None) -> object:
        self.position: list[complex, str] = [[complex(row, line.find(self.position[1])), self.position[1]] for row, line in enumerate(self.field) if line.find(self.position[1]) >= 0][0]
        self.startPosition: complex = self.position[0]
        self.obstructions: set[complex] = {complex(row, col) for col in range(len(self.field[0])) for row in range(len(self.field)) if self.field[row][col] == '#'}
        if newObstruction:
            self.obstructions.add(newObstruction)
        return self

    def inBounds(self, coord: complex) -> bool:
        return 0 <= coord.real < self.rows and 0 <= coord.imag < self.cols
    
    def loopDetect(self, position: tuple[complex, str]) -> bool:
        return position in self.history

    def walk(self) -> None:
        self.history.add((self.position[0], self.position[1]))
        if not self.enableLoopDetect:
            self.coords.add(self.position[0])

        if self.position[0]+self.move[self.position[1]] in self.obstructions:
            self.position[1] = self.direction[self.position[1]]
            return

        self.position[0] += self.move[self.position[1]]
        if not self.inBounds(self.position[0]):
            self.outOfBounds = True
        if self.loopDetect(tuple(self.position)):
            self.loopDetected = True

    def traverse(self) -> None:
        while not self.outOfBounds and not self.loopDetected:
            self.walk()

def partOne(data: list[str]) -> int:
    guard: Guard = Guard(data)
    guard.getInformation().traverse()
    return len(guard.coords)

def process(coords: list[complex], data: list[str]) -> bool:
    loops: int = 0
    for coord in coords:
        guard: Guard = Guard(data, enableLoopDetect=True)
        guard.getInformation(coord).traverse()
        loops += guard.loopDetected
    return loops

def partTwo(data: list[str]) -> int:
    guard: Guard = Guard(data, enableLoopDetect=False)
    guard.getInformation().traverse()
    guard.coords.remove(guard.startPosition)
    guard.coords = list(guard.coords)
    guard.coords = [guard.coords[num:num+50] for num in range(0, len(guard.coords), 50)]
    with Pool(cpu_count()) as pool:
        results = pool.starmap(process, zip(guard.coords, repeat(data)))
    return sum(results)

if __name__ == "__main__":
    data: list[str] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
