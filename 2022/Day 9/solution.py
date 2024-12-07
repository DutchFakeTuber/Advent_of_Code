TEST: str = open("test.txt")
DATA: str = open("input.txt")

def getData() -> list[str, int]:
    return [[str(line.split(' ')[0]), int(line.split(' ')[1])] for line in DATA.splitlines() if len(line) != 0]

class Head:
    MOVE: dict = dict(left=[-1, 0], right=[1, 0], up=[0, 1], down=[0, -1])
    def __init__(self) -> None:
        self.x: int = 0
        self.y: int = 0
    
    def move(self, direction: str, number: int) -> int:
        match direction:
            case 'L': move: list = self.MOVE['left']
            case 'R': move: list = self.MOVE['right']
            case 'U': move: list = self.MOVE['up']
            case 'D': move: list = self.MOVE['down']
        self.x += move[0]
        self.y += move[1]
        return number - 1

class Tail(Head):
    def __init__(self) -> None:
        super().__init__()
        self.positions: set = set()
    
    def move(self, *pos: tuple) -> None:
        dist_x = pos[0] - self.x
        dist_y = pos[1] - self.y
        if abs(dist_x) == 2 and not dist_y:  # Horizontal
            self.x += 1 if dist_x > 0 else -1
        elif abs(dist_y) == 2 and not dist_x:  # Vertical
            self.y += 1 if dist_y > 0 else -1
        elif (abs(dist_y) == 2 and abs(dist_x) in (1, 2)) \
                or (abs(dist_x) == 2 and abs(dist_y) in (1, 2)):
            self.x += 1 if dist_x > 0 else -1
            self.y += 1 if dist_y > 0 else -1
        self.positions.add(tuple([self.x, self.y]))

def parts(knots: int) -> int:
    instruction: list[list[str, int]] = getData()
    head: Head = Head()
    tails: list[Tail] = [Tail() for _ in range(knots)]
    for inst in instruction:
        moves: int = inst[1]
        while moves != 0:
            moves: int = head.move(inst[0], moves)
            tails[0].move(head.x, head.y)
            for t in range(1, len(tails)):
                tails[t].move(tails[t-1].x, tails[t-1].y)
    return len(tails[-1].positions)

def main() -> None:
    print(f'ANSWER PART ONE: {parts(1)}')
    print(f'ANSWER PART TWO: {parts(9)}')

if __name__ == "__main__":
    main()
