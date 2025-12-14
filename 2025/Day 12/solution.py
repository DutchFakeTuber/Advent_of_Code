from os.path import dirname, realpath
from math import prod
import re

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> tuple[list, list]:
    figures: list = [tuple(b.splitlines()[1:]) for b in re.split(r'\n\s*\n', data)[:-1]]
    boards: list = [[list(map(int, line.split(': ')[0].split('x'))), list(map(int, line.split(': ')[1].split()))] for line in re.split(r'\n\s*\n', data)[-1].splitlines()]
    return figures, boards

def partOne(figures: list[list[str]], boards: list[list[list[int], list[int]]]) -> int:
    '''
    Apperently this one is less difficult than originally thought.
    Check if all figures can fit inside the board side-by-side.
    If not, check if all figures can fit by counting all occupying space and check if this is lower than the grid size.
    '''
    return sum([prod(grid) >= sum(pieces)*9 for grid, pieces in boards])

if __name__ == "__main__":
    figures, boards = fetchData(DATA)
    print(partOne(figures, boards))
