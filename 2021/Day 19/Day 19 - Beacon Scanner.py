from itertools import combinations, permutations, product
from Beacon_Scanner import DATA, TEST

class Orientation:
    XYZ: list[tuple] = list(set(permutations([1,1,1,-1,-1,-1], 3))) # Set is used to remove duplicates
    POS: list[tuple] = [(0,1,2), (1,2,0), (2,0,1)]
    COMBINED: list[tuple, tuple] = list(product(XYZ, POS))

def getData(data: str) -> list:
    return [
        [eval(line) for line in beacons.splitlines() if len(line) != 0 and '--' not in line]
        for beacons in data.split('\n\n')
    ]

def otherStuff(x, y, offset):
    if x == (y[0]*offset[0], y[1]*offset[1], y[2]*offset[2]) or x == (y[0]*-offset[0], y[1]*-offset[1], y[2]*-offset[2]):
        print(x == (y[0]*offset[0], y[1]*offset[1], y[2]*offset[2]), x == (y[0]*-offset[0], y[1]*-offset[1], y[2]*-offset[2]))
    print(x, y, offset)

def tryStuff(sensor_one, sensor_two):
    offset = [0, 0, 0]
    offset[0] = sensor_one[0] - sensor_two[0]
    offset[1] = sensor_one[1] - sensor_two[1]
    offset[2] = sensor_one[2] - sensor_two[2]
    otherStuff(sensor_one, sensor_two, offset)


def partOne(data: list) -> int:
    for line in data[0]:
        for lines in data[1]:
            for (x, y, z), (one, two, three) in Orientation.COMBINED:
                tryStuff(line, (lines[one]*x, lines[two]*y, lines[three]*z))

def partTwo(data: list) -> int: ...

def main() -> None:
    data = getData(TEST)
    # print(list(product(Orientation.XYZ, Orientation.POS)))
    print(partOne(data))
    print(partTwo(data))

if __name__ == "__main__":
    main()

# Maybe this can be used to determine the location of the sensor.
# x = (sum(map(lambda i: i[pos[0]]*xyz[0], sensor_two)) + sum(map(lambda i: i[0], sensor_one))) / 12
# y = (sum(map(lambda i: i[pos[1]]*xyz[1], sensor_two)) + sum(map(lambda i: i[1], sensor_one))) / 12
# z = (sum(map(lambda i: i[pos[2]]*xyz[2], sensor_two)) + sum(map(lambda i: i[2], sensor_one))) / 12