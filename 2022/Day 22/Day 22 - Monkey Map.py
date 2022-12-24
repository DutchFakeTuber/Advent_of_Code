import re
from Monkey_Map import INPUT

def getData() -> list[list[str], list[str]]:
    monkeyMap: list[str] = [line for line in INPUT.splitlines() if len(line) != 0]
    _map: list[list[int|str]] = [[l for l in line] for line in monkeyMap[:-1]]
    for m in range(len(_map)):
        while len(_map[m]) != len(_map[0]):
            _map[m].append(' ')
    return _map, re.findall(r"([0-9]+|[a-zA-Z]+)", monkeyMap[-1])

class Path:
    # See ./cube.jpg for more info
    A: dict = {f"[[{n}, 49], '>']": [[149-n, -1], '>'] for n in range(50)}
    B: dict = {f"[[-1, {50+n}], 'v']": [[150+n, -1], '>'] for n in range(50)}
    E: dict = {f"[[-1, {100+n}], 'v']": [[200, n], '^'] for n in range(50)}
    F: dict = {f"[[{n}, 150], '<']": [[149-n, 100], '<'] for n in range(50)}
    G: dict = {f"[[50, {100+n}], '^']": [[50+n, 100], '<'] for n in range(50)}
    I: dict = {f"[[{50+n}, 49], '>']": [[99, n], 'v'] for n in range(50)}
    K: dict = {f"[[150, {50+n}], '^']": [[150+n, 50], '<'] for n in range(50)}
    def __init__(self, monkeyMap: list[str], instructions: list[str]):
        self._map: list[str] = monkeyMap
        self.instr: list[str | int] = [int(i) if i.isnumeric() else i for i in instructions]
        self.rot: list = [[0, '>'], [1, 'v'], [2, '<'], [3, '^']]
        self.pos: dict = {'r': 0, 'c': monkeyMap[0].index('.'), 'a': self.rot[0]}
        self.num: dict = {'r': len(self._map)-1, 'c': len(self._map[0])-1}
        
    def arrow(self) -> None:
        self._map[self.pos['r']] = [*self._map[self.pos['r']][:self.pos['c']], self.pos['a'][1], *self._map[self.pos['r']][self.pos['c']+1:]]
    
    def turn(self, instruction: str) -> None:
        rotate: int = 1 if instruction == 'R' else -1
        rot: dict = {k: v for k, v in enumerate([self.rot[-1], *self.rot, self.rot[0]], start=-1)}
        self.pos['a'] = rot[self.pos['a'][0] + rotate]
        self.arrow()
    
    def area(self, row: int, col: int) -> tuple[int]:
        if row == -1 or row == self.num['r'] + 1: row = 0 if row == self.num['r'] + 1 else self.num['r']
        if col == -1 or col == self.num['c'] + 1: col = 0 if col == self.num['c'] + 1 else self.num['c']
        check: function = lambda rc: [[num for num, i in enumerate(rc) if i not in [' ', '#']][0], rc.index('#') if '#' in rc else None]
        _r, _c = self._map[row], list(zip(*self._map))[::-1][self.num['c'] - col]
        wrap: dict = {'>': check(_r), 'v': check(_c), '<': [self.num['c'] - c for c in check(_r[::-1])], '^': [self.num['r'] - c for c in check(_c[::-1])]}
        if self.pos['a'][1] in ['<', '>']:
            if min(wrap['>']) <= col <= max(wrap['<']): col = col if self._map[row][col] != '#' else self.pos['c']
            elif self.pos['a'][1] == '>': col = wrap['>'][0] if wrap['>'][0] < wrap['>'][1] else self.pos['c']
            else: col = wrap['<'][0] if wrap['<'][0] > wrap['<'][1] else self.pos['c']
        else:
            if min(wrap['v']) <= row <= max(wrap['^']): row = row if self._map[row][col] != '#' else self.pos['r']
            elif self.pos['a'][1] == 'v': row = wrap['v'][0] if wrap['v'][0] < wrap['v'][1] else self.pos['r']
            else: row = wrap['^'][0] if wrap['^'][0] > wrap['^'][1] else self.pos['r']
        return row, col

    def border(self, row: int, col: int) -> tuple:
        rot: list = []
        for side in [self.A, self.B, self.E, self.F, self.G, self.I, self.K]:
            for key, val in side.items():
                key = eval(key)
                if [row, col] == key[0]:
                    row, col, rot = val[0][0], val[0][1], [_rot for _rot in self.rot if _rot[1] == val[1]][0]
                    return row, col, rot
                elif [row, col] == val[0]:
                    row, col, rot = key[0][0], key[0][1], [_rot for _rot in self.rot if _rot[1] == key[1]][0]
                    return row, col, rot
                else: pass
        return row, col, rot

    def cube(self, row: int, col: int) -> None:
        row, col, rot = self.border(row, col)
        if len(rot):
            row += self.change[rot[0]][0]
            col += self.change[rot[0]][1]
        rot = rot if len(rot) else self.pos['a']
        if rot[1] in ['<', '>']:
            if self._map[row][col] == '#': return self.pos['r'], self.pos['c']
            self.pos['a'] = rot if col != self.pos['c'] else self.pos['a']
        else:
            if self._map[row][col] == '#': return self.pos['r'], self.pos['c']
            self.pos['a'] = rot if col != self.pos['r'] else self.pos['a']
        return row, col

    def move(self, instruction: int, cube=False) -> None:
        self.change: list[list[int, int]] = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(instruction, 0, -1):
            if not cube:
                row, col = self.area(self.pos['r'] + self.change[self.pos['a'][0]][0],
                                     self.pos['c'] + self.change[self.pos['a'][0]][1])
            else:
                row, col = self.cube(self.pos['r'] + self.change[self.pos['a'][0]][0],
                                     self.pos['c'] + self.change[self.pos['a'][0]][1])
            if [row, col] == [self.pos['r'], self.pos['c']]: break
            self.pos['r'], self.pos['c'] = row, col
            self.arrow()

def partOne() -> int:
    _map, instructions = getData()
    path: Path = Path(_map, instructions)
    while len(path.instr):
        instr = path.instr.pop(0)
        path.move(instr, cube=False) if isinstance(instr, int) else path.turn(instr)
    return (path.pos['r'] + 1) * 1_000 + (path.pos['c'] + 1) * 4 + path.pos['a'][0]

def partTwo() -> int:
    _map, instructions = getData()
    path: Path = Path(_map, instructions)
    while len(path.instr):
        instr = path.instr.pop(0)
        path.move(instr, cube=True) if isinstance(instr, int) else path.turn(instr)
    return (path.pos['r'] + 1) * 1_000 + (path.pos['c'] + 1) * 4 + path.pos['a'][0]

def main() -> None:
    print(f'ANSWER PART ONE: {partOne()}')
    print(f'ANSWER PART TWO: {partTwo()}')

if __name__ == "__main__":
    main()
