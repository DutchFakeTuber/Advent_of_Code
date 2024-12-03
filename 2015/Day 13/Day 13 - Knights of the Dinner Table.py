from math import sqrt
from itertools import permutations
from multiprocessing import Pool, cpu_count
from Knights_of_the_Dinner_Table import TEST, DATA

def getData(data: str, includeYou: bool) -> dict[str, dict[str, int]]:
    data: list[str] = [d for d in data.splitlines() if len(d)]
    length: int = int(sqrt(len(data)))
    persons: dict = dict()
    for pos in range(0, len(data), length):
        persons[data[pos].split()[0]] = {p: v*m for p, m, v in map(lambda l: [l.split()[-1][:-1], 1 if l.split()[2] == "gain" else -1, int(l.split()[3])], data[pos:pos+length])}
        if includeYou:
            persons[data[pos].split()[0]].update({"You": 0})
    if includeYou:
        persons["You"] = {p: 0 for p in persons.keys()}
    return persons

def calculate(data: dict[str, dict[str, int]], person: str, left: str, right: str) -> int:
    return data[person][left] + data[person][right]
    
def calculateTable(args) -> int:
    data, circ, table = args
    return sum(calculate(data, table[pos], table[a], table[b]) for pos, (a, b) in enumerate(circ))

def parts(data: dict[str, dict[str, int]]) -> int:
    circulate: list[list[int, int]] = [[num, (num+2)%len(data.keys())] for num in range(-1, len(data.keys())-1)]
    args: tuple[list, function, tuple] = ((data, circulate, t) for t in permutations(data.keys()))
    with Pool(cpu_count()) as pool:
        return max(pool.map(calculateTable, args))
    
if __name__ == "__main__":
    data: dict[str, dict[str, int]] = getData(DATA, False)
    print(parts(data))
    data: dict[str, dict[str, int]] = getData(DATA, True)
    print(parts(data))
