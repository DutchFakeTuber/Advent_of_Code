TEST: str = open("test.txt")
DATA: str = open("input.txt")

def getData() -> list[str]:
    return [line for line in DATA.splitlines() if len(line) != 0]

def convert(value) -> str:
    if value:
        dividend, divisor = divmod(value+2, 5)
        return convert(dividend) + "=-012"[divisor]
    else:
        return ''

def partOne() -> int:
    decipher: function = lambda val: sum(pow(5, n) * {'=': -2, '-': -1, '0': 0, '1': 1, '2' :2}[v] for n, v in enumerate(val[::-1]))
    return convert(sum(decipher(instr) for instr in getData()))

def main() -> None:
    print(f'ANSWER PART ONE: {partOne()}')
    print("CONGRATS, ALL STARS COLLECTED!")

if __name__ == "__main__":
    main()
