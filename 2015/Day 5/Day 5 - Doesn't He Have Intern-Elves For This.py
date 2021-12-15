import operator
from Doesnt_He_Have_Intern_Elves_For_This import DATA

class PartOne:
    VOWELS: list = ['a', 'e', 'i', 'o', 'u']
    FORBIDDEN: list = ['ab', 'cd', 'pq', 'xy']

    def __init__(self, data: str=DATA):
        self.data: list = [line for line in data.splitlines() if len(line) != 0]
        self.nice: list = []
        
    def checkDouble(self, line: str) -> bool:
        for char_1, char_2 in zip(line[::], line[1::]):
            if char_1 == char_2: return True
        return False

    def checkNaughty(self, line: str) -> bool:
        for chars in map(operator.add, line[::], line[1::]):
            if chars in self.FORBIDDEN: return False
        return True

    def executor(self) -> int:
        for line in self.data:
            if not sum([1 if char in self.VOWELS else 0 for char in line]) >= 3: continue
            if not self.checkDouble(line): continue
            if not self.checkNaughty(line): continue
            self.nice.append(line)
        return len(self.nice)

class PartTwo:
    def __init__(self, data: str=DATA):
        self.data: list = [line for line in data.splitlines() if len(line) != 0]
        self.nice: list = []
    
    def checkDouble(self, line: str) -> bool:
        double: list = [chars for chars in map(operator.add, line[::], line[1::])]
        for _n, _chars in enumerate(double):
            for n, chars in enumerate(double):
                if _n == n:
                    continue
                if _chars == chars and abs(_n - n) != 1:
                    yield chars
    
    def checkLetters(self, line: str) -> bool:
        even: list = [letter for letter in line[::2]]
        odd: list = [letter for letter in line[1::2]]
        for _e, e in zip(even[::], even[1::]):
            if _e == e: return True
        for _o, o in zip(odd[::], odd[1::]):
            if _o == o: return True
        return False

    def executor(self) -> int:
        for line in self.data:
            if not sum([1 for _ in self.checkDouble(line)]) >= 2: continue
            if not self.checkLetters(line): continue
            self.nice.append(line)
        return len(self.nice)
        

def main() -> None:
    print(PartOne().executor())
    print(PartTwo().executor())

if __name__ == "__main__":
    main()