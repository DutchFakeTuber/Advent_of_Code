import Sonar_Sweep as SS

def readData(data: str) -> list:
    return [int(number) for number in data.split("\n")]

def partOne(data: list) -> int:
    # return len([number for number in range(1, len(data)) if data[number] > data[number-1]])
    count: int = 0
    for number in range(1, len(data)):
        if data[number] > data[number - 1]:
            count += 1
    return count

def partTwo(data: list) -> int:
    # return len([number for number in range(1, len(data) - 2) if sum(data[number:number+3]) > sum(data[number-1:number+2])])
    count = 0
    for number in range(1, len(data) - 2):
        if sum(data[number:number+3]) > sum(data[number-1:number+2]):
            count += 1
    return count

def main() -> None:
    data = readData(SS.DATA)
    print(partOne(data))
    print(partTwo(data))

if __name__ == "__main__":
    main()