from Binary_Diagnostic import DATA

def getData(data: str) -> list:
    return [line for line in data.split("\n")]

def partOne(data: list) -> int:
    diagnostic: dict = {
        'zeroes': 0,
        'ones': 0,
        'gamma total': 0,
        'epsilon total': 0,
    }

    for number in range(0, len(data[0])):
        for line in data:
            if int(line[number]) == 0:
                diagnostic['zeroes'] += 1
            else: diagnostic['ones'] += 1

        if diagnostic['zeroes'] > diagnostic['ones']:
            diagnostic['gamma total'] += 0 * 2**(len(data[0]) - (number + 1))
            diagnostic['epsilon total'] += 1 * 2**(len(data[0]) - (number + 1))
        else:
            diagnostic['gamma total'] += 1 * 2**(len(data[0]) - (number + 1))
            diagnostic['epsilon total'] += 0 * 2**(len(data[0]) - (number + 1))
        
        diagnostic['zeroes'], diagnostic['ones'] = 0, 0
    
    return diagnostic['epsilon total'] * diagnostic['gamma total']

def countOneZero(data: list, position) -> tuple:
    diagnostic: dict = {
        'zeroes': [],
        'ones': [],
        'generator': [],
        'scrubber': [],
    }
    if len(data) == 1:
        return data, data
    [diagnostic['zeroes'].append(line) if int(line[position]) == 0 else diagnostic['ones'].append(line) for line in data]
    if diagnostic['zeroes'] > diagnostic['ones']:
        for x in data:
            if int(x[position]) == 0:
                diagnostic['generator'].append(x)
            else: diagnostic['scrubber'].append(x)
    else:
        for x in data:
            if int(x[position]) == 1:
                diagnostic['generator'].append(x)
            else: diagnostic['scrubber'].append(x)
    return diagnostic['generator'], diagnostic['scrubber']

# def removeValues(data: list, high=True):
#     diagnostic: dict = {
#         'current': [],
#         'previous': [],
#         'zeroes': 0,
#         'ones': 0,
#     }
#     for number in range(1, len(data[0])):
#         [diagnostic['zeroes'] + 1 if int(line[number]) == 0 else diagnostic['ones'] + 1 for line in data]
#         # print(diagnostic['zeroes'], diagnostic['ones'])
#         for line in data:...


def partTwo(data: list) -> int:
    generator: list = []
    scrubber: list = []
    prevGenerator, prevScrubber = countOneZero(data, 0)
    # First calculate generator
    for x in range(1, len(data[0])):
        generator, _ = countOneZero(prevGenerator, x)
        prevGenerator = generator
    for x in range(1, len(data[0])):
        _, scrubber = countOneZero(prevScrubber, x)
        prevScrubber = scrubber
        print(prevScrubber)
    print(prevGenerator, prevScrubber)

def main() -> None:
    data = getData(DATA)
    print(partOne(data))
    print(partTwo(data))

if __name__ == "__main__":
    main()