from os.path import dirname, realpath
from functools import lru_cache
from math import log10, floor

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[int]:
    return list(map(int, data.split(' ')))

@lru_cache(maxsize=4000, typed=False)
def process(value: int) -> tuple[int, int | None]:
    if value == 0:
        return 1, None
    elif (floor(log10(value)) + 1) % 2 == 0:
        value: str = str(value)
        return int(value[:len(value)//2]), int(value[len(value)//2:])
    else:
        return value * 2024, None

def parts(data: list[int], blinks: int=25) -> int:
    stones: dict = {val: 1 for val in data}
    for _ in range(blinks):
        newStones: dict = dict()
        for key, val in stones.items():
            s1, s2 = process(key)
            newStones[s1] = newStones.setdefault(s1, 0) + val
            if s2 is not None:
                newStones[s2] = newStones.setdefault(s2, 0) + val
        stones = newStones
    return sum(stones.values())

if __name__ == "__main__":
    data: list[int] = fetchData(DATA)
    print(parts(data, blinks=25))
    print(parts(data, blinks=75))
