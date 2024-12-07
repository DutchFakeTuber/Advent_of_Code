TEST: str = open("test.txt")
DATA: str = open("input.txt")

class ALU:
    def __init__(self, input: str) -> None:
        self.val: dict = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
        self.input: list = [x for x in input]
        self.position = 0

    def operation(self, instruction: str, a: str, b: str | int=None) -> None:
        match instruction:
            case 'inp':
                self.val[a] = int(self.input[self.position])
                self.position += 1
            case 'add': self.val[a] += self.val[b] if b.isalpha() else int(b)
            case 'mul': self.val[a] *= self.val[b] if b.isalpha() else int(b)
            case 'div': self.val[a] //= self.val[b] if b.isalpha() else int(b)
            case 'mod': self.val[a] %= self.val[b] if b.isalpha() else int(b)
            case 'eql': self.val[a] = (1 if self.val[a] == self.val[b] else 0) if b.isalpha() else (1 if self.val[a] == int(b) else 0)
    
    def __str__(self) -> str:
        return f'POSITION: {self.input} - {self.position-1} - {self.val}'

def getData() -> list[list]:
    return [row.split(' ') for row in DATA.splitlines() if len(row) != 0]

def checkIfTrue(inp: int) -> bool:
    alu: ALU = ALU(str(inp))
    for x in getData():
        alu.operation(*x)
    if alu.val['z'] == 0:
        return True
    return False

def main() -> None:
    """
    USED https://github.com/dphilipson/advent-of-code-2021/blob/master/src/days/day24.rs:
    
    input[3]  = input[2]
    input[5]  = input[4] + 2
    input[6]  = input[1] + 6
    input[10] = input[9] - 3
    input[11] = input[8] + 7
    input[12] = input[7] - 8
    input[13] = input[0] - 7
    """
    ANSWER_PART_ONE: int = 93997999296912
    ANSWER_PART_TWO: int = 81111379141811
    assert checkIfTrue(ANSWER_PART_ONE) == True
    assert checkIfTrue(ANSWER_PART_TWO) == True
    print(f'PASSED!\nANSWER PART ONE: {ANSWER_PART_ONE}\nANSWER PART TWO: {ANSWER_PART_TWO}')

if __name__ == "__main__":
    main()        
