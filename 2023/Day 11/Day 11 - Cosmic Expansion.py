from Cosmic_Expansion import TEST, DATA

def fetchData(data: str) -> list[list[str]]:
    return [[col for col in line] for line in data.splitlines()]

class Space:
    def __init__(self, data: list[list[str]], rate: int=2) -> None:
        self.data: list[list[str]] = data
        self.rate: int = rate - 1
        self.coords: list[list[int]] = []
        self.ex: list[list[int]] = []
    
    def expand(self, row: bool=True) -> None:
        expansion: int = 0
        for rc in range(len(self.data) if row else len(self.data[0])):
            empty: bool = all([True if char == '.' else False for char in (self.data[rc] if row else [line[rc] for line in self.data])])
            expansion += 0 if not empty else self.rate
            if row:
                self.ex.append([rc+expansion])
            else:
                self.ex[rc].append(rc+expansion)
        if row:
            self.expand(row=False)

    def manhattanDistance(self) -> None:
        self.mandist: set = set()
        for num, c in enumerate(self.coords):
            for _num, _c in enumerate(self.coords):
                if num == _num: continue
                self.mandist.add(tuple([num if num < _num else _num, _num if num < _num else num, abs(c[0]-_c[0]) + abs(c[1]-_c[1])]))
        self.mandist: list = list(self.mandist)

    def coordinates(self) -> None:
        self.coords: list[list[int]] = [[row, col] for row in range(len(self.data)) for col, char in enumerate(self.data[row]) if char == '#']
        self.expand(row=True)
        self.coords: list[list[int]] = [[self.ex[row][0], col] for row, col in self.coords]
        self.coords: list[list[int]] = [[row, self.ex[col][1]] for row, col in self.coords]

def parts(data: list[list[str]], rate=2) -> int:
    space: Space = Space(data, rate=rate)
    space.coordinates()
    space.manhattanDistance()
    return sum(length[2] for length in space.mandist)

if __name__ == "__main__":
    data: list[list[str]] = fetchData(DATA)
    print(parts(data, rate=2))
    print(parts(data, rate=1_000_000))
