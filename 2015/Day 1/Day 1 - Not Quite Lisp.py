from Not_Quite_Lisp import DATA

def partOne(data: str):
    floor: int = 0
    for character in data:
        if character == '(':
            floor += 1
        else: floor -= 1
    return floor

def main() -> None:
    print(partOne(DATA))

if __name__ == "__main__":
    main()