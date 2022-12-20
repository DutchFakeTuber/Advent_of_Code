from collections import deque
from Grove_Positioning_System import INPUT

def getData(multiply: int = 1) -> list[list[int, int]]:
    return [(num, int(val) * multiply) for num, val in enumerate(line for line in INPUT.splitlines() if len(line) != 0)]

class GPS:
    def __init__(self, data: list[list[int, int]]) -> None:
        self.data = deque([d for d in data])
        self.length: int = len(data)

    def index(self) -> int:
        return [(num, val) for num, val in enumerate(self.data) if val[0] == self.counter][0]
        
    def process(self) -> None:
        self.counter = 0
        while self.counter < self.length:
            position: int = self.index()
            self.data.remove(position[1])
            self.data.rotate(-position[1][1])
            self.data.insert(position[0], position[1])
            self.counter += 1

def partOne() -> int:
    data: list[list[int, int]] = getData()
    gps: GPS = GPS(data)
    gps.process()
    zero: int = [num for num, val in enumerate(gps.data) if val[1] == 0][0]
    return sum(gps.data[(zero+num)%gps.length][1] for num in [1_000, 2_000, 3_000])

def partTwo() -> int:
    data: list[list[int, int]] = getData(multiply=811_589_153)
    gps: GPS = GPS(data)
    for _ in range(10):
        gps.process()
    zero: int = [num for num, val in enumerate(gps.data) if val[1] == 0][0]
    return sum(gps.data[(zero+num)%gps.length][1] for num in [1_000, 2_000, 3_000])

def main() -> None:
    print(f'ANSWER PART ONE: {partOne()}')
    print(f'ANSWER PART TWO: {partTwo()}')

if __name__ == "__main__":
    main()
