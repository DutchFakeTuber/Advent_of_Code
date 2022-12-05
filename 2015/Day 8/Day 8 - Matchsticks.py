import os, ast

def getData() -> list:
    return [r.rstrip() for r in open(os.path.join(os.path.dirname(__file__), 'Matchsticks.txt'), 'r').readlines()]

def partOne() -> int:
    return sum([len(line) - len(ast.literal_eval(line)) for line in getData()])

def partTwo() -> int:
    ...

def main() -> None:
    print(partOne())
    print(partTwo())

if __name__ == "__main__":
    main()

