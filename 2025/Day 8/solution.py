from os.path import dirname, realpath
from math import sqrt, prod

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[list[int]]:
    return [list(map(int, line.split(','))) for line in data.splitlines()]

def findPairs(circuits: list[int, list[int]], jbx: list[int]) -> int | None:
    for num, val in enumerate(circuits):
        if jbx in val:
            return num
    return None

def parts(data: list[list[int]], length: int, partOne: bool = True) -> int:
    distances: list[int, list[list[int]]] = []
    for x in range(len(data)):
        for y in range(x+1, len(data)):
            distances.append([sqrt((data[x][0]-data[y][0])**2 + (data[x][1] - data[y][1])**2 + (data[x][2] - data[y][2])**2), [x, y]])
    distances.sort(reverse=True)
    # print(distances)
    connections: list[set[int]] = [{n} for n in range(len(data))]
    while length if partOne else True:
        length -= 1
        x, y = distances.pop()[1]
        jb1, jb2 = findPairs(connections, x), findPairs(connections, y)
        if jb1 != jb2:
            connections[jb1] = connections[jb1] | connections[jb2]
            del connections[jb2]
        if not partOne:
            if len(connections) == 1: break
    return prod(map(len, sorted(connections, reverse=True, key=len)[0:3])) if partOne else data[x][0] * data[y][0]

if __name__ == "__main__":
    test: bool = False
    data: list[list[int]] = fetchData(TEST if test else DATA)
    print(parts(data, length=10 if test else 1_000, partOne=True))
    print(parts(data, length=10 if test else 1_000, partOne=False))
