from Dirac_Dice import DATA

class Game:
    def __init__(self, player_1, player_2) -> None:
        self.p1: int = player_1
        self.p2: int = player_2
        self.score: list = [0, 0]
        self.rolled: int = 0
        self.dice: int = 0
    
    def roll(self) -> int:
        self.rolled += 1
        self.dice += 1
        if self.dice > 100:
            self.dice = 1
        return self.dice
    
    def move(self, player: int, amount: int) -> None:
        amount = amount % 10
        if player == 1:
            self.p1 += amount
            if self.p1 > 10:
                self.p1 -= 10
            self.score[0] += self.p1
        else:
            self.p2 += amount
            if self.p2 > 10:
                self.p2 -= 10
            self.score[1] += self.p2
    
    def game(self, win=1000):
        turnPlayerOne: bool = True
        while True:
            amount = sum([self.roll(), self.roll(), self.roll()])
            self.move(1 if turnPlayerOne else 2, amount)
            turnPlayerOne = not turnPlayerOne
            if self.score[0] >= win or self.score[1] >= win:
                break

        loser = min(self.score)
        return loser * self.rolled
        

def getData(data: str) -> list:
    return [int(line[-1]) for line in data.splitlines() if len(line) != 0]

def partOne(data: list) -> int:
    G = Game(data[0], data[1])
    # G = Game(4, 8) # TEST
    return G.game(win=1000)

def partTwo(data: list) -> int:
    ...

def main() -> None:
    data = getData(DATA)
    print(partOne(data))
    print(partTwo(data))

if __name__ == "__main__":
    main()