from Sand_Slabs import TEST, DATA
from collections import defaultdict
from itertools import product

def fetchData(data: str) -> list[list[int]]:
    splitter: function = lambda l: [n for c in l.split('~') for n in c.split(',')]
    return sorted([list(map(int, splitter(line))) for line in data.splitlines()], key=lambda x: x[2])

def drop(coordinates: list[list[int]], skip: int=None) -> tuple[bool, int]:
    peaks: defaultdict = defaultdict(int)
    falls: int = 0

    for num, (x1, y1, z1, x2, y2, z2) in enumerate(coordinates):
        # start: (x1, y1, z1), end: (x2, y2, z2)
        if num == skip: continue # If the current row is equal to skip
        # Get (x, y) coordinates as area
        area: tuple[tuple[int]] = tuple(product(range(x1, x2+1), range(y1, y2+1)))
        # Get tallest peak of the given area. Increment by one.
        peak: int = max(map(lambda x: peaks[x], area)) + 1
        for xy in area:
            # Rewrite Z-coordinate with its previous peak
            # and offset it with the z2-z1 coordinates.
            peaks[xy] = peak + z2-z1
        # Rewrite coordinates with the newly fetched peaks.
        coordinates[num] = (x1, y1, peak, x2, y2, peak+z2-z1)
        # Increment falls by 1 peak is lower than z1
        falls += peak < z1
    return not falls, falls

def parts(coordinates: list[list[int]]) -> int:
    drop(coordinates) # Let the floating bricks fall
    safe: int = 0
    chain: int = 0
    for z in range(len(coordinates)):
        s, c = drop(coordinates.copy(), skip=z)
        safe += s # True is 1, False is 0
        chain += c
    return safe, chain

if __name__ == "__main__":
    coordinates: list[list[int]] = fetchData(DATA)
    print(*parts(coordinates), sep='\n')
