from os.path import dirname, realpath
from dataclasses import dataclass
from collections import deque
import pulp
import re

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()


@dataclass
class Factory:
    state: list[bool]
    buttons: list[tuple[int]]
    joltage: list[int]

def fetchData(data: str) -> list[Factory]:
    return [Factory(state=[char == '#' for char in re.search(r'\[(.*?)\]', line).group(1)],
                    buttons=[eval(chars) if isinstance(eval(chars), tuple) else tuple([eval(chars)]) for chars in re.findall(r'\([^)]*\)', line)],
                    joltage=list(map(int, re.search(r'\{(.*?)\}', line).group(1).split(','))))
            for line in data.splitlines()]

def buttonTree(factory: Factory) -> int:
    # Deque [(button_press, [indicator_state], [pressed_buttons])]
    tree: deque = deque([(0, [False]*len(factory.state))])
    while len(tree):
        press, indicator = tree.popleft()
        for button in factory.buttons:
            new_indicator: list[bool] = [not i if num in button else i for num, i in enumerate(indicator)]
            new_press = press + 1
            if new_indicator == factory.state:
                return new_press
            tree.append((new_press, new_indicator))

def joltageSolve(factory: Factory) -> int:
    numTarget: int = len(factory.joltage)
    numButton: int = len(factory.buttons)
    problem: pulp.LpProblem = pulp.LpProblem('MinPresses', pulp.LpMinimize)
    variables: list[pulp.pulp.LpVariable] = [pulp.LpVariable(f'x{num}', lowBound=0, cat='Integer') for num in range(numButton)]
    problem += pulp.lpSum(variables)
    for target in range(numTarget):
        problem += pulp.lpSum(variables[num] for num in range(numButton) if target in factory.buttons[num]) == factory.joltage[target]
    status = problem.solve(pulp.PULP_CBC_CMD(msg=0))
    if status != 1:
        print('HELP')
    return int(pulp.value(problem.objective))

def partOne(data: list[Factory]) -> int:
    return sum([buttonTree(factory) for factory in data])

def partTwo(data: list[Factory]) -> int:
    return sum([joltageSolve(factory) for factory in data])

if __name__ == "__main__":
    data: list[Factory] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
