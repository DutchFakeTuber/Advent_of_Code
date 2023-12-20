from Pulse_Propagation import TEST, DATA
from dataclasses import dataclass, field
from time import perf_counter_ns

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
            print(self.state, pulse)
            return self.state
        return None

@dataclass(kw_only=True)
class Conjunction:
    name: str = field(init=True, default_factory=str)
    remember: dict = field(init=False, default_factory=dict)
    type: str = field(init=False, default='Conjunction')

    def addMember(self, module) -> None:
        print(module, self.name)
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

def partOne(modules: dict) -> int:
    dcModules: dict[str, Conjunction | FlipFlop | Untyped] = build(modules)
    bools: dict[bool, int] = {True: 0, False: 0}
    # print(*modules.items(), sep='\n')
    for _ in range(2):
        print(dcModules)
        current: list[list[str, bool]] = [['broadcaster', False]]
        # bools[False] += 1
        wait: list[list[str, bool]] = []
        while len(current) or len(wait):
            if not len(current):
                current = wait
                wait = []
            print(f"{current=}, {wait=}")
            c, b = current.pop(0)
            result: bool = dcModules[c].process(b, c)
            if result == None:
                continue
            # print(c, b)
            bools[result] += 1
            for point in modules[c]['pointer']:
                wait.append([point, result])
    return bools

def partTwo(modules: dict) -> int:
    # modules: dict = build(modules)
    ...

if __name__ == "__main__":
    start = perf_counter_ns()
    data: dict = fetchData(TEST)
    print(partOne(data))
    print(partTwo(data))
    print(f"{(perf_counter_ns()-start)/1e9}")
