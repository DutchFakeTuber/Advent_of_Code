from Cosmic_Expansion import TEST, DATA

def fetchData(data: str) -> list[list[str]]:
    return [[col for col in line] for line in data.splitlines()]

class Space:
    def __init__(self, data: list[list[str]]) -> None:
        self.data: list[list[str]] = data
        self.coords: list[list[int]] = []
        
    def expand(self, row: bool=True) -> None:
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
    
    def coordinates(self) -> None:
        self.coords: list[list[int]] = [[row, col] for row in range(len(self.space)) for col, char in enumerate(self.space[row]) if char == '#']

def partOne(data: list[list[str]]) -> int:
    space: Space = Space(data)
    space.expand()
    space.coordinates()
    print(space.coords)
    print(len(space.space), len(space.space[0]))

def partTwo(data: list[list[str]]) -> int: ...

if __name__ == "__main__":
    data: list[list[str]] = fetchData(TEST)
    print(partOne(data))
    print(partTwo(data))
