from os.path import dirname, realpath
from collections import namedtuple
import re

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[list[int]]:
    return [list(map(int, re.findall(r'\b\d+\b', line))) for line in data.split('\n\n') if len(line)]

def CramersRule(b: tuple[int]) -> int:
    A, B = (b.px*b.by-b.bx*b.py)/(b.ax*b.by-b.bx*b.ay), (b.ax*b.py-b.px*b.ay)/(b.ax*b.by-b.bx*b.ay)
    return 3*A+B if A.is_integer() and B.is_integer() else 0

def parts(data: list[list[int]], long: bool=False) -> int:
    Button = namedtuple('Button', ['ax', 'ay', 'bx', 'by', 'px', 'py'])
    return int(sum(CramersRule(Button(*d[:4], 1e13+d[4], 1e13+d[5]) if long else Button(*d)) for d in data))

if __name__ == "__main__":
    data: list[list[int]] = fetchData(DATA)
    print(parts(data))
    print(parts(data, long=True))
