from dataclasses import dataclass
from itertools import product
from functools import reduce
from operator import mul
from Science_for_Hungry_People import TEST, DATA

@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int
    
    def calculate(self, mult: int) -> list[int]:
        return [self.capacity * mult, self.durability * mult, self.flavor * mult, self.texture * mult]

    def kcal(self, mult: int) -> int:
        return self.calories * mult

def getData(data: str) -> list[Ingredient]:
    return [Ingredient(line.split()[0][:-1], *map(lambda x: int(x[:-1]), line.split()[2:9:2]), int(line.split()[10])) for line in data.splitlines() if len(line)]

def partOne(data: list[Ingredient]) -> int:
    def score(data: list[list[int]]) -> int:
        _sum: function = lambda val: sum(val) if sum(val) > 0 else 0
        return reduce(mul, map(_sum, zip(*data[::-1])))
    return max([score([i.calculate(v) for i, v in zip(data, [one, two, three, four])]) for one, two, three, four in product(range(1, 101), range(1, 101), range(1, 101), range(1, 101)) if one + two + three + four == 100])

def partTwo(data: list[Ingredient]) -> int:
    def score(data: list[list[int]]) -> int:
        _sum: function = lambda val: sum(val) if sum(val) > 0 else 0
        return reduce(mul, map(_sum, zip(*data[::-1])))
    return max([score([i.calculate(v) for i, v in zip(data, [one, two, three, four])]) for one, two, three, four in product(range(1, 101), range(1, 101), range(1, 101), range(1, 101)) if one + two + three + four == 100 and sum(i.kcal(v) for i, v in zip(data, [one, two, three, four])) == 500])

if __name__ == "__main__":
    data: list[Ingredient] = getData(DATA)
    print(partOne(data))
    print(partTwo(data))
