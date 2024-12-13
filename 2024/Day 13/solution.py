from os.path import dirname, realpath
from math import gcd
from collections import namedtuple
import re

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[list[int]]:
    return [list(map(int, re.findall(r'\b\d+\b', line))) for line in data.split('\n\n') if len(line)]

def partOne(data: list[list[int]]) -> int:
    Button = namedtuple('Button', ['ax', 'ay', 'bx', 'by', 'px', 'py'])
    calcA: function = lambda b: (b.px*b.by-b.bx*b.py)/(b.ax*b.by-b.bx*b.ay)
    calcB: function = lambda b: (b.ax*b.py-b.px*b.ay)/(b.ax*b.by-b.bx*b.ay)
    return int(sum([3*calcA(b)+calcB(b) for b in [Button(*d) for d in data] if calcA(b).is_integer() and calcB(b).is_integer()]))

def partTwo(data: list[list[int]]) -> int:
    Button = namedtuple('Button', ['ax', 'ay', 'bx', 'by', 'px', 'py'])
    calcA: function = lambda b: (b.px*b.by-b.bx*b.py)/(b.ax*b.by-b.bx*b.ay)
    calcB: function = lambda b: (b.ax*b.py-b.px*b.ay)/(b.ax*b.by-b.bx*b.ay)
    return int(sum([3*calcA(b)+calcB(b) for b in [Button(*d[:4], 1e13+d[4], 1e13+d[5]) for d in data] if calcA(b).is_integer() and calcB(b).is_integer()]))

if __name__ == "__main__":
    data: list[list[int]] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
