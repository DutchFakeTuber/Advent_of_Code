from Dumbo_Octopus import DATA

def getData(data: str) -> list:
    return [[int(number) for number in line] for line in data.splitlines() if len(line) != 0]

def flash(data: list, row: int, col: int, flashed: int) -> tuple:
    flashed += 1
    data[row][col] = -1

    for offset_row in [-1, 0, 1]:
        for offset_col in [-1, 0, 1]:
            o_r: int = row + offset_row
            o_c: int = col + offset_col

            if 0 <= o_r < len(data) and 0 <= o_c < len(data[row]) and data[o_r][o_c] != -1:
                data[o_r][o_c] += 1

                if data[o_r][o_c] >= 10:
                    data, flashed = flash(data, o_r, o_c, flashed)

    return data, flashed

def partOne(data: list) -> int:
    flashed: int = 0
    for _ in range(0, 100):
        for n_row, row in enumerate(data):
            for n_col in range(len(row)):
                data[n_row][n_col] += 1
    
        for n_row, row in enumerate(data):
            for n_col, col in enumerate(row):
                if col >= 10:
                    data, flashed = flash(data, n_row, n_col, flashed)

        for n_row, row in enumerate(data):
            for n_col, col in enumerate(row):
                if col == -1:
                    data[n_row][n_col] = 0
    return flashed

def partTwo(data: list) -> int:
    counter: int = 0
    while True:
        counter += 1
        flashed: int = 0
        for n_row, row in enumerate(data):
            for n_col in range(len(row)):
                data[n_row][n_col] += 1
        
        for n_row, row in enumerate(data):
            for n_col, col in enumerate(row):
                if col >= 10:
                    data, flashed = flash(data, n_row, n_col, flashed)
        
        if flashed == 100:
            break

        for n_row, row in enumerate(data):
            for n_col, col in enumerate(row):
                if col == -1:
                    data[n_row][n_col] = 0

    return counter

def main() -> None:
    print(partOne(getData(DATA)))
    print(partTwo(getData(DATA)))


if __name__ == "__main__":
    main()