from os.path import dirname, realpath

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[int]:
    return [int(line) for line in data.splitlines() if len(line)]

def calculate(number: int, repeat: int = 1) -> int:
    for _ in range(repeat):
        number = (number ^ (number << 6)) & 0xFFFFFF
        number = number ^ (number >> 5)
        number = (number ^ (number << 11)) & 0xFFFFFF
    return number

def partOne(data: list[int]) -> int:
    return sum([calculate(number, repeat=2000) for number in data])

def partTwo(data: list[int]) -> int:
    pattern: dict = dict()
    for number in data:
        sequences: list[int] = [number] + [number:=calculate(number, repeat=1) for _ in range(2000)]
        changes: list[int] = [x%10-y%10 for x, y in zip(sequences, sequences[1:])]
        seen: set = set()
        for position in range(len(sequences)-4):
            consecutive: tuple[int] = tuple(changes[position:position+4])
            if consecutive not in seen:
                pattern.setdefault(consecutive, 0)
                pattern[consecutive] += sequences[position+4] % 10
                seen.add(consecutive)
    return max(pattern.values())

if __name__ == "__main__":
    data: list[int] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
