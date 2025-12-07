from os.path import dirname, realpath

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[str]:
    return data.splitlines()

def partOne(data: list[str]) -> int:
    counter: int = 0
    for line in data:
        for num in range(9, -1, -1):
            found: bool = False
            pos: int = line.find(str(num))
            if 0 <= pos < len(line):
                for n in range(9, -1, -1):
                    p: int = line[pos+1:].find(str(n))
                    if p >= 0:
                        counter += int(f'{num}{n}')
                        found = True
                        break
            if found:
                break
    return counter

def partTwo(data: list[str]) -> int:
    counter: int = 0
    for line in map(list, data):
        number: list = [int(line.pop(0))]
        while len(line):
            num: int = int(line.pop(0))
            if num <= number[-1]:
                if len(number) == 12: continue
                number.append(num)
            else:
                if len(line) + len(number) == 11:
                    number = number + [num] + line
                    break
                while True:
                    number.pop()
                    if len(number) == 0 or len(line) + len(number) == 11:
                        number.append(num)
                        break
                    if num > number[-1]: continue
                    number.append(num)
                    break
        counter += int(''.join(map(str, number)))
    return counter

if __name__ == "__main__":
    data: list[str] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
