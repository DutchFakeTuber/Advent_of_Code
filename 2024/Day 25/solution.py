from os.path import dirname, abspath

TEST: str = open(f'{dirname(abspath(__file__))}\\test.txt').read()
DATA: str = open(f'{dirname(abspath(__file__))}\\input.txt').read()

def fetchData(data: str) -> list[list[str]]:
    return [lines.splitlines() for lines in data.split('\n\n')]

class Key:
    def __init__(self, layout: list[str]) -> None:
        self.coords: set = {(layout[row][col], row, col) for col in range(len(layout[0])) for row in range(len(layout))}
    
class Lock:
    def __init__(self, layout: list[str]) -> None:
        self.coords: set = {(layout[row][col], row, col) for col in range(len(layout[0])) for row in range(len(layout))}

    def __eq__(self, other: Key) -> bool:
        return all(map(lambda x: x[0] == '.', self.coords.intersection(other.coords)))

def partOne(data: list[list[str]]) -> int:
    keys: list[Key] = [Key(layout) for layout in data if layout[0].find('#') < 0]
    locks: list[Lock] = [Lock(layout) for layout in data if layout[0].find('#') == 0]
    return sum(key == lock for key in keys for lock in locks)

if __name__ == "__main__":
    data: list[list[str]] = fetchData(DATA)
    print(partOne(data))
