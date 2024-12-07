TEST: str = open("test.txt")
DATA: str = open("input.txt")

def partOne(data: str) -> int:
    house: dict = {'0,0': 1}
    direction: dict = {
        '^': [1, 0],
        'v': [-1, 0],
        '>': [0, 1],
        '<': [0, -1]
    }
    xAxis, yAxis = 0, 0
    for dir in data:
        yAxis += direction[dir][0]
        xAxis += direction[dir][1]
        
        house[f'{xAxis},{yAxis}'] = house[f'{xAxis},{yAxis}'] + 1 if f'{xAxis},{yAxis}' in house.keys() else 0
    return len(house.keys())

def partTwo(data: str) -> int:
    house: dict = {'0,0': 1}
    dirs: dict = {
        '^': [1, 0],
        'v': [-1, 0],
        '>': [0, 1],
        '<': [0, -1]
    }
    xSanta, ySanta, xRobot, yRobot = 0, 0, 0, 0
    for dirSanta, dirRobot in zip(data[0::2], data[1::2]):
        ySanta, xSanta = ySanta + dirs[dirSanta][0], xSanta + dirs[dirSanta][1]
        yRobot, xRobot = xRobot + dirs[dirRobot][0], yRobot + dirs[dirRobot][1]

        house[f'{xSanta},{ySanta}'] = house[f'{xSanta},{ySanta}'] + 1 if f'{xSanta},{ySanta}' in house.keys() else 0
        house[f'{xRobot},{yRobot}'] = house[f'{xRobot},{yRobot}'] + 1 if f'{xRobot},{yRobot}' in house.keys() else 0
    return len(house.keys())

def main() -> None:
    print(partOne(DATA))
    print(partTwo(DATA))

if __name__ == "__main__":
    main()