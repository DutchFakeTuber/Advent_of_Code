import numpy
from itertools import product

TEST: str = open("test.txt")
DATA: str = open("input.txt")

def getData(data: str) -> list:
    allLines: list = []
    for line in [info.split(' ') for info in [line for line in data.splitlines() if len(line) != 0]]:
        x, y, z = str(line[1]).split(',')
        allLines.append([
            0 if line[0] != 'on' else 1,
            [int(num) for num in x.strip('x=').split('..')],
            [int(num) for num in y.strip('y=').split('..')],
            [int(num) for num in z.strip('z=').split('..')],
        ])
    return allLines

def partOne(data: list) -> int:
    grid = numpy.array([[[0 for _ in range(-50, 51)] for _ in range(-50, 51)] for _ in range(-50, 51)], dtype=object)

    for state, _x, _y, _z in data:
        for x, y, z in product(range(_x[0], _x[1]+1), range(_y[0], _y[1]+1), range(_z[0], _z[1]+1)):
            grid[x][y][z] = state
    
    return numpy.count_nonzero(grid == 1)

def intersection(data, core):
    nodes = [-core[0]]
    for _d, _c in zip(data[1:], core[1:]):
        nodes.append([max([_d[0], _c[0]]), min([_d[1], _c[1]])])

    return None if nodes[1][0] > nodes[1][1] or nodes[2][0] > nodes[2][1] or nodes[3][0] > nodes[3][1] else [nodes]

def partTwo(data: list) -> int:
    cores: list = []
    for _data in data:
        addCore: list = [_data] if _data[0] == 1 else []
        for core in cores:
            inter = intersection(_data, core)
            if inter:
                addCore += inter
        cores += addCore
    
    countcubes: int = 0
    for core in cores:
        countcubes += (
            core[0]
            * (core[1][1]-core[1][0]+1)
            * (core[2][1]-core[2][0]+1)
            * (core[3][1]-core[3][0]+1)
        )
    
    return countcubes
    

def main() -> None:
    data = getData(DATA_50X50)
    print(partOne(data))
    data = getData(DATA)
    print(partTwo(data))

if __name__ == "__main__":
    main()