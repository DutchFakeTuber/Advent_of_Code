from dataclasses import dataclass, field
from Wait_For_It import TEST, DATA

def fetchData(data: str) -> list[int]:
    time: list = data.splitlines()[0].strip('Time:').split()
    distance: list = data.splitlines()[1].strip('Distance:').split()
    return [[int(time), int(distance)] for time, distance in zip(time, distance)]

# @dataclass(kw_only=True)
# class Boat:
#     hold_time: int = field(init=True, default_factory=int)
#     max_time: int = field(init=True, default_factory=int)
#     current_time: int = field(init=False, default_factory=int)
#     millimeters: int = field(init=False, default_factory=int)
#     movement_speed: int = field(init=False, default_factory=int)
    
#     def __post_init__(self) -> None:
#         self.current_time = self.hold_time
#         self.movement_speed = self.hold_time
#         self.millimeters = 0
#         for _ in range(self.max_time-self.current_time):
#             self.millimeters += self.movement_speed
    
#     def distance(self) -> int:
#         return self.millimeters

# @dataclass(kw_only=True)
# class Race:
#     time: int = field(init=True, default_factory=int)
#     distance: int = field(init=True, default_factory=int)
#     boats: list[int] = field(init=False, default_factory=list)
    
#     def __post_init__(self) -> None:
#         for millisecond in range(self.time+1):
#             boat: Boat = Boat(hold_time=millisecond, max_time=self.time)
#             if boat.distance() > self.distance:
#                 self.boats.append(boat.distance())

def partOne(data: dict) -> int:
    calc: function = lambda m, t: m*(t-m)
    records: int = 1
    for time, dist in data:
        records *= len([calc(mov, time) for mov in range(dist+1) if calc(mov, time) > dist])
    return records

def partTwo(data: dict) -> int:
    # movement * (total - movement) > record <- can be rearranged as:
    # -movement**2 + total*movement - record > 0  <- where movement = -1
    data: list = [int(''.join(map(str, (x[0] for x in data)))), int(''.join(map(str, (x[1] for x in data))))]
    print((-data[0] + (data[0]**2 - 4*data[1])**.5)/-2)
    print((-data[0] - (data[0]**2 - 4*data[1])**.5)/-2)

if __name__ == "__main__":
    data: dict[int] = fetchData(TEST)
    print(partOne(data))
    print(partTwo(data))
