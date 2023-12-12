from Hot_Springs import TEST, TESTCASE, DATA
from functools import lru_cache
from time import perf_counter

def fetchData(data: str) -> list[list[str, tuple[int]]]:
    return [[line.split()[0], eval(f"[{line.split()[1]}]")] for line in data.splitlines()]

class HotSpring:
    def __init__(self, data: list[str, tuple[int]]) -> None:
        self.data = data
        self.count: int = 0
        self.arrangements: int = 0
        self.match: list = []

    lru_cache(maxsize=None)
    def pattern(self, patt: str, pos: int, prev: str) -> None:
        if pos == len(patt):
            if self.match == [len(chars) for chars in patt.split('.') if chars != '']:
                self.count += 1
            return
        if prev == '#' and patt[pos] == '.':
            if self.match[0] != [len(chars) for chars in patt.split('.') if chars != ''][0]:
                return
        if patt[pos] == '?':
            self.pattern(patt[:pos] + '.' + patt[pos+1:], pos+1, '.')
            self.pattern(patt[:pos] + '#' + patt[pos+1:], pos+1, '#')
        else:
            self.pattern(patt, pos+1, patt[pos])

    def process(self) -> int:
        for chars, match in self.data:
            self.count: int = 0
            self.match: list = match
            self.pattern(chars, 0, chars[0])
            self.arrangements += self.count

def partOne(data: list[list[list[str], list[int]]]) -> int:
    hotSpring: HotSpring = HotSpring(data)
    hotSpring.process()
    return hotSpring.arrangements

def partTwo(data: list[list[list[str], list[int]]]) -> int:
    ...

if __name__ == "__main__":
    data: list[list[list[str], list[int]]] = fetchData(DATA)
    start = perf_counter()
    print(partOne(data))
    print(perf_counter() - start)
    print(partTwo(data))
