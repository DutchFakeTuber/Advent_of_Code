import ast
import typing
import math
from dataclasses import dataclass
from Snailfish import DATA

from pprint import pprint
# Inspiration from: https://github.com/alexander-yu/adventofcode/blob/master/problems_2021/18.py
@dataclass
class Explode: ...

@dataclass
class Reduce: ...

@dataclass
class Node:
    value: typing.Optional['Node'] = None
    left: typing.Optional['Node'] = None
    right: typing.Optional['Node'] = None

    # Set the converted data (from getData) in the dataclass object.
    def setData(self, number):
        if isinstance(number, int):
            return Node(
                value=number
            )
        left, right = number
        return Node(
            left=Node().setData(left),
            right=Node().setData(right)
        )

    # Process data from string to dataclass.
    def getData(self, data: str):
        return [[Node().setData(number) for number in ast.literal_eval(line)] for line in data.splitlines() if len(line) != 0]

    def copyNode(self):
        return Node(
            value=self.value,
            left=self.left.copyNode() if self.left else None,
            right=self.right.copyNode() if self.right else None,
        )

    def reduce(self): ...

def partOne(data: str) -> int:
    values = Node().getData(data)
    pprint(values)

def partTwo(data: str) -> int: ...

def main() -> None:
    print(partOne(DATA))
    print(partTwo(DATA))

if __name__ == "__main__":
    main()