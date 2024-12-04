from Reindeer_Olympics import TEST, DATA
from dataclasses import dataclass, field


class Stats:
    def __init__(self, speed: int, fly: int, rest: int) -> None:
        self.speed: int = speed
        self.fly: int = fly
        self.rest: int = rest
    
    def __iter__(self):
        return iter((self.speed, self.fly, self.rest))

@dataclass
class Reindeer:
    points: int
    distance: int
    stats: Stats
    current: Stats = field(init=False)
    
    def __post_init__(self) -> None:
        self.current = Stats(*self.stats)
        
    def check_fly(self) -> None:
        if not self.current.fly and not self.current.rest:
            self.current = Stats(*self.stats)
        if self.current.fly:
            self.current.fly -= 1
            self.distance += self.stats.speed
        elif self.current.rest:
            self.current.rest -= 1
    
    def check_distance(self, dist: list[int]) -> None:
        if max(dist) == self.distance:
            self.points += 1

def getData(data: str) -> list[list[int]]:
    return [[int(line.split()[3]), int(line.split()[6]), int(line.split()[-2])] for line in data.splitlines() if len(line)]

def partOne(data: dict[dict[int]], seconds: int=2503) -> int:
    full: function = lambda f, r: int(seconds / (f + r))
    left: function = lambda f, r: seconds - (full(f, r) * (f + r))
    return max(full(fly, rest) * (fly * speed) + speed * (fly if left(fly, rest) > fly else left(fly, rest)) for speed, fly, rest in data)

def partTwo(data: dict[dict[int]], seconds: int=2503) -> int:
    reindeers: list[Reindeer] = [Reindeer(0, 0, Stats(s, f, r)) for s, f, r in data]
    for _ in range(seconds):
        for reindeer in reindeers:
            reindeer.check_fly()
        distance: list = [reindeer.distance for reindeer in reindeers]
        for reindeer in reindeers:
            reindeer.check_distance(distance)
    return max(reindeer.points for reindeer in reindeers)

if __name__ == "__main__":
    data: dict[dict[int]] = getData(DATA)
    print(partOne(data))
    print(partTwo(data))
