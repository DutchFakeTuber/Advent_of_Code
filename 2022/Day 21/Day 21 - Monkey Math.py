from dataclasses import dataclass, field
from Monkey_Math import INPUT

def getData() -> list[list[str, str]]:
    return [line.split(': ') for line in INPUT.splitlines() if len(line) != 0]

@dataclass(kw_only=True)
class Monkey:
    name: str = field(init=True, default_factory=str)
    number: int = field(init=False, default_factory=str)
    dependent: list[str] = field(init=True, default_factory=list[str])
    operation: str = field(init=False, default_factory=str)
    
    def __post_init__(self) -> None:
        d: list[str] = self.dependent.split(' ')
        if len(d) == 1:
            self.dependent, self.operation, self.number = None, None, int(*d)
        else:
            self.dependent = [d[0], d[2]]
            self.operation = d[1]
    
    def __eq__(self, other) -> bool:
        if other.dependent and self.name in other.dependent:
            other.dependent[other.dependent.index(self.name)] = self.number
            return True
        return False
    
    def canCalculate(self) -> bool:
        return True if isinstance(self.dependent[0], int) and isinstance(self.dependent[1], int) else False
    
    def calculate(self) -> int:
        match self.operation:
            case '*': self.number = self.dependent[0] * self.dependent[1]
            case '/': self.number = self.dependent[0] // self.dependent[1]
            case '+': self.number = self.dependent[0] + self.dependent[1]
            case '-': self.number = self.dependent[0] - self.dependent[1]
        self.dependent, self.operation = None, None
        return self.number

def process(monkeys: list[Monkey], root: bool = True) -> list[Monkey]:
    cleared: list = []
    counter: int = 0
    while True:
        for monkey in monkeys:
            if monkey.name == 'root' and isinstance(monkey.number, int) and root:
                return monkey.number
            if isinstance(monkey.number, int) and monkey.name not in cleared:
                [m for m in monkeys if m.dependent and monkey == m]
                cleared.append(monkey.name)
                counter: int = 0
            if monkey.dependent and monkey.canCalculate():
                monkey.calculate()
                counter: int = 0
        counter += 1
        if not root and counter > 10:
            return monkeys

def partOne() -> int:
    data: list[list[str, str]] = getData()
    monkeys: list[Monkey] = [Monkey(name=d[0], dependent=d[1]) for d in data]
    return process(monkeys, root=True)

def partTwo() -> int:
    data: list[list[str, str]] = getData()
    monkeys: list[Monkey] = [Monkey(name=d[0], dependent=d[1]) for d in data]
    human: Monkey = [[num, m] for num, m in enumerate(monkeys) if m.name == 'humn'][0]
    monkeys.pop(human[0])
    monkeys: list[Monkey] = process(monkeys, root=False)
    monkeys: list[Monkey] = [m for m in monkeys if m.dependent]
    ordered: list[Monkey] = [m for m in monkeys if m.name == 'root']
    start: str = [o for o in ordered[0].dependent if isinstance(o, str)][0]
    while True:
        for m in monkeys:
            if start == m.name:
                ordered.append(m)
                start = [_m for _m in m.dependent if isinstance(_m, str)][0]
        if len(ordered) == len(monkeys): break
    [print(o) for o in ordered]
    value: int = [val for val in ordered[0].dependent if isinstance(val, int)][0]
    for o in ordered[1:]:
        nextVal: int = [[num, val] for num, val in enumerate(o.dependent) if isinstance(val, int)][0]
        match o.operation:
            case '*': value = value // nextVal[1] if nextVal[0] == 1 else value // nextVal[1]
            case '/': value = value * nextVal[1] if nextVal[0] == 1 else nextVal[1] // value
            case '+': value -= nextVal[1]
            case '-': value = value + nextVal[1] if nextVal[0] == 1 else nextVal[1] - value
    return value

def main() -> None:
    print(f'ANSWER PART ONE: {partOne()}')
    print(f'ANSWER PART TWO: {partTwo()}')

if __name__ == "__main__":
    main()
