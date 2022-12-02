from Calorie_Counting import INPUT

def partOne() -> list:
    elves: list = [0]
    for calories in INPUT.splitlines():
        if calories:
            elves[-1] += int(calories)
        else:
            elves += [0]
    return elves
    
def partTwo() -> int:
    elves: list = partOne()
    top_three: int = 0
    for _ in range(3):
        top_three += max(elves)
        elves.pop(elves.index(max(elves)))
    return top_three
    
def main() -> None:
    print(f"ANSWER PART ONE: {max(partOne())}")
    print(f"ANSWER PART TWO: {partTwo()}")

if __name__ == "__main__":
    main()
