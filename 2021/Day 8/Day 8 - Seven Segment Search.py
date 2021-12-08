from Seven_Segment_Search import DATA

def getData(data: str) -> dict:
    return [[[characters for characters in pipe.split()] for pipe in line.split(' | ')] for line in data.split('\n')]
    """
    print(characters) # Total list
    print(characters[0]) # Per line
    print(characters[0][0]) # Before or after pipe
    print(characters[0][0][0]) # Each string separately
    """

def partOne(data: list) -> int:
    one, four, seven, eight = [], [], [], []
    [[one.append(sequence) for sequence in string[1] if len(sequence) == 2] for string in data]
    [[four.append(sequence) for sequence in string[1] if len(sequence) == 4] for string in data]
    [[seven.append(sequence) for sequence in string[1] if len(sequence) == 3] for string in data]
    [[eight.append(sequence) for sequence in string[1] if len(sequence) == 7] for string in data]
    return len(one) + len(four) + len(seven) + len(eight)

def partTwo(data: list) -> int:
    ...

def main() -> None:
    data = getData(DATA)
    print(partOne(data))

if __name__ == "__main__":
    main()