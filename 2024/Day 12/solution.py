from os.path import dirname, realpath
from collections import deque
from itertools import product

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[list[str]]:
    return [[char for char in line] for line in data.splitlines() if len(line)]

class Garden:
    def __init__(self, field: list[list[str]]) -> None:
        self.field: list[list[str]] = field[::]
        self.plot: set = set()
        self.found: str = "#"
        self.perimeter: list[int] = []
        self.borders: list[list[int]] = [[0, len(self.field)], [0, len(self.field[0])]] # [[ROW], [COL]]

    def _getFence(self, region: list[list[str]], edge: int=0, start: list=['>', 1, 0], flipped: bool=False) -> int:
        check: dict = {'^': [0, 1], '>': [1, 0], 'v': [0, -1], '<': [-1, 0]} if not flipped else {'^': [0, -1], '>': [-1, 0], 'v': [0, 1], '<': [1, 0]}
        move: dict = {'^': [-1, 0], '>': [0, 1], 'v': [1, 0], '<': [0, -1]} if not flipped else {'^': [1, 0], '>': [0, -1], 'v': [-1, 0], '<': [0, 1]}
        turn: dict = {'^': ['<', '>'], '>': ['^', 'v'], 'v': ['>', '<'], '<': ['v', '^']}
        look: function = lambda x, y: [x, y[1]+move[x][0], y[2]+move[x][1]]
        start: list[str | int] = start
        current: list[str | int] = []
        edge: int = edge
        visited: set = set()
        # Find the first block below while walking next to the fence
        while not current:
            if region[start[1]+check[start[0]][0]][start[2]+check[start[0]][1]] == '#':
                current = [start[0], start[1], start[2]]
                visited.add((current[1], current[2]))
                break
            start = [start[0], start[1]+move[start[0]][0], start[2]+move[start[0]][1]]
        # Start walking!
        while True:
            # [print(''.join(region[row][col] if (row, col) != (current[1], current[2]) else current[0] for col in range(len(region[row])))) for row in range(len(region))]
            previous, left, forward, right = current[0], look(turn[current[0]][0], current), look(current[0], current), look(turn[current[0]][1], current)
            if region[forward[1]][forward[2]] == '+':
                if region[right[1]][right[2]] == '#':
                    # Move forward, we are not at a corner
                    current = forward
                elif region[right[1]][right[2]] == '+' and right[0] != previous:
                    # Rotate to the right, we're at a corner!
                    current = right
                    edge += 1
                elif region[left[1]][left[2]] == '+' and left[0] != previous:
                    # Rotate to the left, we're at a corner!
                    current = left
                    edge += 1
                else:
                    current = forward
            else:
                if region[right[1]][right[2]] == '+' and right[0] != previous:
                    # Rotate to the right, we're at a corner!
                    current = [right[0], current[1], current[2]]
                    forward = look(current[0], current)
                    # Check if you can move forward
                    if region[forward[1]][forward[2]] == '+':
                        current = forward
                else:
                    # Rotate to the left, we're at a corner!
                    current = [left[0], current[1], current[2]]
                    forward = look(current[0], current)
                    # Check if you can move forward
                    if region[forward[1]][forward[2]] == '+':
                        current = forward
                edge += 1
            visited.add((current[1], current[2]))
            if current == start:
                break
        for r, c in visited:
            region[r][c] = self.found
        empty: list[list[int]] = [[r, c] for r, c in product(range(len(region)), range(len(region[0]))) if region[r][c] == '+']
        if len(empty) != 0:
            edge = max(self._getFence(region, edge=edge, start=['>', empty[0][0], empty[0][1]], flipped=True), edge)
        return edge

    def _getPerimeter(self, area: list[list[int]]) -> None:
        region: list[list[str]] = self._buildRegion(area, plotFence=False)
        seen: int = 0
        for r, c in product(range(1, len(region)-1), range(1, len(region[0])-1)):
            if region[r][c] == ' ':
                continue
            seen += sum(1 for _r, _c in [[r-1, c], [r, c-1], [r+1, c], [r, c+1]] if region[_r][_c] == ' ')
        return seen
    
    def _buildRegion(self, area: list[list[int]], plotFence: bool=False) -> list[list[str]]:
        region: list[list[str]] = [[self.found if (r, c) in self.plot else ' ' for c in range(area[1][0]-2, area[1][1]+3)] for r in range(area[0][0]-2, area[0][1]+3)]
        if not plotFence:
            return region
        for row, col in product(range(len(region)), range(len(region[0]))):
            if region[row][col] in [' ', '+']: continue
            for r, c in [[row-1, col-1], [row-1, col], [row-1, col+1], [row, col-1], [row, col+1], [row+1, col-1], [row+1, col], [row+1, col+1]]:
                if region[r][c] == ' ':
                    region[r][c] = '+'
        return region
    
    def getPlot(self, start: tuple[int, int], discount: bool=False) -> None:
        char: str = self.field[start[0]][start[1]]
        check: deque = deque([start])
        self.plot: set = set([start])
        while check:
            row, col = check.popleft()
            for r, c in [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]:
                if (r, c) in self.plot:
                    continue
                if self.borders[0][0] <= r < self.borders[0][1] and self.borders[1][0] <= c < self.borders[1][1]:
                    if self.field[r][c] == char:
                        self.plot.add((r, c))
                        check.append((r, c))
        rows, cols = zip(*self.plot)
        if not discount:
            fence: int = self._getPerimeter([[min(rows), max(rows)], [min(cols), max(cols)]])
        else:
            region: list[list[str]] = self._buildRegion([[min(rows), max(rows)], [min(cols), max(cols)]], plotFence=True)
            fence: int = self._getFence(region)
        self.perimeter.append(fence*len(self.plot))
        for row, col in self.plot:
            self.field[row][col] = self.found
    
    def findField(self) -> bool:
        for row, col in product(range(self.borders[0][1]), range(self.borders[1][1])):
            if self.field[row][col] != self.found:
                return True
        return False

def parts(data: list[list[str]], discount: bool=False) -> int:
    garden: Garden = Garden(field=data)
    while garden.findField():
        for row, col in product(range(garden.borders[0][1]), range(garden.borders[1][1])):
            if garden.field[row][col] != garden.found:
                garden.getPlot((row, col), discount=discount)
                break
    return sum(garden.perimeter)

if __name__ == "__main__":
    print(parts(fetchData(DATA), discount=False))
    print(parts(fetchData(DATA), discount=True))
