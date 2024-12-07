TEST: str = open("test.txt")
DATA: str = open("input.txt")

W, D, L = 6, 3, 0  # Win, Draw, Lose
R, P, S = 1, 2, 3  # Rock, Paper, Scissors

def readData() -> list[list]:
    return [
        [i for i in input.split(' ')]
        for input in DATA.splitlines() if len(input) != 0
    ]

def partOne() -> int:
    RPS: dict = {'A': {'X': D+R, 'Y': W+P, 'Z': L+S},
                 'B': {'X': L+R, 'Y': D+P, 'Z': W+S},
                 'C': {'X': W+R, 'Y': L+P, 'Z': D+S}}
    return sum([RPS[opponent][you] for opponent, you in readData()])

def partTwo() -> int:
    RPS: dict = {'A': {'X': L+S, 'Y': D+R, 'Z': W+P},
                 'B': {'X': L+R, 'Y': D+P, 'Z': W+S},
                 'C': {'X': L+P, 'Y': D+S, 'Z': W+R}}
    return sum([RPS[opponent][you] for opponent, you in readData()])
    

def main() -> None:
    print(f"ANSWER PART ONE: {partOne()}")
    print(f"ANSWER PART TWO: {partTwo()}")
    
if __name__ == "__main__":
    main()
