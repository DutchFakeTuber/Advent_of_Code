from math import log10
from dataclasses import dataclass, field
from Bridge_Repair import TEST, DATA

def fetchData(data: str) -> dict[int, list[int]]:
    return {int(line.split(': ')[0]): list(map(int, line.split(': ')[1].split(' '))) for line in data.splitlines() if len(line)}

@dataclass(kw_only=True)
class Equation:
    value: int = field(init=True)
    numbers: list[int] = field(init=True)
    solutions: int = field(init=False, default=0)

    def solve(self, number: int=None, nextNumbers: list[int]=None, concatenation: bool = False) -> None:
        if number is None and nextNumbers is None:
            number = self.numbers[0]
            nextNumbers = self.numbers[1:]
        if nextNumbers == []:
            self.solutions += (number == self.value)
            return

        nextNumber: int = nextNumbers[0]
        remainingNumbers: list[int] = nextNumbers[1:]
        if number+nextNumber <= self.value:
            self.solve(number+nextNumber, remainingNumbers, concatenation=concatenation)
        if number*nextNumber <= self.value:
            self.solve(number*nextNumber, remainingNumbers, concatenation=concatenation)
        if concatenation:
            concatNumber: int = number * (10 ** (int(log10(nextNumber)) + 1)) + nextNumber
            if concatNumber <= self.value:
                self.solve(concatNumber, remainingNumbers, concatenation=concatenation)

def parts(data: dict[int, list[int]], concatenation: bool=False) -> int:
    calibration: int = 0
    for key, values in data.items():
        equation: Equation = Equation(value=key, numbers=values)
        equation.solve(concatenation=concatenation)
        if equation.solutions:
            calibration += equation.value
    return calibration

if __name__ == "__main__":
    data: dict[int, list[int]] = fetchData(DATA)
    print(parts(data, False))
    print(parts(data, True))
