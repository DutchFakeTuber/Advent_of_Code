TEST: str = open("test.txt")
DATA: str = open("input.txt")

def getData(input: str=DATA) -> list[list]:
    return [[list(map(int, l.split(','))) for l in line.split(' -> ')] for line in input.splitlines() if len(line) != 0]

class Map:
    def __init__(self, coords: list[list[list[int, int]]], start: list[int, int]=[500, 0], wideMap: bool=False) -> None:
        self.coords: list[list[list[int, int]]] = coords
        self.start: list[int, int] = start
        self.wideMap: bool = wideMap
        _c: function = lambda n: (coords[r][c][n] for r in range(len(coords)) for c in range(len(coords[r])))
        self.y_min: int = start[1] if min(_c(1)) > start[1] else min(_c(1))
        self.y_max: int = max(_c(1)) + 3
        self.x_min: int = min(_c(0)) - 1 if not self.wideMap else (min(_c(0)) - 1) - (self.y_max - self.y_min)
        self.x_max: int = max(_c(0)) + 2 if not self.wideMap else (max(_c(0)) + 2) + (self.y_max - self.y_min)
        self.sandCounter: int = 0
    
    def generate(self) -> None:
        self.underground: list[str] = [['.' for _ in range(self.x_max - self.x_min)] for _ in range(self.y_max - self.y_min)]  # Create empty map
        self.underground[self.start[1] - self.y_min][self.start[0] - self.x_min] = '+'  # Set start point
        if self.wideMap:
            self.underground[-1] = ['#' for _ in range(self.x_max - self.x_min)]
        for rock in self.coords:  # Get rock formation [lines from input]
            xy_ss: function = lambda r, c, _xy: (min([rock[r-1][c], rock[r][c]]) - _xy, max([rock[r-1][c], rock[r][c]]) - _xy)
            for n in range(1, len(rock)):  # Get start and end of formation
                x_start, x_stop = xy_ss(n, 0, self.x_min)
                y_start, y_stop = xy_ss(n, 1, self.y_max)
                if x_stop - x_start > 0:
                    for char in range((x_stop - x_start) + 1):
                        self.underground[y_start][char+x_start] = '#'
                else:
                    for char in range((y_stop - y_start) + 1):
                        self.underground[char+y_start][x_start] = '#'
    
    def goDown(self, curr: list[int, int]) -> tuple[list[int, int], bool]:
        return tuple([[curr[0], curr[1]+1], True]) if self.underground[curr[1] + 1][curr[0]] == '.' else tuple([curr, False])
    
    def checkDiagonal(self, curr: list[int, int], left: bool=True) -> tuple[list[int, int], bool]:
        diag: list[int, int] = [curr[0]-1, curr[1]+1] if left else [curr[0]+1, curr[1]+1]
        if self.underground[diag[1]][diag[0]] == '.':
            return diag, True
        return curr, False
    
    def sand(self) -> bool:
        pos: list[int, int] = [self.start[0]-self.x_min, self.start[1]-self.y_min]
        try:
            while True:
                if self.underground[pos[1]][pos[0]] == 'O':
                    return True
                pos, down = self.goDown(pos)
                if down: continue
                pos, diag = self.checkDiagonal(pos, left=True)
                if diag: continue
                pos, diag = self.checkDiagonal(pos, left=False)
                if diag: continue
                self.underground[pos[1]][pos[0]] = 'O'
                self.sandCounter += 1
                break
        except:
            return True

def partOne() -> int:
    _map: Map = Map(coords=getData(DATA), start=[500, 0])
    _map.generate()
    while not _map.sand(): pass
    return _map.sandCounter

def partTwo() -> int:
    _map: Map = Map(coords=getData(DATA), start=[500, 0], wideMap=True)
    _map.generate()
    while not _map.sand(): pass
    return _map.sandCounter

def main() -> None:
    print(f'ANSWER PART ONE: {partOne()}')
    print(f'ANSWER PART TWO: {partTwo()}')

if __name__ == "__main__":
    main()
