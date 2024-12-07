import re
from dataclasses import dataclass, field

TEST: str = open("test.txt")
DATA: str = open("input.txt")

@dataclass
class Sue:
    number: int = field(init=True)
    children: int = field(init=True, default=0)
    cats: int = field(init=True, default=0)
    samoyeds: int = field(init=True, default=0)
    pomeranians: int = field(init=True, default=0)
    akitas: int = field(init=True, default=0)
    vizslas: int = field(init=True, default=0)
    goldfish: int = field(init=True, default=0)
    trees: int = field(init=True, default=0)
    cars: int = field(init=True, default=0)
    perfumes: int = field(init=True, default=0)

    def compare(self, ticker: dict) -> bool:
        for key, val in ticker.items():
            if getattr(self, key) == val:
                continue
            if getattr(self, key) == 0 and val != 0:
                continue
            return False
        return True
    
    def indicate(self, special: dict) -> bool:
        state: bool = True
        for key, val in special.items():
            match key:
                case 'cats' | 'trees':
                    if getattr(self, key) != 0:
                        state = getattr(self, key) > val
                case 'pomeranians' | 'goldfish':
                    if getattr(self, key) != 0:
                        state = getattr(self, key) < val
            if not state:
                return False
        return True

def fetchData(data: str) -> dict:
    return {int(match.group(1)): {k: int(v) for k, v in re.findall(r"(\w+): (\d+)", match.group(2))} for match in re.finditer(r"Sue (\d+): (.+)", data.strip())}

def partOne(data: dict) -> int:
    ticker: dict = dict(children=3, cats=7, samoyeds=2, pomeranians=3, akitas=0, vizslas=0, goldfish=5, trees=3, cars=2, perfumes=1)
    return [sue.number for sue in [Sue(sue, **characteristics) for sue, characteristics in data.items()] if sue.compare(ticker)][0]
    
def partTwo(data: dict) -> int:
    ticker: dict = dict(children=3, samoyeds=2, akitas=0, vizslas=0, cars=2, perfumes=1)
    special: dict = dict(cats=7, pomeranians=3, goldfish=5, trees=3)
    return [sue.number for sue in [Sue(sue, **characteristics) for sue, characteristics in data.items()] if sue.indicate(special) and sue.compare(ticker)][1]

if __name__ == "__main__":
    data: dict = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
