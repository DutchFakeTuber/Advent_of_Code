from Pulse_Propagation import TEST, DATA
from dataclasses import dataclass, field

def fetchData(data: str) -> dict:
    modules: dict = {}
    for line in data.splitlines():
        (module, pointers), operator = line.split(' -> '), None
        if module[0] in ['%', '&']:
            operator, module = module[0], module[1:]
        modules[module] = {'operator': operator, 'pointer': pointers.split(', ')}
    return modules

@dataclass(kw_only=True)
class FlipFlop:
    name: str = field(init=True, default_factory=str)
    state: bool = field(init=False, default=False)
    type: str = field(init=False, default='FlipFlop')

    def process(self, pulse: bool, module: str) -> bool | None:
        if pulse == False:
            self.state = not self.state
            return self.state
        return None

@dataclass(kw_only=True)
class Conjunction:
    name: str = field(init=True, default_factory=str)
    remember: dict = field(init=False, default_factory=dict)
    type: str = field(init=False, default='Conjunction')

    def addMember(self, module) -> None:
        if module != self.name:
            self.remember[module] = False

    def process(self, pulse: bool, module: str) -> bool:
        remember: bool | None = self.remember.get(module, None)
        if isinstance(remember, bool):
            self.remember[module] = pulse
            return not all(self.remember.values())

@dataclass(kw_only=True)
class Untyped:
    name: str = field(init=True, default_factory=str)
    type: str = field(init=False, default='Untyped')

    def process(self, pulse: bool, module: str) -> bool | None:
        return pulse if self.name == 'broadcaster' else None

def build(modules: dict) -> dict:
    dcModules: dict[str, Conjunction | FlipFlop | Untyped] = {}
    for name, inner in modules.items():
        match inner['operator']:
            case '&': module: Conjunction = Conjunction(name=name)
            case '%': module: FlipFlop = FlipFlop(name=name)
            case _: module: Untyped = Untyped(name=name)
        dcModules[module.name] = module
    for name, inner in modules.items():
        for point in inner['pointer']:
            if point not in dcModules.keys():
                untyped: Untyped = Untyped(name=point)
                dcModules[untyped.name] = untyped
            if dcModules[point].type == 'Conjunction':
                dcModules[point].addMember(name)
    return dcModules

def looper(current: list[list[str, bool, str]],
           modules: dict[str, list[str]],
           dcModules: dict[str, Conjunction | FlipFlop | Untyped],
           state: list[str]=[]) -> tuple[dict, dict]:
    bools: dict[bool, int] = {True: 0, False: 0}
    pending: list[list[str, bool, str]] = []
    checkState: bool = bool(len(state))
    found: list = []
    while len(current) or len(pending):
        if not len(current):
            current = pending
            pending = []
        module, true_false, previous = current.pop(0)
        result: bool = dcModules[module].process(true_false, previous)
        if result == None:
            continue
        if checkState:
            if dcModules[module].name in state and result:
                found.append(dcModules[module].name)
        for point in modules[module]['pointer']:
            bools[result] += 1
            pending.append([point, result, module])
    if checkState:
        return found, dcModules
    return bools, dcModules

def partOne(modules: dict) -> int:
    dcModules: dict[str, Conjunction | FlipFlop | Untyped] = build(modules)
    bools: dict[bool, int] = {True: 0, False: 0}
    for _ in range(1000):
        current: list[list[str, bool, str]] = [['broadcaster', False, '']]
        bools[False] += 1
        _bools, dcModules = looper(current, modules, dcModules)
        bools[True] += _bools[True]
        bools[False] += _bools[False]
    return bools[True] * bools[False]

def partTwo(modules: dict) -> int:
    """Strategy:
    
    Find the Conjunctions previous to `rx`.
    The layout for the input is as follows:
    [Conj., Conj., Conj., Conj.] -> Conj. -> `rx`
    
    `rx` should receive a low pulse `False`.
    This equates to: [`True`, `True`, `True`, `True`] -> `False` -> `rx`
    
    Returns:
        int: Conjunctions [Conj., Conj., Conj., Conj.] multiplied.
    """
    dcModules: dict[str, Conjunction | FlipFlop | Untyped] = build(modules)
    previous: str = [k for k, v in modules.items() if 'rx' in v['pointer'] and v['operator'] == '&'][0]
    previous: list[str] = [k for k, v in modules.items() if previous in v['pointer'] and v['operator'] == '&']
    counter: int = 0
    conjunctions: dict = {}
    while True:
        counter += 1
        found, dcModules = looper([['broadcaster', False, '']], modules, dcModules, previous)
        if len(found):
            for f in found:
                if not conjunctions.get(f, False):
                    conjunctions[f] = counter
        if len(conjunctions.keys()) == len(previous):
            result: int = 1
            for c in conjunctions.values():
                result *= c
            return result

if __name__ == "__main__":
    data: dict = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
