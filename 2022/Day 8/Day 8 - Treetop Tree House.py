from Treetop_Tree_House import INPUT

def getData() -> list[list[int]]:
    return [list(map(int, [cell for cell in row])) for row in INPUT.splitlines() if len(row) != 0]

def partOne() -> int:
    grid: list[list[int]] = getData()
    trees: int = sum([len(grid[0]), len(grid[-1]), sum([2 for _ in grid[1:-1]])])
    print(trees)
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):
            tree: int = grid[row][col]
            left: list = max(grid[row][:col])
            right: list = max(grid[row][col+1:])
            up: list = max([grid[i][col] for i in range(0, row)])
            down: list = max([grid[i][col] for i in range(row+1, len(grid))])
            if tree > left or tree > right or tree > up or tree > down:
                trees += 1
    return trees

def treeCounter(left: list, right: list, up: list, down: list, current: int) -> int:
    counter: int = 1
    for direction in [left, right, up, down]:
        count: int = 0
        blocked: bool = False
        for d in direction:
            if (d < current) and not blocked:
                count += 1
            if d >= current and not blocked:
                count += 1
                blocked = True
        counter *= count
    return counter

def partTwo() -> int:
    grid: list[list[int]] = getData()
    scene: list = []
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):
            left: list = grid[row][:col][::-1]
            right: list = grid[row][col + 1:]
            up: list = [grid[i][col] for i in range(0, row)][::-1]
            down: list = [grid[i][col] for i in range(row + 1, len(grid))]
            scene.append(treeCounter(left, right, up, down, grid[row][col]))
    return max(scene)

def main():
    print(f'ANSWER PART ONE: {partOne()}')
    print(f'ANSWER PART TWO: {partTwo()}')

if __name__ == "__main__":
    main()
