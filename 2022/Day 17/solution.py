from tqdm import tqdm

TEST: str = open("test.txt")
DATA: str = open("input.txt")

def getData() -> list:
    return [char for char in DATA]

class Flow:
    HBAR: list[list[str]] = [['.','.','.','.'],['.','.','.','.'],['.','.','.','.'],['#','#','#','#']]
    CROSS: list[list[str]] = [['.','.','.','.'],['.','#','.','.'],['#','#','#','.'],['.','#','.','.']]
    INVERSEL: list[list[str]] = [['.','.','.','.'],['.','.','#','.'],['.','.','#','.'],['#','#','#','.']]
    VBAR: list[list[str]] = [['#','.','.','.'],['#','.','.','.'],['#','.','.','.'],['#','.','.','.']]
    BLOCK: list[list[str]] = [['.','.','.','.'],['.','.','.','.'],['#','#','.','.'],['#','#','.','.']]
    def __init__(self, operations: list, width: int=7) -> None:
        self.operations: list = operations
        self.pieces: list[list[list[str]]] = [self.HBAR, self.CROSS, self.INVERSEL, self.VBAR, self.BLOCK]
        self.jets: int = 0
        self.total: int = 0
        self.width: int = width
        self.chamber: list[list[str]] = [['.' if n != 3 + len(self.HBAR) else '$' for _ in range(self.width)] for n in range(4 + len(self.HBAR))]
        self.starts: dict = {0: [0]}
    
    def reset(self) -> None:
        self.jets: int = 0
        self.total: int = 0
        self.chamber: list[list[str]] = [['.' if n != 3 + len(self.HBAR) else '$' for _ in range(self.width)] for n in range(4 + len(self.HBAR))]
        self.starts: dict = {0: [0]}

    def rotateOperations(self, step: int) -> str:
        return self.operations[step % len(self.operations)]

    def rotatePieces(self, step: int) -> list[list[str]]:
        return self.pieces[step % len(self.pieces)]

    def createEmptyRows(self) -> None:
        rowsNeeded: int = 2 + len(self.HBAR)
        for num, row in enumerate(self.chamber):
            if '$' in row:
                rowsNeeded -= num - 1
                break
        for _ in range(rowsNeeded):
            self.chamber = [['.' for _ in range(self.width)], *self.chamber]
    
    def gasJet(self, pos: list[int, int], d: str) -> None:
        coords: list[list[int]] = [[row, col] for col in range(len(self.chamber[0])) for row in range(pos[0], pos[1] + 1) if self.chamber[row][col] == '#']
        for row, col in coords:
            if (d == '<' and col == 0) or (d == '>' and col == len(self.chamber[row]) - 1): return
            elif self.chamber[row][col - 1 if d == '<' else col + 1] == '$': return
        for row, col in coords: self.chamber[row][col] = '.'
        for row, col in coords: self.chamber[row][col - 1 if d == '<' else col + 1] = '#'
        
    def fall(self, pos: list[int, int]) -> tuple[list[int, int], bool]:
        ok: bool = True
        coords: list[list[int]] = [[row, col] for col in range(len(self.chamber[0])) for row in range(pos[0], pos[1] + 1) if self.chamber[row][col] == '#']
        for row, col in coords:
            if ok and self.chamber[row + 1][col] == '$': ok = False
        if not ok:
            for row, col in coords:
                self.chamber[row][col] = '$'
            return pos, True
        for row, col in coords: self.chamber[row][col] = '.'
        for row, col in coords: self.chamber[row + 1][col] = '#'
        return [pos[0] + 1, pos[1] + 1], False

    def place(self, count: int=2022) -> int:
        self.reset()
        for rock in tqdm(range(count)):
            self.jets = self.jets % len(self.operations)
            self.createEmptyRows()
            if len(self.chamber) > 100:
                self.total += len(self.chamber) - 99
                self.chamber = self.chamber[:99]
            if rock % len(self.pieces) == 0 and rock != 0:
                if self.chamber[7][4] == '$':
                    if self.jets in self.starts:
                        self.starts[self.jets] += [rock]
                    else:
                        self.starts[self.jets] = [rock]
            piece = self.rotatePieces(rock)
            for n in range(4):
                self.chamber[n] = [*self.chamber[n][:2], *piece[n], *self.chamber[n][6:]]
            row: list = [0, 3]
            done: bool = False
            while not done:
                direction = self.rotateOperations(self.jets)
                self.jets += 1
                self.gasJet(row, direction)
                row, done = self.fall(row)
        return sum(1 for row in self.chamber if '$' in row) + self.total - 1

def partOne() -> int:
    steps: list = getData()
    flow: Flow = Flow(steps, width=7)
    return flow.place(count=2022)

def partTwo() -> int:
    count: int = 1_000_000_000_000
    steps: list = getData()
    flow: Flow = Flow(steps, width=7)
    iteration: int = len(steps) * len(flow.pieces)
    flow.place(count=iteration)
    starts: dict = flow.starts
    largest: int = max(x for x in starts.keys())
    repetition: int = starts[largest][-1] - starts[largest][-2]
    growth: int = flow.place(starts[largest][-1]) - flow.place(starts[largest][-2])
    start = count % repetition + iteration//repetition*repetition
    return flow.place(start) + growth * (count-start)//repetition

def main() -> None:
    print(f'ANSWER PART ONE: {partOne()}')
    print(f'ANSWER PART TWO: {partTwo()}')

if __name__ == "__main__":
    main()
