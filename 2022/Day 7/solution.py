TEST: str = open("test.txt")
DATA: str = open("input.txt")

def getData() -> list[list]:
    return [line.split(' ') for line in DATA.splitlines() if len(line) != 0]

class Drive:
    def __init__(self) -> None:
        self.commands: list[list] = getData()
        self.path: list = ['/']
        self.folders: dict = {self.path[0]: {}}
    
    def cd(self, command: str) -> None:
        match command:
            case '/': self.path = ['/']
            case '..': self.path.pop()
            case _: self.path.append(command)

    def dictPath(self, _dict: dict, path: list) -> dict:
        return _dict[path[0]] if len(path) == 1 else self.dictPath(_dict[path[0]], path[1:])
    
    def size(self, _dict: dict) -> int:
        return sum(self.size(_d) if isinstance(_d, dict) else _d for _d in _dict.values())

    def traverse(self, _dict: dict, _size: list=None) -> list:
        if not _size:
            _size = []
        for value in _dict.values():
            if isinstance(value, dict):
                _size.append(self.size(value))
                self.traverse(value, _size)
        return _size
    
    def generate(self) -> None:
        for c in self.commands:
            if c[0:2] == ['$', 'cd']: self.cd(c[2])
            if c[0:2] == ['$', 'ls']: continue
            else:
                if c[0].isnumeric():
                    self.dictPath(self.folders, self.path)[c[1]] = int(c[0])
                else:
                    self.dictPath(self.folders, self.path)[c[1]] = {}
        return self

def partOne() -> int:
    drive: Drive = Drive().generate()
    return sum(f for f in drive.traverse(drive.folders) if f <= 100_000)
                
def partTwo() -> int:
    drive: Drive = Drive().generate()
    folders: list = [f for f in drive.traverse(drive.folders)]
    required: int = 30_000_000 - (70_000_000 - max(folders))
    return min(f for f in folders if f >= required)

def main() -> None:
    print(f'ANSWER PART ONE: {partOne()}')
    print(f'ANSWER PART TWO: {partTwo()}')

if __name__ == "__main__":
    main()
