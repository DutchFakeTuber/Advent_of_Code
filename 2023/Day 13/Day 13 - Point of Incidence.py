from Point_of_Incidence import TEST, DATA

def fetchData(data: str) -> list[list[str, str, str]]:
    emptyLines: list = [0] + [num for num, line in enumerate(data.splitlines()) if line == ''] + [len(data.splitlines())]
    patterns: list = []
    for num in range(1, len(emptyLines)):
        pattern: list[str] = [line for line in data.splitlines()[emptyLines[num-1]:emptyLines[num]] if len(line)]
        patterns.append([pattern, [line[::-1] for line in pattern], pattern[::-1]])
    return patterns

def checkAxis(original: str, mirror: str, pos: int) -> tuple[bool, int]:
    o, m = len(original[:pos]), len(mirror[:-pos])
    if o >= m:
        original: str = original[o-m:pos]
        mirror: str = mirror[:-pos]
        return (original == mirror, sum([0 if original[num] == mirror[num] else 1 for num in range(len(original))]))
    else:
        original: str = original[:pos]
        mirror: str = mirror[m-o:-pos]
        return (original == mirror, sum([0 if original[num] == mirror[num] else 1 for num in range(len(original))]))

def parts(patterns: list[list[str, str, str]]):
    mirror: int = 0
    broken: int = 0
    for patt in range(len(patterns)):
        for num in range(len(patterns[patt][0][0])-1, 0, -1):
            length: int = len(patterns[patt][0])
            results = [checkAxis(patterns[patt][0][p], patterns[patt][1][p], num) for p in range(length)]
            if all([x[0] for x in results]):
                mirror += num
            if sum([x[1] for x in results]) == 1:
                broken += num
        for num in range(len(patterns[patt][0])-1, 0, -1):
            length: int = len(patterns[patt][0][0])
            results = [checkAxis(''.join(x[p] for x in patterns[patt][0]), ''.join(x[p] for x in patterns[patt][2]), num) for p in range(length)]
            if all(x[0] for x in results):
                mirror += num * 100
            if sum(x[1] for x in results) == 1:
                broken += num * 100
    return mirror, broken

if __name__ == "__main__":
    patterns: list[list[str, str, str]] = fetchData(DATA)
    print(*parts(patterns), sep='\n')
