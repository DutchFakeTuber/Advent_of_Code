TEST: str = open("test.txt")
DATA: str = open("input.txt")

def fetchData(data: str, duplicate: int=0) -> list[str]:
    plots: list[str] = data.splitlines()
    if not duplicate:
        return plots
    extra: list[str] = [line.replace('S', '.') for line in plots]
    parts: int = duplicate // 2
    new: list[str] = []
    for number in range(duplicate):
        for p, e in zip(plots, extra):
            if number == parts:
                new.append((duplicate//2)*e+p+(duplicate//2)*e)
            else:
                new.append(duplicate*e)
    return new

class GardenPlots:
    def __init__(self, data: list[str], start: tuple[int, int], steps: int=64) -> None:
        self.plots: list[int] = data
        self.edge: list[list[int]] = [[-1, len(data)], [-1, len(data[0])]]
        self.steps: int = steps
        self.current: set = set([start])
    
    def boulder(self, coordinate: tuple[int]) -> bool:
        for row, col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if self.plots[coordinate[0]+row][coordinate[1]+col] != '#':
                if (coordinate[0]+row, coordinate[1]+col) not in self.current:
                    self.pending.add((coordinate[0]+row, coordinate[1]+col))
    
    def walk(self) -> None:
        counter: int = 0
        while counter != self.steps:
            if counter in [num*131+65 for num in range(3)]:
                print(f"{counter=} - {len(self.current)}")
            self.pending: set = set()
            for coordinate in self.current:
                self.boulder(coordinate)
            self.current: set = self.pending
            counter += 1
        return len(self.current)

def partOne(plots: list[str], steps: int) -> int:
    coordinate: tuple[int] = [(r, c) for r, row in enumerate(plots) for c, col in enumerate(row) if col == 'S'][0]
    garden: GardenPlots = GardenPlots(plots, coordinate, steps=steps)
    return garden.walk()

def partTwo(plots: list[str], steps: int) -> int:
    # coordinate: tuple[int] = [(r, c) for r, row in enumerate(plots) for c, col in enumerate(row) if col == 'S'][0]
    # garden: GardenPlots = GardenPlots(plots, coordinate, steps=steps)
    # return garden.walk()
    """
    Using the statements above, plots found at 65, 196, 327: 3832, 33967, 94056
    Length of the field is 131, total steps taken is: 26501365
    
    """
    one, two, three = 3832, 33967, 94056
    steps: int = 26501365
    fields: int = steps // 131
    return one + (two-one)*fields + (fields*(fields-1)//2)*((three-two)-(two-one))

if __name__ == "__main__":
    plots: list[str] = fetchData(DATA)
    print(partOne(plots, steps=64))
    plots: list[str] = fetchData(DATA, 7)
    print(partTwo(plots, steps=330))
