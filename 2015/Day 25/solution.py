from os.path import dirname, abspath
from re import findall

TEST: str = open(f'{dirname(abspath(__file__))}\\test.txt').read()
DATA: str = open(f'{dirname(abspath(__file__))}\\input.txt').read()

def fetchData(data: str) -> list[int]:
    return list(map(int, findall(r'\d+', data)))

def partOne(data: list[int], start: int=20151125) -> int:
    row, col = data
    triangularNumber: int = (row + col - 2) * (row + col -1) // 2 + col - 1
    return (pow(252533, triangularNumber, 33554393) * start) % 33554393

if __name__ == "__main__":
    data: list[int] = fetchData(DATA)
    print(partOne(data))
