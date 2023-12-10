import math
from Haunted_Wasteland import TEST, DATA

def fetchData(data: str) -> tuple[list, dict]:
    steps: list = [*data.splitlines()[0]]
    nodes: dict = {line.split(' = ')[0]: [line.split(' = ')[1][1:4], line.split(' = ')[1][6:9]] for line in data.splitlines()[2:]}
    return steps, nodes

def walkNodes(steps: str, nodes: dict, start: str, end: list[str]) -> int:
    found: bool = False
    counter: int = 0
    position: str = start
    while not found:
        position: str = nodes[position][0 if steps[counter % len(steps)] == 'L' else 1]
        if position in end:
            found: bool = True
        counter += 1
    return counter

def partOne(steps: list, nodes: dict) -> int:
    return walkNodes(steps, nodes, 'AAA', ['ZZZ'])

def partTwo(steps: list, nodes: dict) -> int:
    start: list = [node for node in nodes if node[2] == 'A']
    end: list = [node for node in nodes if node[2] == 'Z']
    return math.lcm(*[walkNodes(steps, nodes, begin, end) for begin in start])

if __name__ == "__main__":
    steps, nodes = fetchData(DATA)
    print(partOne(steps, nodes))
    print(partTwo(steps, nodes))
