from Aplenty import TEST, DATA

def fetchData(data: str) -> tuple[dict, list[dict]]:
    split: int = [num for num, val in enumerate(data.splitlines()) if not len(val)][0]
    workflow: dict = {line.split('{')[0]: line.split('{')[1][:-1].split(',') for line in data.splitlines()[:split]}
    ratings: list[dict] = [{value[0]: int(value[2:]) for value in line[1:-1].split(',')} for line in data.splitlines()[split+1:]]
    return workflow, ratings

class Node:
    def __init__(self,
                 x: range=range(1, 4001),
                 m: range=range(1, 4001),
                 a: range=range(1, 4001),
                 s: range=range(1, 4001)) -> None:
        self.x, self.m, self.a, self.s = x, m, a, s
    
    def __len__(self) -> int:
        return len(self.x)*len(self.m)*len(self.a)*len(self.s)
    
    def copy(self) -> object:
        return Node(self.x, self.m, self.a, self.s)
    
    def process(self, xmas: str, operation: str, value: int) -> None:
        left: Node = self.copy()
        right: Node = self.copy()
        rating: range = getattr(self, xmas)
        if operation == '>':
            l: range = range(value+1, rating.stop)
            r: range = range(rating.start, value+1)
        elif operation == '<':
            l: range = range(rating.start, value)
            r: range = range(value, rating.stop)
        setattr(left, xmas, l)
        setattr(right, xmas, r)
        return left, right

def checkNodes(workflow: dict, work: str, node: Node) -> int:
    if work == 'A':
        return len(node)
    elif work == 'R':
        return 0
    total: int = 0
    *conditions, default = workflow[work]
    for cond in conditions:
        cond, target = cond.split(':')
        lnode, node = node.process(cond[0], cond[1], int(cond[2:]))
        total += checkNodes(workflow, target, lnode)
    return total + checkNodes(workflow, default, node)

def check(ratings: list[dict], workflow: dict, work: str='in') -> str:
    parse: function = lambda x: (x[0], x[1], int(x[2:].split(':')[0]), x[2:].split(':')[1])
    while work not in ['A', 'R']:
        for w in workflow[work]:
            if '<' in w or '>' in w:
                char, inst, num, move = parse(w)
                if (ratings[char] < num) if inst == '<' else (ratings[char] > num):
                    work = move
                    break
            else:
                work = w
                break
    return work

def partOne(workflow: dict, ratings: list[dict]) -> int:
    accepted: list = []
    for r in ratings:
        if check(r, workflow) == 'A':
            accepted.append(r)
    return sum([sum(a.values()) for a in accepted])

def partTwo(workflow: dict, ratings: list[dict]) -> int:
    return checkNodes(workflow, 'in', Node())

if __name__ == "__main__":
    workflow, ratings = fetchData(DATA)
    print(partOne(workflow, ratings))
    print(partTwo(workflow, ratings))
