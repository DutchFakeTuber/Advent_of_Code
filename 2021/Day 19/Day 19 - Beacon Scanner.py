from itertools import combinations, permutations, product
from collections import defaultdict
from Beacon_Scanner import DATA, TEST

class Helpers:
    XYZ: list[tuple] = list(set(permutations([1,1,1,-1,-1,-1], 3))) # Set is used to remove duplicates
    POS: list[tuple] = [(0,1,2), (1,2,0), (2,0,1)]
    COMBINED: list[tuple, tuple] = list(product(XYZ, POS))

    def getData(self, data: str) -> list:
        input_data = data.strip().split('\n')
        scanners: list = []
        scanner = None
        scanner_count: int = 0
        for row in input_data:
            if not row:
                continue
            if row.startswith('---'):
                scanner = Scanner(scanner_id=scanner_count)
                scanners.append(scanner)
                scanner_count += 1
            else:
                # assert scanner is not None
                coord = tuple(map(int, row.split(',')))
                scanner.add_beacon(coord)
        
        for scanner in scanners:
            scanner.finalize()
        
        beacon_matches = defaultdict(set)
        for sid, scanner in enumerate(scanners):
            for _scanner in scanners[sid:]:
                potential_beacon_mathes = scanner.matchBeacon(_scanner)
                for beacon, beacon_match in potential_beacon_mathes.items():
                    beacon_matches[beacon].add(beacon_match)
                    beacon_matches[beacon_match].add(beacon)
        
        canonical = [0]
        scanners[0].pos = (0, 0, 0)
        scanners[0].orientation = (self.COMBINED[0][0], self.COMBINED[0][1])

        iterations = 0
        while len(canonical) < len(scanners) and iterations <= len(scanners):
            for sb1, values in beacon_matches.items():
                if not sb1[0] in canonical:
                    continue
                beacon_one = scanners[sb1[0]].getBeacon(sb1[1])
                for sb2 in values:
                    if sb2[0] in canonical:
                        continue
                    beacon_two = scanners[sb2[0]].getBeacon(sb2[1])
                    for orientation in self.COMBINED:
                        dpos = self.getDifference(beacon_one.pos, self.orientation(beacon_two.pos, orientation[0], orientation[1]))
                        _beacon_two = beacon_two.orientSlide(orientation[0], orientation[1], dpos)
                        if len(beacon_one.dist_pair_set & _beacon_two.dist_pair_set) >= 12:
                            canonical.append(sb2[0])
                            scanners[sb2[0]].orientSlide(orientation[0], orientation[1], dpos)
                            break
            iterations += 1
        return scanners

    def getDifference(self, beacon_one: list, beacon_two: list) -> tuple:
        return (beacon_one[0] - beacon_two[0], beacon_one[1] - beacon_two[1], beacon_one[2] - beacon_two[2])
    
    def orientation(self, coord: list, xyz: tuple, pos: tuple) -> tuple:
        return (coord[pos[0]]*xyz[0], coord[pos[1]]*xyz[1], coord[pos[2]]*xyz[2])

class Beacon:
    def __init__(self, position, dist_map=None):
        self.pos = position
        if not dist_map:
            self.dist_map = defaultdict(list)
        else:
            self.dist_map = dist_map
    
    def distanceBeacon(self, beacon):
        return ((self.pos[0] - beacon.pos[0])**2 + (self.pos[1] - beacon.pos[1])**2 + (self.pos[2] - beacon.pos[2])**2)

    def markBeacon(self, dist_pair, beacon_num):
        self.dist_map[beacon_num] = dist_pair
    
    def orientSlide(self, xyz, pos, dpos):
        x, y, z = Helpers().orientation(self.pos, xyz, pos)
        
        dx, dy, dz = dpos
        newPos = (x + dx, y + dy, z + dz)

        new_dist_map = {}
        for key, value in self.dist_map.items():
            dist, coord = value
            bx, by, bz = Helpers().orientation(coord, xyz, pos)
            new_dist_map[key] = (dist, (bx + dx, by + dy, bz + dz))
        
        return Beacon(
            position=newPos,
            dist_map=new_dist_map
        )
    
    @property
    def dist_set(self):
        return set(dist_coord_pair[0] for dist_coord_pair in self.dist_map.values())
    
    @property
    def dist_pair_set(self):
        return set(dist_coord_pair for dist_coord_pair in self.dist_map.values())

class Scanner:
    def __init__(self, scanner_id):
        self.pos = None
        self.sid = scanner_id
        self.beacons = []

    def add_beacon(self, beacon_coord):
        self.beacons.append(Beacon(position=beacon_coord))
    
    def finalize(self):
        for _, beacon in enumerate(self.beacons):
            for _number, _beacon in enumerate(self.beacons):
                distance = beacon.distanceBeacon(_beacon)
                beacon.markBeacon((distance, _beacon.pos), _number)
    
    def orientSlide(self, orientation, position):
        self.pos = position

        new_beacons = [beacon.orientSlide(orientation, position) for beacon in self.beacons]
        self.beacons = new_beacons
    
    def matchBeacon(self, other_scanner):
        potential_overlap = {}
        for number, beacon in enumerate(self.beacons):
            for _number, other_beacon in enumerate(other_scanner.beacons):
                if len(beacon.dist_set & other_beacon.dist_set) >= 12:
                    potential_overlap[(self.sid, number)] = (other_scanner.sid, _number)
        return potential_overlap

    def getBeacon(self, beacon_id):
        return self.beacons[beacon_id]

def partOne(data: str) -> int:
    scanners = Helpers().getData(data)
    canonical_coords = set()
    for scanner in scanners:
        canonical_coords |= {beacon.pos for beacon in scanner.beacons}
    return len(canonical_coords)

def partTwo(data: list) -> int:
    scanners = Helpers().getData(data)
    
    answer = 0
    for sid, scanner in enumerate(scanners):
        for scanner2 in scanners[sid:]:
            answer = max(answer, sum(map(abs, list(Helpers().getDifference(scanner.pos, scanner2.pos)))))
    return answer

def main() -> None:
    print(partOne(DATA))
    print(partTwo(DATA))

if __name__ == "__main__":
    main()

# Maybe this can be used to determine the location of the sensor.
# x = (sum(map(lambda i: i[pos[0]]*xyz[0], sensor_two)) + sum(map(lambda i: i[0], sensor_one))) / 12
# y = (sum(map(lambda i: i[pos[1]]*xyz[1], sensor_two)) + sum(map(lambda i: i[1], sensor_one))) / 12
# z = (sum(map(lambda i: i[pos[2]]*xyz[2], sensor_two)) + sum(map(lambda i: i[2], sensor_one))) / 12