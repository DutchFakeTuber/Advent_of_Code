from Syntax_Scoring import DATA
from sys import exit

class SyntaxScoring:
    POINTS: dict = {
        ')': [3, 1],
        ']': [57, 2],
        '}': [1197, 3],
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

    def compareString(self, line, partOne=True) -> int:
        for character in line:
            if character in self.open_close[0]:
                self._open.append(character)

            elif character in self.open_close[1]:
                if self.compareCharacters(self._open[-1], character):
                    self._open.pop(-1)
                    continue
                
                else:
                    if partOne: return [SyntaxScoring.POINTS[char][0] for char in SyntaxScoring.POINTS if char == character][0] 
                    else: return False, None
        
        if self._open.count != 0: # If the string is incomplete
            if partOne: return 0
            else:
                return True, line
        else: # String was correct
            if partOne: return 0
            else: False, None

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
            # Collect missing characters per line
            self.missing_chars.append(self._open)
        
        self.totalMissing = {}
        for number in range(len(self.missing_chars)):
            self.totalMissing[number] = 0
            while len(self.missing_chars[number]) != 0:
                self.totalMissing[number] = self.totalMissing[number] * 5
                character: str = self.missing_chars[number][0] # Get last character in list
                character: str = self.open_close[1][self.open_close[0].index(character)]
                self.totalMissing[number] += [SyntaxScoring.POINTS[char][1] for char in SyntaxScoring.POINTS if char == character][0]
                self.missing_chars[number].pop(0)

        self.totalMissingList: list = [value for value in self.totalMissing.values()]
        self.totalMissingList.sort()
        return self.totalMissingList[len(self.totalMissingList)//2+1]
        # [print(self.data.index(line)) for line in self.incomplete]
        # The middle score can be found by: [len(score)//2+1]

def main() -> None:
    print(SyntaxScoring().partOne())
    print(SyntaxScoring().partTwo())

if __name__ == "__main__":
    main()