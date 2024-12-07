import re
from itertools import product

TEST: str = open("test.txt")
DATA: str = open("input.txt")

def fetchData(data: str) -> list[list[str | int]]:
    return [[col if not col.isnumeric() else int(col) for col in row] for row in data.splitlines()]

class GearRatios:
    def __init__(self, data: list[list[str | int]], filter: list=['%', '&', '#', '@', '-', '+', '$', '=', '/', '*']) -> None:
        self.data: list[list[str | int]] = data
        self.filter: list = filter
        self._map: list[list[str | bool]] = [[col if col in self.filter else False for col in row] for row in self.data]
    
    def markCells(self) -> None:
        for rn, cn in product(range(len(self._map)), range(len(self._map[0]))):
            if isinstance(self._map[rn][cn], bool): continue
            for r, c in product([-1, 0, 1], repeat=2):
                self._map[rn-r][cn-c] = True if isinstance(self._map[rn-r][cn-c], bool) else self._map[rn-r][cn-c]
    
    def checkNeighbor(self, location: list, direction: bool = False) -> list[list[str | bool]] | None:
        """Mark neigbours of the Trues as True if it is an integer"""
        checkDirection: function = lambda r, p, d=direction: (bool(r+p >= 0) if d else bool(r+p < len(self._map[0])))
        pos: int = 0
        while checkDirection(location[1], pos):
            if self.data[location[0]][location[1] + pos] in self.filter: pass
            elif not isinstance(self.data[location[0]][location[1] + pos], int):
                self._map[location[0]][location[1] + pos] = False
                break
            self._map[location[0]][location[1] + pos] = True
            pos += -1 if direction else 1
        # Check other direction if not done already
        if not direction:
            self.checkNeighbor(location, direction=True)
    
    def getRatios(self, partOne: bool=True) -> list[list[int | str]]:
        self.markCells()
        for row, col in product(range(len(self._map)), range(len(self._map[0]))):
            if self._map[row][col] is True:
                self.checkNeighbor(location=[row, col])
        if partOne:
            return [''.join(str(self.data[r][c]) if self._map[r][c] and isinstance(self.data[r][c], int) else '.' for c in range(len(self._map[0]))) for r in range(len(self._map))]
        return [''.join(str(self.data[r][c]) if self._map[r][c] and (isinstance(self.data[r][c], int) or self.data[r][c] in self.filter) else '.' for c in range(len(self._map[0]))) for r in range(len(self._map[0]))]
    
def partOne(data: list[list[str | int]]) -> int:
    gearRatios: GearRatios = GearRatios(data)
    data = gearRatios.getRatios(partOne=True)
    return sum([sum(list(map(lambda x: int(x) if len(x) > 0 else 0, row.split('.')))) for row in data])

def partTwo(data: list[list[str | int]]) -> int:
    gearRatios: GearRatios = GearRatios(data, filter=['*'])
    data: list[list[int | str]] = gearRatios.getRatios(partOne=False)
    pattern: re.compile = re.compile(r'(\d+|\.|\*)')
    data = [re.findall(pattern, row) for row in data]
    for row in range(len(data)):
        pos: int = 0
        while pos < len(gearRatios._map[0]):
            if data[row][pos].isnumeric():
                length: int = len(data[row][pos])
                data[row] = data[row][:pos] + [int(data[row][pos])]*length + data[row][pos+1:]
                pos += length
                continue
            pos += 1
    ratio: list = []
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] in gearRatios.filter:
                _set: list = list(set(data[row+r][col+c] for r, c in product([-1, 0, 1], repeat=2) if isinstance(data[row+r][col+c], int)))
                if len(_set) == 1:
                    check: list = [data[row+r][col+c] for r, c in product([-1, 0, 1], repeat=2) if isinstance(data[row+r][col+c], int) and (isinstance(data[row-1][col], str) and isinstance(data[row+1][col], str))]
                    if len(check) == 2:
                        _set = check
                if len(_set) == 2: ratio.append(_set[0]*_set[1])
    return sum(ratio)
    
    
    
if __name__ == "__main__":
    data: list[list[str | int]] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
