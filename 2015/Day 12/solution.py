from json import loads

TEST: str = open("test.txt")
DATA: str = open("input.txt")

def partOne(data: str) -> int:
    passableChars: list = ["-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    numList: list = []
    for pos, char in enumerate(data):
        if char in passableChars:
            if data[pos-1] in passableChars:
                numList[-1] = numList[-1] + char
            else:
                numList.append(char)
    numList = [int(num) for num in numList]
    return sum(numList)

def partTwo(data) -> int:
    if type(data) == int:
        return data
    if type(data) == list:
        return sum([partTwo(d) for d in data])
    if type(data) != dict:
        return 0
    if 'red' in data.values():
        return 0
    return partTwo(list(data.values()))
        

if __name__ == "__main__":
    print(partOne(DATA))
    print(partTwo(loads(DATA)))
