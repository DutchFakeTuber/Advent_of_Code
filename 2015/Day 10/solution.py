TEST: str = open("test.txt")
DATA: str = open("input.txt")

def getData(data: str) -> list[int]:
    return [int(number) for number in data]

def elveCount(sequence: list[int]) -> list[int]:
    count: list[list[int]] = [[sequence[0]]]
    for number in sequence[1:]:
        if number == count[-1][-1]:
            count[-1].append(number)
        else:
            count.append([number])
    
    newSequence: list[int] = []
    for numbers in count:
        newSequence += [len(numbers), numbers[0]]
    return newSequence

def parts(data: str, cycles: int) -> int:
    for _ in range(cycles):
        data: str = elveCount(data)
    return len(data)

if __name__ == "__main__":
    numbers: list[int] = getData(DATA)
    print(parts(numbers, 40))
    print(parts(numbers, 50))
