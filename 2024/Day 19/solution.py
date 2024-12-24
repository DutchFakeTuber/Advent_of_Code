from os.path import dirname, realpath
from functools import cache

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> tuple[tuple[str], list[str]]:
    return tuple(data.split('\n\n')[0].split(', ')), [line for line in data.split('\n\n')[1].splitlines() if len(line)]

@cache
def designCheck(towels: tuple[str], design: str) -> bool:
    return 1 if not design else sum(designCheck(towels, design[len(towel):]) for towel in towels if design.startswith(towel))

def partOne(towels: tuple[str], designs: list[str]) -> int:
    return sum(map(bool, [designCheck(towels, d) for d in designs]))

def partTwo(towels: tuple[str], designs: list[str]) -> int:
    return sum([designCheck(towels, d) for d in designs])

if __name__ == "__main__":
    towels, designs = fetchData(DATA)
    print(partOne(towels, designs))
    print(partTwo(towels, designs))
