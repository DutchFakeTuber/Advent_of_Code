from typing import Generator
import re

TEST: str = open("test.txt")
DATA: str = open("input.txt")

NUMBERS: dict = {
    char: str(num)
    for num, char in enumerate(
        'one,two,three,four,five,six,seven,eight,nine'.split(','),
        start=1)
}

def fetchData(data: str) -> list:
    return data.splitlines()

def partOne(data: list) -> int:
    return sum([int(f'{num[0]}{num[-1]}') for num in [re.findall(r'[0-9]', line) for line in data]])

def findChars(line: str) -> Generator:
    """Returns: Generator(pos, val)"""
    for key, val in NUMBERS.items():
        f, rf = line.find(key), line.rfind(key)
        if f != -1: yield (f, int(val))
        if rf != -1: yield (rf, int(val))
    for num in range(1, 10):
        f, rf = line.find(str(num)), line.rfind(str(num))
        if f != -1: yield (f, num)
        if rf != -1: yield (rf, num)

def partTwo(data: list) -> int:
    return sum(
        int(f'{nums[min(nums.keys())]}{nums[max(nums.keys())]}')
        for nums in [dict(set(findChars(d))) for d in data]
    )

if __name__ == "__main__":
    data: list = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
