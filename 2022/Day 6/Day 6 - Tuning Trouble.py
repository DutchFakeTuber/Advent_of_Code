from Tuning_Trouble import INPUT

def parts(length: int) -> int:
    return min([num+length for num in range(len(INPUT)) if len(set(INPUT[num:num+length])) == length])

def main() -> None:
    print(f"ANSWER PART ONE: {parts(4)}")
    print(f"ANSWER PART TWO: {parts(14)}")
    
if __name__ == "__main__":
    main()
    