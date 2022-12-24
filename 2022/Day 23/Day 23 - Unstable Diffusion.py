from Unstable_Diffusion import INPUT

def getData() -> list[list[str]]:
    return set((col, row) for row, r in enumerate(l for l in INPUT.splitlines() if len(l) != 0) for col, c in enumerate(r) if c == '#')

class Grove:
    M: dict = {'N': [[-1, -1], [0, -1], [1, -1]],
               'S': [[-1, 1], [0, 1], [1, 1]],
               'W': [[-1, 1], [-1, 0], [-1, -1]],
               'E': [[1, 1], [1, 0], [1, -1]]}

    def __init__(self, elves: list[list[str]]) -> None:
        self.elf: list[list[str]] = elves
        self.proposed: dict = {}  # key=new coord, val=[current coord(s)]
        self.n: function = lambda r, c: {(r+n[0], c+n[1]) for n in self.M['N']}
        self.s: function = lambda r, c: {(r+n[0], c+n[1]) for n in self.M['S']}
        self.w: function = lambda r, c: {(r+n[0], c+n[1]) for n in self.M['W']}
        self.e: function = lambda r, c: {(r+n[0], c+n[1]) for n in self.M['E']}
        self.nswe: list[function] = [[self.n, *self.M['N'][1]], [self.s, *self.M['S'][1]], [self.w, *self.M['W'][1]], [self.e, *self.M['E'][1]]]
        self.all: function = lambda r, c: {*self.n(r, c), *self.s(r, c), *self.w(r, c), *self.e(r, c)}

    def rotate(self) -> None:
        self.nswe = [*self.nswe[1:], self.nswe[0]]

    def propose(self) -> None:
        self.proposed: dict = {}
        for row, col in list(self.elf):
            _row, _col = row, col
            if len(self.all(row, col).difference(self.elf)) < 8:
                for x in range(len(self.nswe)):
                    if len(self.nswe[x][0](row, col).difference(self.elf)) == 3:
                        _row, _col = row+self.nswe[x][1], col+self.nswe[x][2]
                        break
            self.proposed.setdefault(f'[{_row}, {_col}]', []).append([row, col])
    
    def move(self) -> None:
        empty = set()
        for key, val in self.proposed.items():
            if len(val) == 1:
                empty.add((eval(key)[0], eval(key)[1]))
            else:
                for v in val:
                    empty.add((v[0], v[1]))
        self.elf = empty

def partOne() -> int:
    grove: Grove = Grove(getData())
    for _ in range(0, 10, 1):
        grove.propose()
        grove.move()
        grove.rotate()
    field: list[list[str]] = [
        ['.' for _ in range(max(n[1] for n in grove.elf) - min(n[1] for n in grove.elf) + 1)]
        for _ in range(max(n[0] for n in grove.elf) - min(n[0] for n in grove.elf) + 1)
    ]
    for row, col in grove.elf:
        field[col][row] = '#'
    [print(''.join(f)) for f in field]
    return sum(1 for r in range(len(field)) for c in field[r] if c == '.')
    
def partTwo() -> int:
    grove: Grove = Grove(getData())
    counter: int = 0
    while True:
        previous = grove.elf
        grove.propose()
        grove.move()
        grove.rotate()
        counter += 1
        if grove.elf == previous:
            break
    return counter

def main() -> None:
    print(f"ANSWER PART ONE: {partOne()}")
    print(f"ANSWER PART TWO: {partTwo()}")
    
if __name__ == "__main__":
    main()
