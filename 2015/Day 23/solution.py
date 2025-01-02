from os.path import dirname, abspath
import re

TEST: str = open(f'{dirname(abspath(__file__))}\\test.txt').read()
DATA: str = open(f'{dirname(abspath(__file__))}\\input.txt').read()

class Computer:
    def __init__(self, offset: bool=False) -> None:
        self.a: int = int(offset)
        self.b: int = 0
    
    def hlf(self, register: str, offset: None) -> None:
        if register == 'a':
            self.a //= 2
        else:
            self.b //= 2
    
    def tpl(self, register: str, offset: None) -> None:
        if register == 'a':
            self.a *= 3
        else:
            self.b *= 3
    
    def inc(self, register: str, offset: None) -> None:
        if register == 'a':
            self.a += 1
        else:
            self.b += 1
    
    def jmp(self, register: None, offset: int) -> int:
        return offset
    
    def jie(self, register: str, offset: int) -> int | None:
        return offset if not getattr(self, register) % 2 else None
    
    def jio(self, register: str, offset: int) -> int | None:
        return offset if getattr(self, register) == 1 else None

def fetchData(data: str) -> list[list[str, str | None, int | None]]:
    instructions: list = []
    for line in data.splitlines():
        regex: re.match = re.match(r"^(jio|jie|jmp|inc|tpl|hlf)\s+(?:([ab])(?:,\s*([+-]?\d+))?|([+-]?\d+))$", line)
        instruction: list = [regex.group(1), regex.group(2), regex.group(3) or regex.group(4)]
        if isinstance(instruction[-1], str):
            instruction[-1] = int(instruction[-1])
        instructions.append(instruction)
    return instructions

def parts(data: list[list[str, str | None, int | None]], offset: bool=False) -> int:
    length: int = len(data)
    position: int = 0
    computer: Computer = Computer(offset)
    while position < length:
        instruction, register, value = data[position]
        offset: int | None = getattr(computer, instruction)(register, value)
        if isinstance(offset, int):
            position += offset
            continue
        position += 1
    return computer.b

if __name__ == "__main__":
    data: list[list[str, str | None, int | None]] = fetchData(DATA)
    print(parts(data, offset=False))
    print(parts(data, offset=True))
