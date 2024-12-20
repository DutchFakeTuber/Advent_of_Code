TEST: str = open("test.txt")
DATA: str = open("input.txt")

def getData(data: str) -> tuple[dict, list]:
    crates: dict = {int(data.splitlines()[9][n]): [letter[n] for letter in data.splitlines()[1:9] if letter[n] != ' '][::-1] for n in range(1, 34, 4)}
    operations: list = [list(map(int, op.split(' ')[1::2])) for op in data.splitlines()[11:]]
    return crates, operations

def partOne() -> str:
    crates, operations = getData()
    for num, f, t in operations:
        crates[t] += list(reversed(crates[f][-num:]))
        crates[f] = crates[f][:-num]
    return "".join([line[-1] for line in crates.values()])

def partTwo() -> int:
    crates, operations = getData()
    for num, f, t in operations:
        crates[t] += crates[f][-num:]
        crates[f] = crates[f][:-num]
    return "".join([line[-1] for line in crates.values()])

def main() -> None:
    print(f"ANSWER PART ONE: {partOne()}")
    print(f"ANSWER PART TWO: {partTwo()}")

if __name__ == "__main__":
    main()
