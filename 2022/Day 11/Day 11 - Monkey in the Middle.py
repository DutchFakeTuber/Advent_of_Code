from functools import reduce
from Monkey_in_the_Middle import INPUT

def getData() -> list[dict]:
    inp: list = [line for line in INPUT.splitlines() if len(line)]
    return [
        dict(
            holding=list(map(int, inp[i:i+6][1].strip(' ').split(':')[1].split(','))),
            operation=[str(inp[i:i+6][2].split(' ')[-2]), int(inp[i:i+6][2].split(' ')[-1]) if inp[i:i+6][2].split(' ')[-1].isnumeric() else inp[i:i+6][2].split(' ')[-1]],
            test=int(inp[i:i+6][3].split(' ')[-1]),
            true=int(inp[i:i+6][4].split(' ')[-1]),
            false=int(inp[i:i+6][5].split(' ')[-1]),
            inspected=0
        ) for i in range(0, len(inp), 6)
    ]

def operation(instruction: str, value: int | str, current: int):
    if isinstance(value, str):
        value = current
    match instruction:
        case '+': return current + value
        case '*': return current * value

def test(value: int, case: int, true: int, false: int) -> int:
    if value % case == 0:
        return true
    return false

def process(monkeys: list[dict], div: bool = False) -> list:
    monkeys: list[dict] = getData()
    red: reduce = reduce((lambda x, y: x * y), [m['test'] for m in monkeys])
    for _ in range(20 if div else 10_000):
        for num in range(len(monkeys)):
            while len(monkeys[num]['holding']) != 0:
                monkeys[num]['holding'][0] = operation(*monkeys[num]['operation'], monkeys[num]['holding'][0])
                if div: monkeys[num]['holding'][0] //= 3
                else: monkeys[num]['holding'][0] %= red
                monkeys[test(monkeys[num]['holding'][0], monkeys[num]['test'], monkeys[num]['true'], monkeys[num]['false'])]['holding'].append(monkeys[num]['holding'][0])
                monkeys[num]['holding'].pop(0)
                monkeys[num]['inspected'] += 1
    return monkeys
    

def partOne() -> int:
    monkeys: list[dict] = getData()
    result: list = sorted([m['inspected'] for m in process(monkeys, div=True)], reverse=True)[:2]
    return result[0] * result[1]
    
def partTwo() -> int:
    monkeys: list[dict] = getData()
    result: list = sorted([m['inspected'] for m in process(monkeys, div=False)], reverse=True)[:2]
    return result[0] * result[1]

def main() -> None:
    print(f'ANSWER PART ONE: {partOne()}')
    print(f'ANSWER PART TWO: {partTwo()}')

if __name__ == "__main__":
    main()
