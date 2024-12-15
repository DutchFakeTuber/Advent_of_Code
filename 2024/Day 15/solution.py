import os
from collections import deque
import numpy as np

TEST: str = open(f"{os.path.dirname(os.path.realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{os.path.dirname(os.path.realpath(__file__))}\\input.txt").read()

class Warehouse:
    def __init__(self, field: list[list[str]], large: bool=False) -> None:
        self.field: np.array = np.array(field)
        self.robot: list[int] = [[r, c] for r in range(len(field)) for c in range(len(field[r])) if field[r][c] == '@'][0]
        self.move: dict[str, list[int]] = {'^': [-1, 0], '>': [0, 1], 'v': [1, 0], '<': [0, -1]}
        self.large: bool = large
        self.plotted: bool = False

    def __repr__(self) -> str:
        if not self.plotted:
            os.system("")
            self.plotted = True
            replace: dict = {'@': '\033[33m@\033[0m', '#': '\033[31m#\033[0m', 'O': '\033[32mO\033[0m', '.': '\033[30m.\033[0m', '[': '\033[32m[\033[0m', ']': '\033[32m]\033[0m'}
            for row in self.field:
                print(''.join(replace[col] for col in row))
            return '\r'
        return ''

    def goodsPositioningSystem(self) -> int:
        return sum(100*row+col for row in range(len(self.field)) for col in range(len(self.field[row])) if self.field[row][col] == ('[' if self.large else 'O'))
    
    def moveLargeBox(self, coords: list[int], direction: str) -> None:
        match direction:
            case '>':
                check: np.array = self.field[coords[0], coords[1]:]
                empty: int = np.where(check == '.')[0]
                if not len(empty) or empty[0] > np.where(check == '#')[0][0]:
                    return
                self.field[coords[0], coords[1]:coords[1]+empty[0]+1] = np.roll(self.field[coords[0], coords[1]:coords[1]+empty[0]+1], 1)
            case '<':
                check: np.array = self.field[coords[0], :coords[1]+1][::-1]
                empty: int = np.where(check == '.')[0]
                if not len(empty) or empty[0] > np.where(check == '#')[0][0]:
                    return
                self.field[coords[0], coords[1]-empty[0]:coords[1]+1] = np.roll(self.field[coords[0], coords[1]-empty[0]:coords[1]+1], -1)
            case '^' | 'v':
                offset: int = -1 if direction == '^' else 1
                # Get all boxes that are connected to the box that the robot wants to push
                visited: set = set()
                toCheck: deque = deque([(self.robot[0], self.robot[1])])
                while toCheck:
                    coords = toCheck.popleft()
                    visited.add(coords)
                    match self.field[coords[0]+offset][coords[1]]:
                        case '#':
                            return
                        case '.': pass
                        case '[': toCheck.extend([(coords[0]+offset, coords[1]), (coords[0]+offset, coords[1]+1)])
                        case ']': toCheck.extend([(coords[0]+offset, coords[1]-1), (coords[0]+offset, coords[1])])
                # Get current coords and future coords for replacement
                coords: dict[tuple[int], list[list[int], str]] = {v: [[v[0]+offset, v[1]], self.field[v[0], v[1]]] for v in visited}
                for r, c in coords.keys():
                    self.field[r, c] = '.'
                for (r, c), val in coords.values():
                    self.field[r, c] = val
        self.moveRobot(direction)
    
    def moveBox(self, coords: list[int], direction: str) -> None:
        check: dict[str, np.array] = {'^': self.field[:coords[0]+1, coords[1]][::-1], '>': self.field[coords[0], coords[1]:], 'v': self.field[coords[0]:, coords[1]], '<': self.field[coords[0], :coords[1]+1][::-1]}
        empty: int = np.where(check[direction] == '.')[0]
        if not len(empty) or empty[0] > np.where(check[direction] == '#')[0][0]:
            return
        match direction:
            case '^': self.field[coords[0]-empty[0]:coords[0]+1, coords[1]] = np.roll(self.field[coords[0]-empty[0]:coords[0]+1, coords[1]], -1)
            case '>': self.field[coords[0], coords[1]:coords[1]+empty[0]+1] = np.roll(self.field[coords[0], coords[1]:coords[1]+empty[0]+1], 1)
            case 'v': self.field[coords[0]:coords[0]+empty[0]+1, coords[1]] = np.roll(self.field[coords[0]:coords[0]+empty[0]+1, coords[1]], 1)
            case '<': self.field[coords[0], coords[1]-empty[0]:coords[1]+1] = np.roll(self.field[coords[0], coords[1]-empty[0]:coords[1]+1], -1)
        self.moveRobot(direction)

    def moveRobot(self, direction: str) -> None:
        self.robot = [self.robot[0] + self.move[direction][0], self.robot[1] + self.move[direction][1]]

    def sortWarehouse(self, direction: str) -> None:
        self.plotted = False
        nextSpot: str = self.field[self.robot[0] + self.move[direction][0]][self.robot[1] + self.move[direction][1]]
        if nextSpot == '#':
            return
        if nextSpot == '.':
            self.field[self.robot[0], self.robot[1]] = '.'
            self.moveRobot(direction)
            self.field[self.robot[0], self.robot[1]] = '@'
            return
        if self.large:
            self.moveLargeBox(self.robot, direction)
        else:
            self.moveBox(self.robot, direction)

def fetchData(data: str, large: bool=False) -> tuple[list[list[str]], str]:
    replace: dict[str] = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}
    return [list(map(str, ''.join([replace[char] for char in line]))) if large else [char for char in line] for line in data.split('\n\n')[0].splitlines() if len(line)], ''.join(data.split('\n\n')[1].splitlines())

def partOne(field: list[list[str]], steps: str) -> int:
    warehouse: Warehouse = Warehouse(field)
    for step in steps:
        warehouse.sortWarehouse(step)
    return warehouse.goodsPositioningSystem()

def partTwo(field: list[list[str]], steps: str) -> int:
    warehouse: Warehouse = Warehouse(field, large=True)
    # print(warehouse)
    for step in steps:
        warehouse.sortWarehouse(step)
    # print(warehouse)
    return warehouse.goodsPositioningSystem()

if __name__ == "__main__":
    print(partOne(*fetchData(DATA, large=False)))
    print(partTwo(*fetchData(DATA, large=True)))
