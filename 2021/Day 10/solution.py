TEST: str = open("test.txt")
DATA: str = open("input.txt")

class SyntaxScoring:
    POINTS: dict = {
        ')':     [3, 1],
        ']':    [57, 2],
        '}':  [1197, 3],
        '>': [25137, 4],
    }

    def __init__(self, data: str=DATA) -> None:
        self.data: list = [line for line in data.splitlines()]
        self.open_close: list = [
            ['(', '[', '{', '<'],
            [')', ']', '}', '>']
        ]
        self.total: int = 0
        self._open: list = []
        self.incomplete: list = []
        self.missing_chars: list = []

    def compareCharacters(self, open: str, close: str) -> bool:
        return True if self.open_close[1][self.open_close[0].index(open)] == close else False

    def compareString(self, line: str, partOne: bool=True) -> int:
        for character in line:
            if character in self.open_close[0]:
                self._open.append(character)

            elif character in self.open_close[1]:
                if self.compareCharacters(self._open[-1], character):
                    self._open.pop(-1)
                
                else:
                    if partOne: return [SyntaxScoring.POINTS[char][0] for char in SyntaxScoring.POINTS if char == character][0] 
                    else: return False, None
        
        if self._open.count != 0: # If the string is incomplete
            if partOne: return 0
            else: return True, line
        else: # String was correct
            if partOne: return 0
            else: return False, None

    def partOne(self) -> int:
        for line in self.data:
            self._open: list = []
            self.total += self.compareString(line)
        return self.total

    def partTwo(self) -> int:
        for line in self.data:
            status, string = self.compareString(line, partOne=False)
            if status: self.incomplete.append(string)
        
        for line in self.incomplete:
            self._open: list = []
            for character in line:
                if character in self.open_close[0]: self._open.append(character)
                else: self._open.pop(-1)
            self.missing_chars.append(self._open)
        
        self.totalMissing: dict = {}
        for number in range(len(self.missing_chars)):
            self.totalMissing[number] = 0

            for character in reversed(self.missing_chars[number]):
                self.totalMissing[number] *= 5
                self.totalMissing[number] += [
                    SyntaxScoring.POINTS[char][1]
                    for char in SyntaxScoring.POINTS
                    if char == self.open_close[1][self.open_close[0].index(character)]
                ][0]

        self.totalMissingList: list = [value for value in self.totalMissing.values()]
        self.totalMissingList.sort()
        return self.totalMissingList[len(self.totalMissingList)//2]

def main() -> None:
    print(SyntaxScoring().partOne())
    print(SyntaxScoring().partTwo())

if __name__ == "__main__":
    main()