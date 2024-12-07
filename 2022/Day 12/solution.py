from collections import deque

TEST: str = open("test.txt")
DATA: str = open("input.txt")

def getData() -> list:
    return [line for line in DATA.splitlines() if len(line) != 0]

class BreadthFirstSearch:
    """ INSPIRED BY: https://github.com/juanplopes/advent-of-code-2022/blob/main/day12.py"""
    def __init__(self, input: list, *start: tuple[str]) -> None:
        self.input: list = input
        self.queue: deque = deque(
            (row, col, 0, 'a') for row in range(len(input))
            for col in range(len(input[row]))
            if input[row][col] in start
        )
        self.visited: set = set(
            (row, col)
            for row, col, _, _ in self.queue
        )
    
    def run(self) -> int:
        while len(self.queue):
            row, col, steps, height = self.queue.popleft()
            if self.input[row][col] == 'E':
                return steps
            for _row, _col in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
                if not 0 <= _row < len(self.input):
                    continue
                elif not 0 <= _col < len(self.input[_row]):
                    continue
                if (_row, _col) in self.visited:
                    continue
                _height = self.input[_row][_col].replace('E', 'z')
                if ord(_height) > ord(height) + 1:
                    continue
                self.visited.add((_row, _col))
                self.queue.append((_row, _col, steps + 1, _height))

def partOne() -> int:
    maze: list = getData()
    bfs: BreadthFirstSearch = BreadthFirstSearch(maze, 'S')
    return bfs.run()

def partTwo() -> int:
    maze: list = getData()
    bfs: BreadthFirstSearch = BreadthFirstSearch(maze, 'S', 'a')
    return bfs.run()

def main() -> None:
    print(f'ANSWER PART ONE: {partOne()}')
    print(f'ANSWER PART TWO: {partTwo()}')

if __name__ == "__main__":
    main()
