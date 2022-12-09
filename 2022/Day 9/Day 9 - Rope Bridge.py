from Rope_Bridge import INPUT

def getData() -> list[str, int]:
    return [[str(line.split(' ')[0]), int(line.split(' ')[1])] for line in INPUT.splitlines() if len(line) != 0]

class Rope:
    SAFE: dict = {1: [-1, 0, 1], 0: [-1, 0, 1], -1: [-1, 0, 1]}
    MOVE: dict = dict(left=[-1, 0], right=[1, 0], up=[0, 1], down=[0, -1])
    def __init__(self, head: list=[0, 0], tail: list=[0, 0]) -> None:
        self.head: list = head  # [X, Y]
        self.tail: list = tail  # [X, Y]
        self.path: dict = {f'{self.tail[0]}, {self.tail[1]}': 1}  # "Coord X, Coord Y": # Passes

    def checkPath(self) -> None:
        if f'{self.tail[0]}, {self.tail[1]}' in self.path.keys():
            self.path[f'{self.tail[0]}, {self.tail[1]}'] += 1
        else:
            self.path[f'{self.tail[0]}, {self.tail[1]}'] = 1
    
    def checkRange(self) -> bool:
        """ Check if the tail is in range of the head. """
        if self.head[1] - self.tail[1] in self.SAFE.keys():
            if self.head[0] - self.tail[0] in self.SAFE[self.head[1] - self.tail[1]]:
                return True
        return False

    def moveHead(self, direction, number) -> None:
        match direction:
            case 'L': move: list = self.MOVE['left']
            case 'R': move: list = self.MOVE['right']
            case 'U': move: list = self.MOVE['up']
            case 'D': move: list = self.MOVE['down']

        for _ in range(number):
            self.head = [self.head[0] + move[0], self.head[1] + move[1]]
            self._moveTail()
    
    def _moveTail(self) -> None:
        """ First, check if the tail has to be moved. If so, prioritize non-diagonal movements. """
        # Check if the tail is in range of the head. If so, do nothing.
        if self.checkRange():
            return
        # Check diagonal moves.
        for h in self.MOVE.values():
            for key in self.SAFE.keys():
                for val in self.SAFE[key]:
                    if [self.head[0]+h[0], self.head[1]+h[1]] == [self.tail[0]+val, self.tail[1]+key]:
                        self.tail = [self.tail[0]+val, self.tail[1]+key]
                        self.checkPath()
                        return

def partOne() -> int:
    instruction: list[list[str, int]] = getData()
    rope = Rope(head=[0, 0], tail=[0, 0])
    for inst in instruction:
        rope.moveHead(*inst)
    return len(rope.path.keys())

def partTwo() -> int:
    ...

def main() -> None:
    print(f'ANSWER PART ONE: {partOne()}')
    print(f'ANSWER PART TWO: {partTwo()}')

if __name__ == "__main__":
    main()
