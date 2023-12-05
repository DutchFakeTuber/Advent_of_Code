from If_You_Gave_A_Seed_A_Fertilizer import TEST, DATA

class Almanac:
    def __init__(self, data: str) -> None:
        self.seeds: list = [int(seed) for seed in data.splitlines()[0].strip('seeds: ').split(' ')]
        self.data: list = [line for line in data.splitlines()[3:] if len(line) > 0]
        self.location: int = 10**50
        self.found: bool = False
    
    def getMaps(self) -> list[list[int]]:
        self.maps: dict = {}
        for num in range(7):
            index: int = [num for num, val in enumerate(self.data) if not val[0].isnumeric()]
            index: int = len(self.data) if not len(index) else index[0]
            self.maps[num] = [list(map(int, self.data.pop(0).split(' '))) for _ in range(index)]
            if len(self.data) and not self.data[0].isnumeric():
                self.data = self.data[1:]

    def checkMaps(self, location: int, destination: int=0) -> None:
        if self.found: return
        recursion: bool = destination < len(self.maps) - 1
        present: bool = False
        for d, s, r in self.maps[destination]:
            if s <= location <= s+r:
                present = True
                if recursion:
                    self.checkMaps(d+(location-s), destination=destination+1)
                elif not self.found:
                    self.location = min([self.location, d+(location-s)])
                    self.found = True
                    return
        if not present:
            if recursion:
                self.checkMaps(location, destination=destination+1)
            elif not self.found:
                self.location = min([self.location, location])
                self.found = True
                return
    
    def partTwo(self, location: list[list[int]], destination=0) -> int:
        recursion: bool = destination < len(self.maps) - 1
        currMap: list = location
        nextMap: list = []
        for d, s, r in self.maps[destination]:
            position: int = 0
            while position < len(currMap):
                if currMap[position][-1] < s: pass
                elif currMap[position][0] > s+r: pass
                else:
                    ##### BETWEEN THESE LINES SHOULD BE ENHANCED
                    curr: set = set(range(currMap[position][0], currMap[position][-1]+1))
                    dest: set = set(range(s, s+r+1))
                    intersect: set = dest.intersection(curr)
                    intersect: list[int, int] = [min(intersect), max(intersect)]
                    ##### BETWEEN THESE LINES SHOULD BE ENHANCED
                    nextMap.append(list([d+(intersect[0]-s), d+(intersect[1]-s)]))
                    if currMap[position][0] < intersect[0]:
                        currMap.append([currMap[position][0], intersect[0]-1])
                    if currMap[position][1] > intersect[1]:
                        currMap.append([currMap[position][0], intersect[1]+1])
                    currMap = [*currMap[:position], *currMap[position+1:]]
                position += 1
        if destination < len(self.maps):
            nextMap = [*nextMap, *currMap]
        if recursion:
            self.partTwo(nextMap, destination=destination+1)
        if not self.found:
            self.location = min([self.location, min([min(nums) for nums in nextMap])])
            self.found = True

    def process(self) -> int:
        for seed in self.seeds:
            self.found = False
            self.checkMaps(location=seed)
        return self.location

def partOne(data: str) -> int:
    almanac: Almanac = Almanac(data)
    almanac.getMaps()
    seeds: list = almanac.seeds
    for seed in range(len(seeds)):
        almanac.seeds = [seeds[seed]]
        almanac.process()
    return almanac.location

def partTwo(data: str):
    almanac: Almanac = Almanac(data)
    almanac.getMaps()
    seeds: list = almanac.seeds
    for seed in range(0, len(seeds), 2):
        almanac.found = False
        almanac.seeds = [[seeds[seed], seeds[seed]+seeds[seed+1]]]
        almanac.partTwo(almanac.seeds)
    return almanac.location

if __name__ == "__main__":
    print(partOne(DATA))
    print(partTwo(DATA))
