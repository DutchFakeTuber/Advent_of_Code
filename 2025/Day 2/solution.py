from os.path import dirname, realpath
from collections import Counter

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[list[int]]:
    return [list(map(int, nums.split('-'))) for nums in data.split(',')]

def partOne(data: list[list[int]]) -> int:
    return sum([int(num) for start, end in data for num in map(str, range(start, end+1)) if num[:len(num)//2] == num[len(num)//2:]])

def partTwo(data: list[list[int]]) -> int:
    counter: int = 0
    for num in [n for start, end in data for n in map(str, range(start, end+1))]:
        for n in [Counter([num[i:i+n] for i in range(0, len(num), n)]) for n in range(1, len(num)//2+1)]:
            if len(n) == 1:
                counter += int(num)
                break
    return counter

if __name__ == "__main__":
    data: list[list[int]] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
