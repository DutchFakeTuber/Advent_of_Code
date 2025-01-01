from os.path import dirname, abspath
from itertools import product

TEST: str = open(f'{dirname(abspath(__file__))}\\test.txt').read()
DATA: str = open(f'{dirname(abspath(__file__))}\\input.txt').read()

SHOP: dict = {
    'weapon': [[8, 4], [10, 5], [25, 6], [40, 7], [74, 8]],
    'armor': [[0, 0], [13, 1], [31, 2], [53, 3], [75, 4], [102, 5]],
    'rings': [[0, 0, 0], [25, 1, 0], [50, 2, 0], [100, 3, 0], [0, 0, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]
}

class RPG:
    def __init__(self, hp: int=100) -> None:
        self.hp: int = hp
        self.attack: int = 0
        self.defense: int = 0
        self.gold: int = 0
    
    def weapon(self, cost: int, damage: int) -> object:
        self.gold += cost
        self.attack += damage
        return self
    
    def armor(self, cost: int, defense: int) -> object:
        self.gold += cost
        self.defense += defense
        return self
    
    def rings(self, cost: int, damage: int, defense: int) -> None:
        self.gold += cost
        self.attack += damage
        self.defense += defense
        return self
    
    def fight(self, bossHP: int, bossDMG: int, bossDEF: int) -> bool:
        while True:
            bossHP -= self.attack - bossDEF
            if bossHP <= 0:
                return True
            self.hp -= bossDMG - self.defense
            if self.hp <= 0:
                return False

def fetchData(data: str) -> list[int]:
    return list(map(int, [line.split(': ')[1] for line in data.splitlines() if len(line)]))

def parts(data: list[int]) -> tuple[int, int]:
    wins: list[int] = []
    lost: list[int] = []
    for weapon, armor in product(SHOP['weapon'], SHOP['armor']):
        for pos, ring1 in enumerate(SHOP['rings']):
            for ring2 in SHOP['rings'][:pos] + SHOP['rings'][pos+1:]:
                rpg: RPG = RPG()
                rpg.weapon(*weapon).armor(*armor).rings(*ring1).rings(*ring2)
                if rpg.fight(*data):
                    wins.append(rpg.gold)
                else:
                    lost.append(rpg.gold)
    return min(wins), max(lost)

if __name__ == "__main__":
    data: list[int] = fetchData(DATA)
    print(parts(data)[0])
    print(parts(data)[1])
    