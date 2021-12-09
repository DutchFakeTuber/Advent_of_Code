from Seven_Segment_Search import DATA

class SevenSegments:
    SEVEN_SEGMENTS: dict = {
        #  [A, B, C, D, E, F, G]
        0: [1, 1, 1, 0, 1, 1, 1],
        1: [0, 0, 1, 0, 0, 1, 0],
        2: [1, 0, 1, 1, 1, 0, 1],
        3: [1, 0, 1, 1, 0, 1, 1],
        4: [0, 1, 1, 1, 0, 1, 0],
        5: [1, 1, 0, 1, 0, 1, 1],
        6: [1, 1, 0, 1, 1, 1, 1],
        7: [1, 0, 1, 0, 0, 1, 0],
        8: [1, 1, 1, 1, 1, 1, 1],
        9: [1, 1, 1, 1, 0, 1, 1],
    }

    def __init__(self, data) -> None:
        self.data: list = self.getData(data)
        self.unique: dict = {
            number: [] for number in ['One', 'Four', 'Seven', 'Eight']
        }
        self.calculate: int = 0

    def getData(self, data: str) -> list:
        return [[[characters for characters in pipe.split()] for pipe in line.split(' | ')] for line in data.split('\n')]

    def partOne(self) -> int:
        [[self.unique['One'].append(sequence) for sequence in string[1] if len(sequence) == 2] for string in self.data]
        [[self.unique['Four'].append(sequence) for sequence in string[1] if len(sequence) == 4] for string in self.data]
        [[self.unique['Seven'].append(sequence) for sequence in string[1] if len(sequence) == 3] for string in self.data]
        [[self.unique['Eight'].append(sequence) for sequence in string[1] if len(sequence) == 7] for string in self.data]
        return sum([len(x) for x in self.unique.values()])

    def segmentLooper(self, chars: list, counter: int=0) -> None:
        self.sevenSegments: dict = {
            letter: None for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        }
        discovered: int = 0
        while discovered != 5:
            counter = counter + 1 if counter != 9 else 0

            # Get position C and F. It is not clear which position precisely
            if len(chars[counter]) == 2 and discovered == 0:    # Number 1
                self.sevenSegments['c'] = chars[counter]
                self.sevenSegments['f'] = chars[counter]
                discovered += 1
            
            # Secure position A.
            elif len(chars[counter]) == 3 and discovered == 1:  # Number 7
                self.sevenSegments.update({'a': letter for letter in chars[counter] if letter not in self.sevenSegments['c']})
                discovered += 1
            
            # Get position B and D. It is not clear which position precisely
            elif len(chars[counter]) == 4 and discovered == 2:  # Number 4
                segmentsBD = [letter for letter in chars[counter] if letter not in self.sevenSegments['c']]
                self.sevenSegments['b'] = ''.join(letter for letter in segmentsBD[0:2])
                self.sevenSegments['d'] = ''.join(letter for letter in segmentsBD[0:2])
                discovered += 1
            
            elif len(chars[counter]) == 5:  # Numbers 2, 3 & 5
                if discovered == 3:
                    # Only let numbers through that have segment C and F (Number 3)
                    if self.sevenSegments['c'][0] in chars[counter] and self.sevenSegments['c'][1] in chars[counter]:
                        # Secure position B
                        self.sevenSegments.update({'b': letter for letter in self.sevenSegments['d'] if letter not in chars[counter]})
                        # Secure position D
                        self.sevenSegments.update({'d': letter for letter in self.sevenSegments['d'] if letter not in self.sevenSegments['b']})
                        # Secure position G
                        self.sevenSegments.update({'g': letter for letter in chars[counter] if letter not in [self.sevenSegments[x][0] if x != 'f' else self.sevenSegments[x][1] for x in 'abcdf']})
                        discovered += 1
                
                elif discovered == 4:
                    # Only let numbers through that have segment B (Number 5)
                    if self.sevenSegments['b'] in chars[counter]:
                        # Secure position C
                        self.sevenSegments.update({'c': letter for letter in self.sevenSegments['f'] if letter not in chars[counter]})
                        # Secure position F
                        self.sevenSegments.update({'f': letter for letter in self.sevenSegments['f'] if letter not in self.sevenSegments['c']})
                        # Secure position E
                        self.sevenSegments.update({'e': letter for letter in 'abcdefg' if letter not in self.sevenSegments.values()})
                        discovered += 1

    def partTwo(self) -> int:
        for string in self.data:
            self.segmentLooper(string[0], counter=0)
            total: int = 0
            for number, sequence in enumerate(string[1]):
                value = [1 if chars in sequence else 0 for chars in self.sevenSegments.values()]
                total += 10**(abs(number-3)) * [key for key, segments in SevenSegments.SEVEN_SEGMENTS.items() if value == segments][0]
            self.calculate += total
        return self.calculate

def main() -> None:
    print(SevenSegments(DATA).partOne())
    print(SevenSegments(DATA).partTwo())

if __name__ == "__main__":
    main()