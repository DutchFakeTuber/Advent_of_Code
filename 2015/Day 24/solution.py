from os.path import dirname, abspath
from itertools import combinations
from functools import reduce
from operator import mul

TEST: str = open(f'{dirname(abspath(__file__))}\\test.txt').read()
DATA: str = open(f'{dirname(abspath(__file__))}\\input.txt').read()

def fetchData(data: str) -> list[int]:
    return list(map(int, (line for line in data.splitlines() if len(line))))

def parts(data: list[int], partitions: int) -> int:
    partition_size: int = sum(data) // partitions
    for size in range(len(data)):
        hits: list[list[int]] = [list(comb) for comb in combinations(data, size) if sum(comb) == partition_size]
        if len(hits):
            return reduce(mul, hits[0])

if __name__ == "__main__":
    data: list[int] = fetchData(DATA)
    print(parts(data, 3))
    print(parts(data, 4))
