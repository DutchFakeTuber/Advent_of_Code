import ast

TEST: str = open("test.txt")
DATA: str = open("input.txt")

def getData(data: str) -> list:
    return [r.rstrip() for r in data.readlines()]

def partOne() -> int:
    return sum([len(line) - len(ast.literal_eval(line)) for line in getData()])

def partTwo() -> int:
    func: function = lambda x: x.replace('\\', '\\\\').replace('"', '\\"')
    return sum([len(f'"{func(line)}"') - len(line) for line in getData()])

def main() -> None:
    print(partOne())
    print(partTwo())

if __name__ == "__main__":
    main()
