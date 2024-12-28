from os.path import dirname, realpath
from collections import deque
from dataclasses import dataclass, field

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[str]:
    return [line for line in data.splitlines() if len(line)]

@dataclass(kw_only=True)
class Keypad:
    numeric: bool = field(init=True, default_factory=bool)
    layer: int = field(init=True, default_factory=int)
    buttons: dict[str, tuple[int]] = field(init=False, default_factory=dict)
    prune: dict[str, dict[str, list[str]]] = field(init=False, default_factory=dict)
    cache: dict[tuple[str, int], int] = field(init=False, default_factory=dict)
    
    def __post_init__(self) -> None:
        if self.numeric:
            self.buttons: dict[str, tuple[int]] = {'7':(0,0),'8':(0,1),'9':(0,2),'4':(1,0),'5':(1,1),'6':(1,2),'1':(2,0),'2':(2,1),'3':(2,2),'0':(3,1),'A':(3,2)}
        else:
            self.buttons: dict[str, tuple[int]] = {'^': (0, 1), 'A': (0, 2), '<': (1, 0), 'v': (1, 1), '>': (1, 2)}
        self._pruneButtons()
        self.cache = dict()
        self.test: list = []
    
    def _pruneButtons(self) -> None:
        zigzag: list = ['^>^', '>^>', '>v>', 'v>v', 'v<v', '<v<', '<^<', '^<^']
        self.prune: dict[str, dict[str, str]] = dict()
        for key, val in self.buttons.items():
            self.prune.setdefault(key, dict())
            for k, v in self.buttons.items():
                manhattan: int = abs(val[0]-v[0])+abs(val[1]-v[1])
                todo: deque = deque([(0, val, list())])
                while todo:
                    steps, (row, col), path = todo.popleft()
                    if steps > manhattan: continue
                    if (row, col) == v:
                        strPath = ''.join(path)
                        zigzagPresent: bool = any(zz in strPath for zz in zigzag)
                        if zigzagPresent: continue
                        self.prune[key].setdefault(k, []).append(strPath)
                    moves: dict[str, list[int]] = {(row-1, col): '^', (row+1, col): 'v', (row, col-1): '<', (row, col+1): '>'}
                    for r, c, d in [[r, c, moves[(r, c)]] for r, c in self.buttons.values() if (r, c) in moves.keys()]:
                        todo.append((steps + 1, (r, c), path + [d]))

    def move(self, combinations: str, position: int, previous: str, current: str, result: list) -> list[str]:
        if position == len(combinations):
            result.append(current)
            return
        for options in self.prune[previous][combinations[position]]:
            self.move(combinations, position=position+1, previous=combinations[position], current=current+options+'A', result=result)
        return result
    
    def splitter(self, sequence: str) -> object:
        current: str = ''
        for char in sequence:
            current += char
            if char == 'A':
                yield current
                current = ''
    
    def shortest(self, sequence: str, robot: int) -> int:
        if robot == 0:
            return len(sequence)
        if self.cache.get(sequence, None) is not None:
            if self.cache[sequence].get(robot, None) is not None:
                return self.cache[sequence][robot]
        total: int = 0
        for subSeq in self.splitter(sequence):
            moves: list = self.move(subSeq, 0, 'A', '', [])
            total += min(self.shortest(m, robot-1) for m in moves)
        self.cache.setdefault(sequence, dict()).setdefault(robot, total)
        return total

def pressCode(code: str, robots: int=2) -> int:
    numpad: Keypad = Keypad(numeric=True)
    robot: Keypad = Keypad(numeric=False)
    sequences: list = numpad.move(code, 0, 'A', '', [])
    return min(robot.shortest(sequence, robots) for sequence in sequences)

def parts(data: list[list[str]], robots: int=2) -> int:
    return sum([int(code[:-1]) * pressCode(code, robots) for code in data])

if __name__ == "__main__":
    data = fetchData(DATA)
    print(parts(data, robots=2))
    print(parts(data, robots=25))
