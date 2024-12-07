import pandas as pd
import numpy as np

TEST: str = open("test.txt")
DATA: str = open("input.txt")

class Grid:
    MULTI: tuple = (
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1), ( 0, 0), ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    )
    def __init__(self, data: str=TEST_DATA, algorithm: str=TEST_ALGORITHM) -> None:
        self.data = [[char for char in line] for line in data.split('\n') if len(line) != 0]
        self.algorithm = algorithm
        self.start_end_algo = (self.algorithm[0], self.algorithm[-1])
    
    def emptyGrid(self, padding: int, grid: pd.DataFrame|None=None) -> pd.DataFrame:
        """Create a pandas DataFrame with NaN as contents."""
        return pd.DataFrame(
            index=np.arange(len(self.data if grid is None else grid) + padding),
            columns=np.arange(len(self.data[0] if grid is None else grid[0]) + padding),
        )
    
    def fillGrid(self, grid: pd.DataFrame, start_pos: tuple) -> pd.DataFrame:
        """Fill grid with the puzzle data. This function is only used during initialization."""
        # Fill DataFrame with puzzle data
        _y, _x = start_pos
        for yDF, yData in zip(np.arange(_y, len(self.data) + _y), self.data):
            for xDF, xData in zip(np.arange(_x, len(self.data[0]) + _x), yData):
                grid.iat[yDF, xDF] = xData
        
        # Add padding around puzzle data
        grid.fillna('.', inplace=True)

        return grid
    
    def calcGrid(self, grid: pd.DataFrame, number: int) -> pd.DataFrame:
        """Calculating contents and change values accordingly."""
        _grid = self.emptyGrid(2, grid) # This can be changed to 2 if needed.
        if self.start_end_algo == ('#', '.'):
            _grid.fillna('#' if number%2 == 0 else '.', inplace=True)
        else: _grid.fillna('.', inplace=True)

        for y in np.arange(1, len(grid) - 1):
            for x in np.arange(1, len(grid[y]) - 1):
                # Convert characters to an integer
                value = int(''.join('1' if char == '#' else '0' for char in [grid.iat[y+_y, x+_x] for _y, _x in self.MULTI]), 2)
                _grid.iat[y+1, x+1] = self.algorithm[value]
        
        return _grid

def partOne(padding: int=2) -> int:
    if padding%2 != 0: padding += 1
    padding *= 2 # Create padding for both sides of the DataFrame

    G = Grid(data=DATA, algorithm=ALGORITHM)
    grid = G.fillGrid(G.emptyGrid(padding), (padding//2, padding//2))
    
    for number in range(0, 2):
        _grid = G.calcGrid(grid, number)
        grid = _grid

    return sum([sum([1 if grid.iat[row, col] == '#' else 0 for col in range(0, len(grid[row]))]) for row in range(0, len(grid))])

def partTwo(padding: int=2) -> int:
    if padding%2 != 0: padding += 1
    padding *= 2

    G = Grid(data=DATA, algorithm=ALGORITHM)
    grid = G.fillGrid(G.emptyGrid(padding), (padding//2, padding//2))

    for number in range(0, 50):
        _grid = G.calcGrid(grid, number)
        grid = _grid

    return sum([sum([1 if grid.iat[row, col] == '#' else 0 for col in range(0, len(grid[row]))]) for row in range(0, len(grid))])

def main() -> None:
    print(partOne())
    print(partTwo())

if __name__ == "__main__":
    main()