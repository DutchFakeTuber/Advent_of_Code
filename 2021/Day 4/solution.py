TEST: str = open("test.txt")
DATA: str = open("input.txt")

class Bingo:
    def markNumber(self, sheet: list, bingo_number: int) -> list:
        [[sheet[rows_number][position].__setitem__(1, True) for position, number in enumerate(rows) if number[0] == bingo_number] for rows_number, rows in enumerate(sheet)]
        return sheet

    def checkBingo(self, sheet: list, bingo_number: int) -> tuple:
        # Check horizontal bingo
        for rows in sheet:
            if rows[0][1] and rows[1][1] and rows[2][1] and rows[3][1] and rows[4][1]:
                return sheet, bingo_number, True

        # Check vertical Bingo
        for column in range(len(sheet)):
            if sheet[0][column][1] and sheet[1][column][1] and sheet[2][column][1] and sheet[3][column][1] and sheet[4][column][1]:
                return sheet, bingo_number, True
        return sheet, bingo_number, False

def getData(data: str) -> dict:
    rows: list = [row for row in data.split('\n') if len(row) != 0]
    boards: dict = {
        f'Board {board}': [[[int(number), False]
        for number in row.split()]            # For loop for each number in a row of the Bingo board
        for row in rows[5*board:(5*board)+5]] # For loop for 5 rows of the Bingo board data
        for board in range(len(rows)//5)      # For loop for all boards in the Bingo board data (5 rows per board)
    }
    return boards

def parts(data: dict, numbers: list, partOne: bool=True):
    if partOne: index: int = len(numbers)
    else: index: int = 0

    for sheet in data:
        stop: bool = False
        for number in numbers:
            if stop: continue
            else:
                marked_sheet = Bingo().markNumber(data[sheet], number)
                bingo_sheet, bingo_number, stop = Bingo().checkBingo(marked_sheet, number)
                
        if partOne:
            if numbers.index(bingo_number) < index:
                index = numbers.index(bingo_number)
                bingo = [bingo_sheet, bingo_number]
        else:
            if numbers.index(bingo_number) > index:
                index = numbers.index(bingo_number)
                bingo = [bingo_sheet, bingo_number]
    
    totalUnmarked: int = 0
    for line in bingo[0]:
        for column in line:
            if not column[1]:
                totalUnmarked += column[0]
    return totalUnmarked * bingo[1]

def main() -> None:
    print(parts(getData(BOARDS), NUMBERS, partOne=True))
    print(parts(getData(BOARDS), NUMBERS, partOne=False))

if __name__ == "__main__":
    main()