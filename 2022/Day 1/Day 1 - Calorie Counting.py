from Calorie_Counting import INPUT

def puzzle_one():
    elves: list = [0]
    for calories in INPUT.splitlines():
        if calories:
            elves[-1] += int(calories)
        else:
            elves += [0]
    return elves
    
def puzzle_two():
    elves: list = puzzle_one()
    top_three: int = 0
    for _ in range(3):
        top_three += max(elves)
        elves.pop(elves.index(max(elves)))
    return top_three
    
def main():
    print(max(puzzle_one()))
    print(puzzle_two())

if __name__ == "__main__":
    main()
