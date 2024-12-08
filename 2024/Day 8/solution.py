from os.path import dirname, realpath
from typing import Callable
from itertools import combinations, product, chain

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[int]:
    return [line for line in data.splitlines() if len(line)]

def antinode(ant: list[complex, complex], borders: list[int]) -> set:
    offset: complex = complex(ant[0].real-ant[1].real, ant[0].imag-ant[1].imag)
    coords: list[complex] = [ant[0] - offset, ant[1] + offset] if (ant[0]+offset) == ant[1] else [ant[0] + offset, ant[1] - offset]
    return set(coord for coord in coords if borders[0] <= coord.real < borders[2] and borders[1] <= coord.imag < borders[3])

def resonant(ant: list[complex, complex], borders: list[int]) -> set:
    offset: complex = complex(ant[0].real-ant[1].real, ant[0].imag-ant[1].imag)
    antinodes: set = set()
    stack: list = [ant]
    while stack:
        ant: list[complex, complex] = stack.pop()
        coords: list[complex] = [ant[0] - offset, ant[1] + offset] if (ant[0]+offset) == ant[1] else [ant[0] + offset, ant[1] - offset]
        for id, coord in enumerate(coords):
            if coord in antinodes: continue
            if borders[0] <= coord.real < borders[2] and borders[1] <= coord.imag < borders[3]:
                antinodes.add(coord)
                stack.append([ant[id], coord])
    return antinodes

def parts(data: list[str], locations: Callable) -> int:
    antennas: dict[str, set[complex]] = {char: {complex(row, col) for row, col in product(range(len(data)), range(len(data[0]))) if data[row][col] == char} for char in {char for line in data for char in line if char != '.'}}
    antinodes: set = set(chain(*antennas.values()))
    for antenna in antennas.values():
        for ant1, ant2 in combinations(antenna, 2):
            antinodes = antinodes.union(locations([ant1, ant2], [0, 0, len(data), len(data[0])]))
    return len(antinodes)

if __name__ == "__main__":
    data: list[str] = fetchData(DATA)
    print(parts(data, antinode))
    print(parts(data, resonant))
