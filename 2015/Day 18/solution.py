import os
from itertools import product

TEST: str = open(f"{os.path.dirname(os.path.realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{os.path.dirname(os.path.realpath(__file__))}\\input.txt").read()


# Conways' Game of Life
class CGoL:
    def __init__(self, data: str, stuck: bool = False) -> None:
        self.field: list[list[str]] = [[char for char in line] for line in data.splitlines() if len(line)]
        self.rc: list[list[int]] = [[0, len(self.field)], [0, len(self.field[0])]]
        self.coords: list[list[int]] = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        self.flipCoords: list[list[int]] = []
        self.stuck: bool = stuck
        if self.stuck:
            self.flip()
    
    def flip(self) -> None:
        while self.flipCoords:
            row, col = self.flipCoords.pop()
            self.field[row][col] = '.' if self.field[row][col] == '#' else '#'
        if self.stuck:
            self.field[0][0] = '#'
            self.field[0][-1] = '#'
            self.field[-1][0] = '#'
            self.field[-1][-1] = '#'
    
    def check(self) -> None:
        for row, col in product(range(self.rc[0][1]), range(self.rc[1][1])):
            counter: int = 0
            char: str = self.field[row][col]
            for coord in self.coords:
                _row, _col = row + coord[0], col + coord[1]
                if self.rc[0][0] <= _row < self.rc[0][1] and self.rc[1][0] <= _col < self.rc[1][1]:
                    counter += self.field[_row][_col] == '#'
            if char == '.' and counter == 3:
                self.flipCoords.append([row, col])
            elif char == '#' and counter not in [2, 3]:
                self.flipCoords.append([row, col])
        self.flip()

def parts(data: str, stuck: bool=False) -> int:
    cgol: CGoL = CGoL(data, stuck=stuck)
    for _ in range(100):
        cgol.check()
    return sum([sum([1 for char in line if char == '#']) for line in cgol.field])

if __name__ == "__main__":
    print(parts(DATA, False))
    print(parts(DATA, True))
