from Blizzard_Basin import INPUT

def getData() -> list[list[str]]:
    return [[l for l in line] for line in INPUT.splitlines() if len(line) != 0]

class Blizzard:
    def __init__(self, basin: list[list[str]]) -> None:
        self.basin: list[list[str]] = basin
        topBottom: function = lambda pos: ['#' if i != pos else '.' for i in range(len(self.basin[0]))]
        middle: function = lambda: ['#' if i in [0, len(self.basin[0])-1] else '.' for i in range(len(self.basin[0]))]
        self.newBasin: function = lambda: [topBottom(1), *[middle() for _ in range(len(self.basin)-2)], topBottom(len(self.basin[0])-2)]

    def move(self, direction: str, row: int=0, col: int=0) -> tuple[int, int]:
        _r: function = lambda pos, wrap: row+pos if self.basin[row+pos][col] != '#' else wrap
        _c: function = lambda pos, wrap: col+pos if self.basin[row][col+pos] != '#' else wrap
        fuse: function = lambda basin, dir: dir if basin == '.' else [*basin, dir]
        match direction:
            case '^': self._basin[_r(-1, len(self.basin)-2)][col] = fuse(self._basin[_r(-1, len(self.basin)-2)][col], direction)
            case '>': self._basin[row][_c(+1, 1)] = fuse(self._basin[row][_c(+1, 1)], direction)
            case 'v': self._basin[_r(+1, 1)][col] = fuse(self._basin[_r(+1, 1)][col], direction)
            case '<': self._basin[row][_c(-1, len(self.basin[row])-2)] = fuse(self._basin[row][_c(-1, len(self.basin[row])-2)], direction)
            case _: pass

    def minute(self) -> None:
        self._basin: list[list[str]] = self.newBasin()
        for row in range(len(self.basin)):
            for col, char in enumerate(self.basin[row]):
                for c in [[char] if not isinstance(char, list) else char][0]:
                    self.move(c, row=row, col=col)
        self.basin = self._basin
    
    def process(self, start: tuple[int, int], end: tuple[int, int]) -> int:
        moves: set[tuple[int, int]] = {(start[0], start[1])}
        minutes: int = 0
        while True:
            minutes += 1
            self.minute()
            m = moves
            moves = set()
            while m:
                r, c = m.pop()
                if self.basin[r][c] == '.':
                    moves.add((r, c))
                if r-1 >= 0 and self.basin[r-1][c] == '.':
                    moves.add((r-1, c))
                if self.basin[r][c+1] == '.':
                    moves.add((r, c+1))
                if r+1 < len(self.basin) and self.basin[r+1][c] == '.':
                    moves.add((r+1, c))
                if self.basin[r][c-1] == '.':
                    moves.add((r, c-1))
            if end in moves:
                break
        return minutes

def partOne() -> int:
    _map = getData()
    blizzard: Blizzard = Blizzard(basin=_map)
    return blizzard.process(start=(0, 1), end=(len(blizzard.basin)-1, len(blizzard.basin[0])-2))

def partTwo() -> int:
    _map = getData()
    blizzard: Blizzard = Blizzard(basin=_map)
    start: tuple[int, int] = (0, 1)
    end: tuple[int, int] = (len(blizzard.basin)-1, len(blizzard.basin[0])-2)
    return sum(blizzard.process(start=s_e[0], end=s_e[1]) for s_e in [[start, end], [end, start], [start, end]])

def main() -> None:
    print(f'ANSWER PART ONE: {partOne()}')
    print(f'ANSWER PART TWO: {partTwo()}')
    
if __name__ == "__main__":
    main()
