from Step_Counter import TEST, DATA

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
    
    def walk(self, show: bool=False, duplicate: int=0) -> None:
        counter: int = 0
        while counter != self.steps:
            if show:
                row: list = [i[0] for i in self.current]
                col: list = [i[1] for i in self.current]
                if (max(row)-min(row)) % (len(self.plots)//duplicate) == 0:
                    print(f"{counter=} - {len(self.current)} - {max(row)-max(row)}")
                # print(f"{counter=} - Row: {min(row)}, {max(row)}; Col: {min(col)}, {max(col)}; Dist: {max(row)-min(row)}, {max(col)-min(col)}")
                # print(counter, len(self.current))
            self.pending: set = set()
            for coordinate in self.current:
                self.boulder(coordinate)
            self.current: set = self.pending
            counter += 1
        return len(self.current)

def partOne(plots: list[str], steps=64) -> int:
    coordinate: tuple[int] = [(r, c) for r, row in enumerate(plots) for c, col in enumerate(row) if col == 'S'][0]
    garden: GardenPlots = GardenPlots(plots, coordinate, steps=steps)
    return garden.walk()

def partTwo(plots: list[str], steps: int=1000) -> int:
    coordinate: tuple[int] = [(r, c) for r, row in enumerate(plots) for c, col in enumerate(row) if col == 'S'][0]
    garden: GardenPlots = GardenPlots(plots, coordinate, steps=steps)
    return garden.walk(True, duplicate=5)

if __name__ == "__main__":
    plots: list[str] = fetchData(DATA)
    print(partOne(plots, steps=64))
    plots: list[str] = fetchData(DATA, 5)
    print(partTwo(plots, steps=300))
