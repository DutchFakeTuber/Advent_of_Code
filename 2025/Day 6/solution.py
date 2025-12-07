from os.path import dirname, realpath
from math import prod

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> tuple[list[list[int]], list[str]]:
    locations: list[int] = [[start, end-2] for start, end in zip([pos for pos, val in enumerate(data.splitlines()[-1]) if val != ' '], [pos for pos, val in enumerate(data.splitlines()[-1]) if val != ' '][1:]+[len(data.splitlines()[0])+1])]
    operations: list[str] = [char for char in data.splitlines()[-1].split(' ') if len(char)]
    data: list[list[str]] = [[line[start:end+1] for start, end in locations] for line in data.splitlines()[:-1]]
    return list(map(list, zip(*[val for val in data]))), operations

def partOne(data: list[list[int]], operations: list[str]) -> int:
    return sum([sum(map(int, data[pos])) if operations[pos] == '+' else prod(map(int, data[pos])) for pos in range(len(data))])

def partTwo(data: list[list[int]], operations: list[str]) -> int:
    return sum([sum([int(''.join(v)) for v in zip(*[val for val in row])][::-1]) if (operations[::-1])[pos] == '+' else prod([int(''.join(v)) for v in zip(*[val for val in row])][::-1]) for pos, row in enumerate(data[::-1])])

if __name__ == "__main__":
    data, operations = fetchData(DATA)
    print(partOne(data, operations))
    print(partTwo(data, operations))
