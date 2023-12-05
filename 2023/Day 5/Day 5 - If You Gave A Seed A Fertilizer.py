from If_You_Gave_A_Seed_A_Fertilizer import TEST, DATA

class Almanac:
    def __init__(self, data: str) -> None:
        self.seeds: list = [int(seed) for seed in data.splitlines()[0].strip('seeds: ').split(' ')]
        self.data: list = [line for line in data.splitlines()[3:] if len(line) > 0]
        self.locations: dict[int] = {seed: [] for seed in self.seeds}
    
    def getMaps(self) -> list[list[int]]:
        self.maps: dict = {}
        for num in range(7):
            index: int = [num for num, val in enumerate(self.data) if not val[0].isnumeric()]
            index: int = len(self.data) if not len(index) else index[0]
            self.maps[num] = [list(map(int, self.data.pop(0).split(' '))) for _ in range(index)]
            if len(self.data) and not self.data[0].isnumeric():
                self.data = self.data[1:]

    def checkMaps(self, seed: int, location: int, destination: int=0) -> None:
        recursion: bool = destination < len(self.maps) - 1
        present: bool = False
        for d, s, r in self.maps[destination]:
            if s <= location <= s+r:
                present = True
                if recursion:
                    self.checkMaps(seed, d+(location-s), destination=destination+1)
                else:
                    self.locations[seed].append(d+(location-s))
                    print(seed, d+(location-s))
                    return
        if not present:
            if recursion:
                self.checkMaps(seed, location, destination=destination+1)
            else:
                self.locations[seed].append(location)
                print(seed, location)
                return

    def process(self) -> int:
        self.getMaps()
        for seed in self.seeds:
            self.checkMaps(seed=seed, location=seed)

if __name__ == "__main__":
    almanac: Almanac = Almanac(TEST)
    almanac.process()
    print(almanac.locations)
    # print(*almanac.maps.values(), sep='\n')