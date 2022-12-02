from Some_Assembly_Required import INPUT

def getData() -> list:
    return [
        [l.split(' ') if len(l.split(' ')) > 1 else l for l in line.split(' -> ')]
        for line in INPUT.splitlines() if len(line) != 0
    ]

class ASM:
    def __init__(self, 
                 _a: str, 
                 operation: str = None, 
                 _b: str = None, 
                 output: str = None) -> None:
        self.a: str = _a if not str(_a).isnumeric() else int(_a)
        self.b: str | None = _b if not str(_b).isnumeric() else int(_b)
        self.operation: str | None = operation
        self.output: str | int = output
        self.processed: bool = False
    
    def __str__(self) -> str:
        return f'{self.a=}; {self.operation=}; {self.b=}; {self.output=}; {self.processed=}'
    
    def OPERATION(self) -> int:
        match self.operation:
            case 'RSHIFT': return self.a >> self.b
            case 'LSHIFT': return self.a << self.b
            case 'AND': return self.a & self.b
            case 'OR': return self.a | self.b
            case 'NOT': return ~self.a
            case _: return self.a
    
    def process(self) -> list[int | None, bool]:
        if isinstance(self.a, int) and self.b == None:
            value = self.OPERATION()
        elif isinstance(self.a, int) and isinstance(self.b, int):
            value = self.OPERATION()
        else:
            return [None, False]
        return [value, True]

def assembler(assembly: list[ASM]) -> int:
    while True:
        for asm in assembly:
            if not asm.processed:
                value, state = asm.process()
                if state:
                    asm.processed = state
                    for _asm in assembly:
                        if _asm.a == asm.output:
                            _asm.a = value
                        elif _asm.b == asm.output:
                            _asm.b = value
                    if asm.output == 'a':
                        return value

def partOne() -> int:
    wires: list[ASM] = []
    for _in, _out in getData():
        if isinstance(_in, list):
            wires.append(ASM(_in[1], _in[0], None, _out) if str(_in[0]).isupper() else ASM(*_in, _out))
        else:
            wires.append(ASM(_in, None, None, _out))
    return assembler(wires)

def partTwo() -> int:
    _b = partOne()
    wires: list[ASM] = []
    for _in, _out in getData():
        if isinstance(_in, list):
            wires.append(ASM(_in[1], _in[0], None, _out) if str(_in[0]).isupper() else ASM(*_in, _out))
        else:
            wires.append(ASM(_in, None, None, _out))
    for asm in wires:
        if asm.output == 'b':
            asm.a = _b
    return assembler(wires)
    
def main() -> None:
    print(partOne())
    print(partTwo())

if __name__ == "__main__":
    main()
