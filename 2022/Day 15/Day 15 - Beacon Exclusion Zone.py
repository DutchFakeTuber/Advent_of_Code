from multiprocessing import Pool
from Beacon_Exclusion_Zone import INPUT

def getData() -> list:
    f: function = lambda l, n: l.split(' ')[n].split('=')[1]
    return [list(map(int, [f(l, 2)[:-1], f(l, 3)[:-1], f(l, 8)[:-1], f(l, 9)])) for l in INPUT.splitlines() if len(l) != 0]

class Beacons:
    def __init__(self, sensors: list[int, int], beacons: list[int, int]) -> None:
        self.beacons: list[int, int] = beacons
        self.sensors: list[int, int] = sensors
        self.areas: dict = dict()
        self.cell: bool = False

    def diamonds(self, row) -> int:
        if self.cell: return
        min_max: list[int, int] = [0, 4_000_000]
        values: list[list[int, int]] = sorted(self.line(row))
        v: list[list[int, int]] = [values[0]]
        v[0][0] = v[0][0] if v[0][0] >= min_max[0] else min_max[0]
        v[0][1] = v[0][1] if v[0][1] <= min_max[1] else min_max[1]
        for val in values[1:]:
            for num, _v in enumerate(v):
                if val[0] <= min_max[0] or _v[0] <= val[0] <= _v[1]:
                    v[num] += val if val[0] >= min_max[0] else [min_max[0], val[1]]
                    v[num] = [min(v[num]), max(v[num])]
                    if v[-1][1] > min_max[1]:
                        break
                else:
                    self.cell = True
                    return row, values
    
    def line(self, place: int) -> list[list[int, int]]:
        row: list = []
        for key, val in self.areas.items():
            if val['u'] <= place <= val['d']:
                if place > eval(key)[1]:
                    row.append([eval(key)[0]-((val['d']-place)*2+1)//2, eval(key)[0]+((val['d']-place)*2+1)//2])
                else:
                    row.append([eval(key)[0]-((place-val['u'])*2+1)//2, eval(key)[0]+((place-val['u'])*2+1)//2])
        return row

    def area(self) -> None:
        for num, sensor in enumerate(self.sensors):
            dist = abs(sensor[0]-self.beacons[num][0]) + abs(sensor[1]-self.beacons[num][1])
            self.areas[f'{sensor}'] = {
                'l': sensor[0]+dist*-1, 'r': sensor[0]+dist,
                'u': sensor[1]+dist*-1, 'd': sensor[1]+dist,
            }

def partOne(num: int) -> int:
    units: list[list[int, int]] = getData()
    beacons: Beacons = Beacons([x[:2] for x in units], [x[2:] for x in units])
    beacons.area()
    row: list[list[int, int]] = beacons.line(num)
    positions: set = set()
    for r in row:
        for c in range(r[0], r[1]+1):
            positions.add(c)
    for sb in [*beacons.sensors, *beacons.beacons]:
        if sb[1] == num and sb[0] in positions:
            positions.remove(sb[0])
    return len(positions)

def partTwo(area: list[int, int]) -> int:
    units: list[list[int, int]] = getData()
    beacons: Beacons = Beacons([x[:2] for x in units], [x[2:] for x in units])
    beacons.area()
    result: list = []
    with Pool(processes=5) as p:
        res = p.map(beacons.diamonds, (range(area[0], area[1]+1)))
        for r in res:
            if r and len(result) == 0:
                result = r
    print(result)
    for c1, c2 in zip(result[1], result[1][1:]):
        if c2[0] - c1[1] == 2:
            return (c1[1] + 1) * 4_000_000 + result[0]

def main() -> None:
    print(f'ANSWER PART ONE: {partOne(2_000_000)}')
    print(f'ANSWER PART TWO: {partTwo([0, 4_000_000])}')

if __name__ == '__main__':
    main()
