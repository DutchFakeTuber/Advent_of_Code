from multiprocessing import Pool

TEST: str = open("test.txt")
DATA: str = open("input.txt")

def fetchData(data: str) -> list[list[str]]:
    return [[char for char in line] for line in data.splitlines()]

class Contraption:
    def __init__(self, field: list[list[str]], start=(0, 0, '>')) -> None:
        self.field: list[list[str]] = field
        self.clone: set = set()
        self.moves: set[tuple[int, int, str]] = set([start])
        self.beenHere: set = set()
        self.change: dict = {
            '.': {'^': ['^'], '>': ['>'], 'v': ['v'], '<': ['<']},
            '/': {'^': ['>'], '>': ['^'], 'v': ['<'], '<': ['v']},
            '\\': {'^': ['<'], '>': ['v'], 'v': ['>'], '<': ['^']},
            '|': {'^': ['^'], '>': ['^', 'v'], 'v': ['v'], '<': ['^', 'v']},
            '-': {'^': ['<', '>'], '>': ['>'], 'v': ['<', '>'], '<': ['<']},
        }
        self.border: tuple[tuple[int], tuple[int]] = ((0, len(field)-1), (0, len(field[0])-1))

    def move(self) -> None:
        row, col, direction = self.moves.pop()
        # Check if the move is in the field
        if self.border[0][0] <= row <= self.border[0][1] and \
                self.border[1][0] <= col <= self.border[1][1]:
            if (row, col, direction) not in self.beenHere:
                self.clone.add((row, col))
                self.beenHere.add((row, col, direction))    
                nextMoves: list = self.change[self.field[row][col]][direction]
                for nm in nextMoves:
                    match nm:
                        case '^': self.moves.add((row-1, col, nm))
                        case '>': self.moves.add((row, col+1, nm))
                        case 'v': self.moves.add((row+1, col, nm))
                        case '<': self.moves.add((row, col-1, nm))

def process(args: tuple) -> int:
    contraption: Contraption = Contraption(*args)
    while len(contraption.moves):
        contraption.move()
    return len(contraption.clone)

def partOne(field: list[list[str]]) -> int:
    return process((field, (0, 0, '>')))

def partTwo(field: list[list[str]]) -> int:
    maxRow: int = len(field)-1
    maxCol: int = len(field[0])-1
    moves: list[tuple[int, int, str]] = [*[(0, col, 'v') for col in range(len(field[0]))],
                                         *[(row, 0, '>') for row in range(len(field))],
                                         *[(row, maxCol, '<') for row in range(len(field))],
                                         *[(maxRow, col, '^') for col in range(len(field[0]))]]
    moves: tuple = ((field, m) for m in moves)
    with Pool(processes=None) as pool:
        counter: map = pool.map_async(process, moves)
        counter: int = max(counter.get())
    return counter

if __name__ == "__main__":
    field: list[list[str]] = fetchData(DATA)
    print(partOne(field))
    print(partTwo(field))
