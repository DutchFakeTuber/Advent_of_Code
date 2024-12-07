import re

TEST: str = open("test.txt")
DATA: str = open("input.txt")

def fetchData(data: str) -> dict[list[int]]:
    return {
        int(re.sub(r"(Card|\s)+", "", line.split(': ')[0])): [
            list(map(int, re.sub(r"(\s)+", ",", line.split(': ')[1].split(' | ')[num].strip()).split(','))) for num in [0, 1]
        ] for line in data.splitlines()
    }

def partOne(data: dict[list[int]]) -> int:
    count: function = lambda p: sum([1 if n in p[1] else 0 for n in p[0]])
    return sum([2**(count(card)-1) for card in data.values() if count(card) >= 1])

def partTwo(data: dict[list[int]]) -> int:
    data: dict[int, list[int]] = {key: [1, *val] for key, val in data.items()}
    number: int = 1
    while number <= len(data.values()):
        hits: int = sum([1 if num in data[number][2] else 0 for num in data[number][1]])
        for hit in range(1, hits+1):
            data[number+hit][0] += 1 + (data[number][0]-1)
        number += 1
    return sum([cards[0] for cards in data.values()])

if __name__ == "__main__":
    data: dict[list] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
