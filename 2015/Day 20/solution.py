from os.path import dirname, realpath
import math

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def getDivisors(house: int, cutoff: bool=False) -> list[int]:
    small: list[int] = [num for num in range(1, int(math.sqrt(house)) + 1) if house % num == 0]
    large: list[int] = [house/num for num in small if house != num**2]
    if not cutoff:
        return sum(small) + sum(large)
    return sum(s for s in small if house / s <= 50) + sum(l for l in large if house / l <= 50)

def partOne(presents: int) -> int:
    house: int = 0
    while True:
        house += 1
        divisors: int = getDivisors(house)
        if divisors * 10 >= presents:
            return house

def partTwo(presents: int) -> int:
    house: int = 0
    while True:
        house += 1
        divisors: int = getDivisors(house, cutoff=True)
        if divisors * 11 >= presents:
            return house

if __name__ == "__main__":
    print(partOne(33_100_000))
    print(partTwo(33_100_000))
