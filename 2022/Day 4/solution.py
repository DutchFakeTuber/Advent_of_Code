TEST: str = open("test.txt")
DATA: str = open("input.txt")

def getData() -> list[list]:
    return [[list(map(int, p.split('-'))) for p in pair.split(',')] for pair in DATA.splitlines() if len(pair) != 0]
    
def partOne() -> int:
    return sum([1 for p1, p2 in getData() if (p1[0] >= p2[0] and p1[1] <= p2[1]) or (p1[0] <= p2[0] and p1[1] >= p2[1])])

def partTwo() -> int:
    return sum([1 for p1, p2 in getData() if p1[0] <= p2[0] <= p1[1] or p1[0] <= p2[1] <= p1[1] or p2[0] <= p1[0] <= p2[1] or p2[0] <= p1[1] <= p2[1]])

def main() -> None:
    print(f"ANSWER PART ONE: {partOne()}")
    print(f"ANSWER PART TWO: {partTwo()}")

if __name__ == "__main__":
    main()
