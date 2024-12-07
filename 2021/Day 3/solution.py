TEST: str = open("test.txt")
DATA: str = open("input.txt")

def getData(data: str) -> list:
    return [line for line in data.split("\n")]

def partOne(data: list) -> int:
    diagnostic: dict = {
        'zeros': 0,
        'ones': 0,
        'gamma total': 0,
        'epsilon total': 0,
    }

    for number in range(0, len(data[0])):
        for line in data:
            if int(line[number]) == 0:
                diagnostic['zeros'] += 1
            else: diagnostic['ones'] += 1

        if diagnostic['zeros'] > diagnostic['ones']:
            diagnostic['gamma total'] += 0 * 2**(len(data[0]) - (number + 1))
            diagnostic['epsilon total'] += 1 * 2**(len(data[0]) - (number + 1))
        else:
            diagnostic['gamma total'] += 1 * 2**(len(data[0]) - (number + 1))
            diagnostic['epsilon total'] += 0 * 2**(len(data[0]) - (number + 1))
        
        diagnostic['zeros'], diagnostic['ones'] = 0, 0
    
    return diagnostic['epsilon total'] * diagnostic['gamma total']

def countOneZero(data: list, position: int) -> tuple:
    zero = [line for line in data if line[position] == '0']
    one = [line for line in data if line[position] == '1']
    if len(zero) == 0 or len(one) == 0:
        if len(zero) == 0: return one, one
        else: return zero, zero
    if len(zero) > len(one):
        return zero, one
    else:
        return one, zero

def partTwo(data: list) -> int:
    generator: list = []
    scrubber: list = []
    prevGenerator, prevScrubber = countOneZero(data, 0)
    # First calculate generator
    for x in range(1, len(data[0])):
        generator, _ = countOneZero(prevGenerator, x)
        prevGenerator = generator
    # Then calculate scrubber
    for x in range(1, len(data[0])):
        _, scrubber = countOneZero(prevScrubber, x)
        prevScrubber = scrubber
    # Convert binary to decimal
    deciGenerator, deciScrubber = 0, 0
    for number in range(0, len(data[0])):
        deciGenerator += int(generator[0][number]) * 2**(len(data[0]) - (number + 1))
        deciScrubber += int(scrubber[0][number]) * 2**(len(data[0]) - (number + 1))
    return deciGenerator * deciScrubber

def main() -> None:
    data = getData(DATA)
    print(partOne(data))
    print(partTwo(data))

if __name__ == "__main__":
    main()