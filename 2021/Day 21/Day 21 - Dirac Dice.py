from functools import cache
from itertools import product
from Dirac_Dice import DATA

class Game:
    def __init__(self, data: str) -> None:
        self.data: list = [int(line[-1]) for line in data.splitlines() if len(line) != 0]
        self.players: tuple = [self.data[0], self.data[1]]
        self.score: list = [0, 0]
        self.rolled: int = 0
        self.dice: int = 0
    
    def roll(self) -> int:
        self.rolled += 1
        self.dice = self.dice + 1 if self.dice != 100 else 1
        return self.dice
    
    def move(self, player: int, amount: int) -> None:
        self.players[player] += amount % 10
        if self.players[player] > 10: self.players[player] -= 10
        self.score[player] += self.players[player]

    def game(self, win=1000) -> int:
        turnPlayerOne: bool = True
        while True:
            self.move(0 if turnPlayerOne else 1, sum([self.roll() for _ in range(0, 3)]))
            turnPlayerOne = not turnPlayerOne
            if self.score[0] >= win or self.score[1] >= win:
                return min(self.score) * self.rolled
    
    @cache
    def quantumGame(self, position: tuple, score: tuple) -> tuple:
        wins = [0, 0]
        for rolls in product((1, 2, 3), repeat=3):
            _position = (position[0] - 1 + sum(rolls)) % 10 + 1
            _score = score[0] + _position
            if _score >= 21:
                wins[0] += 1
            else:
                _wins = self.quantumGame(tuple([position[1], _position]), tuple([score[1], _score]))
                wins[0] += _wins[1]
                wins[1] += _wins[0]
        return wins[0], wins[1]

def partOne(data: str) -> int:
    return Game(data).game()

def partTwo(data: str) -> int:
    game = Game(data)
    return max(game.quantumGame(tuple(game.players), tuple([0, 0])))

def main() -> None:
    print(partOne(DATA))
    print(partTwo(DATA))

if __name__ == "__main__":
    main()