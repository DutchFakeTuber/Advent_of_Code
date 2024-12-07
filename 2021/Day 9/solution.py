from typing import Generator
import math

TEST: str = open("test.txt")
DATA: str = open("input.txt")

class SmokeBasin:
    def __init__(self, data: str) -> None:
        self.data: list = [[int(number) for number in line] for line in data.split('\n')]
    
    def getCoords(self, row: int, column: int) -> Generator:
        for conv_row, conv_col in zip([row, row, row-1, row+1], [column-1, column+1, column, column]):
            try: yield self.data[conv_row][conv_col]
            except: yield None

    def partOne(self) -> int:
        lowPoints: list = []
        for row in range(len(self.data)):
            for column, number in enumerate(self.data[row]):
                left, right, up, down = self.getCoords(row, column)
                if (column == 0 or number < left) \
                        and (column == len(self.data[row])-1 or number < right) \
                        and (row == 0 or number < up) \
                        and (row == len(self.data)-1 or number < down):
                    lowPoints.append(number)

        return sum(lowPoints) + len(lowPoints)

    def check(self, row: int, column: int) -> int:
        count: int = 0
        if not (0 <= row < len(self.data) and 0 <= column < len(self.data[row])) \
                or self.data[row][column] == 9:
            return 0
        self.data[row][column] = 9
        count += 1

        for row_offset, column_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            count += self.check(row+row_offset, column+column_offset)
        return count

    def partTwo(self) -> int:
        return math.prod(
            sorted([
                self.check(row, column)
                for row in range(len(self.data))
                for column in range(len(self.data[row]))
            ])[-3:]
        )

def main() -> None:
    print(SmokeBasin(DATA).partOne())
    print(SmokeBasin(DATA).partTwo())

if __name__ == "__main__":
    main()