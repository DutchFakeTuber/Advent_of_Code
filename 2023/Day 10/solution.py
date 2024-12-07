TEST: str = open("test.txt")
DATA: str = open("input.txt")

def fetchData(data: str) -> list[list[list[str, None]]]:
    return [[[char, None] for char in line] for line in data.splitlines()]

class Maze:
    PATH: dict = {
        '|': [[-1, 0], [1, 0]],
        '-': [[0, -1], [0, 1]],
        'L': [[-1, 0], [0, 1]],
        'J': [[-1, 0], [0, -1]],
        '7': [[1, 0], [0, -1]],
        'F': [[1, 0], [0, 1]],
        'S': [[-1, 0], [1, 0], [0, -1], [0, 1]],
        '.': None
    }
    
    def __init__(self, data: list[list[list[str, None]]]) -> None:
        self.positions: list = [[row, col] for row in range(len(data)) for col in range(len(data[row])) if data[row][col][0] == 'S']
        self.counter: int = 0
        self.data = data
        self.size: list = [len(self.data), len(self.data[0])]
    
    def walk(self, row: int, col: int) -> None:
        for coords in self.PATH[self.data[row][col][0]]:
            _r, _c = row+coords[0], col+coords[1]
            # Continue because we've been here before
            if self.data[_r][_c][1] is not None:
                continue
            # Check if the _r and _c values are in bounds and the position is not equal to '.'
            if 0 <= _r < self.size[0] and 0 <= _c < self.size[1] and self.PATH[self.data[_r][_c][0]]:
                for pipe in self.PATH[self.data[_r][_c][0]]:
                    # Check if the coords of the selected pipe match with the current position
                    if _r+pipe[0] == row and _c+pipe[1] == col:
                        self.positions.append([_r, _c])
                        self.data[_r][_c][1] = self.counter

    def process(self) -> None:
        self.data[self.positions[0][0]][self.positions[0][1]][1] = self.counter
        self.counter += 1
        # It is better to walk one way instead of both.
        self.walk(*self.positions.pop(0))
        remove: list[int] = self.positions.pop(-1)
        self.data[remove[0]][remove[1]][1] = None
        self.counter += 1
        while len(self.positions):
            for _ in range(len(self.positions)):
                self.walk(*self.positions.pop(0))
            self.counter += 1

def partOne(data: list[list[list[str, None]]]) -> int:
    maze: Maze = Maze(data)
    maze.process()
    counter: float = max([max(map(lambda x: x[1] if x[1] else 0, line)) for line in maze.data]) / 2
    return int(counter) if counter == int(counter) else int(counter) + 1

def partTwo(data: list[list[list[str, None]]]) -> int:
    maze: Maze = Maze(data)
    maze.process()
    coords: list[list[int]] = [[row, col, maze.data[row][col][1]] for row in range(len(maze.data)) for col in range(len(maze.data[row])) if isinstance(maze.data[row][col][1], int)]
    coords.sort(key=lambda x: x[2])
    c: list[list[int]] = [*coords, coords[0]]
    # Calculate area with the Shoelace formula
    area: float = abs(sum([(c[n][0] * c[n+1][1]) - (c[n+1][0] * c[n][1]) for n in range(len(c)-1)])) / 2
    # Include Pick's theorem
    points: float = abs(area*-1 + (len(c)/2) - 1)
    return int(points) if int(points) == points else int(points) + 1

if __name__ == "__main__":
    print(partOne(fetchData(DATA)))
    print(partTwo(fetchData(DATA)))
