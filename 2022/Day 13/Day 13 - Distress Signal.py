from functools import cmp_to_key
from Distress_Signal import INPUT

def getData() -> list[list]:
    return [eval(line) for line in INPUT.splitlines() if len(line) != 0]

def compare(a: list | int, b: list | int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    if isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    if isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    for _a, _b in zip(a, b):
        comp = compare(_a, _b)
        if comp != 0:
            return comp
    return len(a) - len(b)

def partOne() -> int:
    signals: list[list] = getData()
    return sum(signal//2+1 for signal in range(0, len(signals), 2) if compare(*signals[signal:signal+2]) < 0)

def partTwo() -> int:
    signals: list[list] = getData()
    signals += [[[2]], [[6]]]
    signals.sort(key=cmp_to_key(compare))
    a, b = (num+1 for num, val in enumerate(signals) if val in ([[2]], [[6]]))
    return a * b

def main() -> None:
    print(f'ANSWER PART ONE: {partOne()}')
    print(f'ANSWER PART TWO: {partTwo()}')

if __name__ == "__main__":
    main()
