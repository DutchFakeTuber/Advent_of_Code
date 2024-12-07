TEST: str = open("test.txt")
DATA: str = open("input.txt")

def parts(length: int) -> int:
    return min([num+length for num in range(len(DATA)) if len(set(DATA[num:num+length])) == length])

def main() -> None:
    print(f"ANSWER PART ONE: {parts(4)}")
    print(f"ANSWER PART TWO: {parts(14)}")
    
if __name__ == "__main__":
    main()
    