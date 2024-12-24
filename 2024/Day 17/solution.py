import re
from os.path import dirname, realpath
from collections import deque

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> tuple[dict[str, int], list[int]]:
    match = re.search(r"A: (\d+).*?B: (\d+).*?C: (\d+).*?Program: ([\d,]+)", data, re.DOTALL)
    return dict(A=int(match.group(1)), B=int(match.group(2)), C=int(match.group(3))), list(map(int, match.group(4).split(',')))

class Computer:
    def __init__(self, registers: dict[str, int], program: list[int]) -> None:
        self.A = registers['A']
        self.B = registers['B']
        self.C = registers['C']
        self.program: list[int] = program
        self.pointer: int = 0
        self.output: list[int] = []

    def __repr__(self) -> str:
        return ','.join(map(str, self.output))
    
    def __eq__(self, other: str) -> bool:
        return ','.join(map(str, self.output)) == other

    def adv(self, operand: int, literal: int) -> None:
        self.A //= (2**operand)
        self.pointer += 2

    def bxl(self, operand: int, literal: int) -> None:
        self.B ^= literal
        self.pointer += 2

    def jnz(self, operand: int, literal: int) -> None:
        self.pointer = (self.pointer + 2) if self.A == 0 else literal

    def bxc(self, operand: int, literal: int) -> None:
        self.B ^= self.C
        self.pointer += 2

    def bst(self, operand: int, literal: int) -> None:
        self.B = operand % 8
        self.pointer += 2

    def out(self, operand: int, literal: int) -> None:
        self.output.append(operand % 8)
        self.pointer += 2

    def bdv(self, operand: int, literal: int) -> None:
        self.B = self.A // (2**operand)
        self.pointer += 2

    def cdv(self, operand: int, literal: int) -> None:
        self.C = self.A // (2**operand)
        self.pointer += 2

    def reset(self) -> object:
        self.pointer = 0
        self.output = []
        return self

    def process(self) -> None:
        opcode: dict = {0: 'adv', 1: 'bxl', 2: 'bst', 3: 'jnz', 4: 'bxc', 5: 'out', 6: 'bdv', 7: 'cdv'}
        while len(self.program) - self.pointer >= 2:
            combo: dict = {0: 0, 1: 1, 2: 2, 3: 3, 4: self.A, 5: self.B, 6: self.C, 7: None}
            combo_value: int = combo[self.program[self.pointer+1]]
            getattr(self, opcode[self.program[self.pointer]])(combo_value, self.program[self.pointer+1])

def partOne(registers: dict[str, int], program: list[int]) -> str:
    computer: Computer = Computer(registers, program)
    computer.process()
    return computer
    
def partTwo(registers: dict[str, int], program: list[int]) -> int:
    todo: deque = deque([0b0])
    done: deque = deque()
    for position in range(len(program)):
        computer: Computer = Computer(registers, program)
        equal: str = ','.join(map(str, program[len(program) - position - 1:]))
        while todo:
            A: int = todo.popleft() << 3
            for number in range(8):
                A = (A & ~0b111) | number
                computer.A = A
                computer.reset().process()
                if computer == equal:
                    done.append(A)
        todo: deque = done
        done: deque = deque()
    return min(todo)

if __name__ == "__main__":
    registers, program = fetchData(DATA)
    print(partOne(registers, program))
    print(partTwo(registers, program))
