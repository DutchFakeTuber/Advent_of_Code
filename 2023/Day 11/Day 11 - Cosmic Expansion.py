from Cosmic_Expansion import TEST, DATA

def fetchData(data: str) -> list[list[str]]:
    return [[col for col in line] for line in data.splitlines()]

class Space:
    def __init__(self, data: list[list[str]]) -> None:
        self.data: list[list[str]] = data
        self.coords: list[list[int]] = []

    def expand(self, row: bool=True) -> None:
        # For part two: expand coordinates instead of the whole map.
        counter: int = 0
        while counter < (len(self.data) if row else len(self.data[0])):
            empty: bool = all([True if char == '.' else False for char in (self.data[counter] if row else [line[counter] for line in self.data])])
            if empty:
                if row:
                    self.data = self.data[:counter+1] + self.data[counter:]
                else:
                    for r in range(len(self.data)):
                        self.data[r] = self.data[r][:counter+1] + self.data[r][counter:]
            counter += 1 if not empty else 2
        if row:
            self.expand(row=False)
        self.space: list[list[str]] = self.data

    def _manhattanDistance(self) -> None:
        self.mandist: set = set()
        for num, c in enumerate(self.coords):
            for _num, _c in enumerate(self.coords):
                if num == _num: continue
                self.mandist.add(tuple([c if num < _num else _c, _c if num < _num else c, abs(c[0]-_c[0]) + abs(c[1]-_c[1])]))
        self.mandist = list(self.mandist)

    def coordinates(self) -> None:
        self.coords: list[list[int]] = [tuple([row, col]) for row in range(len(self.space)) for col, char in enumerate(self.space[row]) if char == '#']
        self._manhattanDistance()

def partOne(data: list[list[str]]) -> int:
    space: Space = Space(data)
    space.expand()
    space.coordinates()
    return sum(length[2] for length in space.mandist)

def partTwo(data: list[list[str]]) -> int: ...

if __name__ == "__main__":
    data: list[list[str]] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
