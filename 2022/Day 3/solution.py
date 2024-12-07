TEST: str = open("test.txt")
DATA: str = open("input.txt")

POINTS: str = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
LINE: list = [l for l in DATA.splitlines() if len(l) != 0]

def partOne() -> int:
    return sum([POINTS.index([x for x in comp1 if x in comp2][0]) for comp1, comp2 in [[l[:len(l)//2], l[len(l)//2:]] for l in LINE]])

def partTwo() -> int:
    groups: list[list] = [LINE[num:num+3] for num in range(0, len(LINE)+1, 3) if len(LINE[num:num+3]) != 0]
    count: int = 0
    for g1, g2, g3 in groups:
        found: bool = False
        for char in g1:
            if char in g2 and char in g3 and not found:
                count += POINTS.index(char)
                found = True
    return count

def main() -> None:
    print(f"ANSWER PART ONE: {partOne()}")
    print(f"ANSWER PART TWO: {partTwo()}")

if __name__ == "__main__":
    main()
