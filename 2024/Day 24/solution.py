from os.path import dirname, realpath
from dataclasses import dataclass, field
from graphviz import Digraph
from time import perf_counter_ns

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> tuple[dict[str, int], dict[str, list[str]]]:
    return (
        {line.split(': ')[0]: int(line.split(': ')[1]) for line in data.split('\n\n')[0].splitlines() if len(line)},
        {line.split(' ')[4]: line.split(' ')[:3] for line in data.split('\n\n')[1].splitlines() if len(line)}
    )

@dataclass(kw_only=True)
class Gates:
    current: str = field(init=True, default_factory=str)
    parent: object | None = field(init=False, default=None)
    left: object | int = field(init=False, default=None)
    operation: str = field(init=False, default=None)
    right: object | int = field(init=False, default=None)
    zValues: dict = field(init=False)
    
    def __post_init__(self) -> None:
        self.zValues = dict()
    
    def AND(self) -> int:
        return int(self.left == 1 and self.right == 1)

    def OR(self) -> int:
        return int(self.left == 1 or self.right == 1)

    def XOR(self) -> int:
        return int(self.left != self.right)

    def _checkParent(self) -> None:
        if not isinstance(self.parent, Gates):
            return
        self.parent.left = self.left
        self.parent.right = self.right
        self.zValues[self.parent.current] = self.parent.calculate()

    def calculate(self) -> int:
        if isinstance(self.left, int) and isinstance(self.right, int):
            self._checkParent()
            return getattr(self, self.operation)()
        if isinstance(self.left, Gates):
            value: int = self.left.calculate()
            self.zValues |= self.left.zValues
            self.left = value
        if isinstance(self.right, Gates):
            value: int = self.right.calculate()
            self.zValues |= self.right.zValues
            self.right = value
        self._checkParent()
        return getattr(self, self.operation)()
    
    def collapse(self) -> object:
        self.zValues[self.current] = self.calculate()
        return self

def build(current: str, wires: dict[str, int], operation: dict[str, list[str]], test: bool=False) -> Gates | int:
    if wires.get(current, None) is not None:
        return current if test else wires[current]
    gate = Gates(current=current)
    lt, op, rt = operation[current]
    gate.operation = op
    gate.left = build(lt, wires, operation, test)
    gate.right = build(rt, wires, operation, test)
    for z in sorted([chars for chars in gates.keys() if chars.startswith('z')], reverse=True):
        if current == z: continue
        if [operation[z][0], operation[z][2]] not in [[lt, rt], [rt, lt]]: continue
        gate.parent = Gates(current=z)
        gate.parent.left, gate.parent.right = lt, rt
        gate.parent.operation = operation[z][1]
    return gate

def visualize_gate_tree(gate: Gates, graph: Digraph=None, parent: Gates=None, edge_label: str=""):
    if graph is None:
        graph = Digraph()
        graph.attr(rankdir='BT')
    # Label for the current gate
    label = f"{gate.current}\n{gate.operation or ''}"
    if isinstance(gate, int):
        label = str(gate)
    # Add the current node to the graph
    graph.node(gate.current, label=label)
    if parent: # If child
        graph.edge(parent, gate.current, label=edge_label)
    if isinstance(gate.left, Gates):
        visualize_gate_tree(gate.left, graph, gate.current, "L")
    else:
        graph.node(f"{gate.current}_L", str(gate.left))
        graph.edge(gate.current, f"{gate.current}_L", label="L")
    if isinstance(gate.right, Gates):
        visualize_gate_tree(gate.right, graph, gate.current, "R")
    else:
        graph.node(f"{gate.current}_R", str(gate.right))
        graph.edge(gate.current, f"{gate.current}_R", label="R")
    if isinstance(gate.parent, Gates):
        graph.node(gate.parent.current, label=f"{gate.parent.current}\n{gate.parent.operation or ''}")
        graph.edge(gate.parent.current, gate.left if isinstance(gate.left, str) else gate.left.current, label="L")
        graph.edge(gate.parent.current, gate.right if isinstance(gate.right, str) else gate.right.current, label="R")
    return graph

def partOne(wires: dict[str, int], gates: dict[str, list[str]]) -> int:
    binary: dict[str, int] = {num: build(num, wires, gates).calculate() for num in sorted([chars for chars in gates.keys() if chars.startswith('z')], reverse=True)}
    return int(''.join(map(str, binary.values())), base=2)

def partTwo(wires: dict[str, int], gates: dict[str, list[str]]) -> str:
    # graph = visualize_gate_tree(build('z45', wires, gates, True))
    # graph.render(f"{dirname(realpath(__file__))}\\puzzle", format='pdf', cleanup=True)

    # See puzzle.pdf for more info.
    gates['z06'], gates['fhc'] = gates['fhc'], gates['z06'] # Nodes at z06
    gates['z11'], gates['qhj'] = gates['qhj'], gates['z11'] # Nodes at z11
    gates['mwh'], gates['ggt'] = gates['ggt'], gates['mwh'] # Nodes at z23
    gates['hqk'], gates['z35'] = gates['z35'], gates['hqk'] # Nodes at z35
    # graph = visualize_gate_tree(build('z45', wires, gates, True))
    # graph.render(f"{dirname(realpath(__file__))}\\solution", format='pdf', cleanup=True)
    for adder in range(45):
        _wires: dict[str, int] = {key: int(val) for key, val in zip(wires.keys(), f"{int('1' + '1'*adder):<045d}{int('1' + '1'*adder):<045d}")}
        nodes: Gates = build('z45', _wires, gates, test=False).collapse()
        assert int(f"{int('1' + '1'*adder):<045d}"[::-1], base=2) * 2 == int(''.join(map(str, nodes.zValues.values()))[::-1], base=2), f'POSITION: {adder}, SEQUENCE: {''.join(map(str, nodes.zValues.values()))[::-1]}'
        # print(f'{adder:02d}', int(f"{int('1' + '1'*adder):<045d}"[::-1], base=2)*2, int(''.join(map(str, nodes.zValues.values()))[::-1], base=2))
    return ','.join(sorted(['z06', 'fhc', 'z11', 'qhj', 'mwh', 'ggt', 'hqk', 'z35']))

if __name__ == "__main__":
    start: int = perf_counter_ns()
    wires, gates = fetchData(DATA)
    print(partOne(wires, gates))
    print(f'P1: {(perf_counter_ns()-start)/1e9} s')
    print(partTwo(wires, gates))
    print(f'P2: {(perf_counter_ns()-start)/1e9} s')
