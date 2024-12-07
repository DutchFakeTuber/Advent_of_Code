TEST: str = open("test.txt")
DATA: str = open("input.txt")

def partOne(data: str) -> int:
    floor: int = 0
    for character in data:
        if character == '(': floor += 1
        else: floor -= 1
        
    return floor

def partTwo(data: str) -> int:
    floor: int = 0
    for number, character in enumerate(data):
        if character == '(': floor += 1
        else: floor -= 1

        if floor == -1: return number + 1

def main() -> None:
    print(partOne(DATA))
    print(partTwo(DATA))

if __name__ == "__main__":
    main()