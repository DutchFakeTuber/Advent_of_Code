from Point_of_Incidence import TEST, DATA

def fetchData(data: str) -> list[list[str, str, str]]:
    # [[original, mirror for rowscan, mirror for colscan], ...]
    emptyLines: list = [0] + [num for num, line in enumerate(data.splitlines()) if line == ''] + [len(data.splitlines())]
    patterns: list = []
    for num in range(1, len(emptyLines)):
        patterns.append([[line for line in data.splitlines()[emptyLines[num-1]:emptyLines[num]] if len(line)]])
    for num in range(len(patterns)):
        patterns[num].append([line[::-1] for line in patterns[num][0]])
        patterns[num].append(patterns[num][0][::-1])
    return patterns

def checkAxis(check: tuple[str, str, int, bool]) -> bool:
    original, mirror, pos, row = check
    # Is original[:pos], original[pos::-1] possible for rows?
    # This could be easier to work with.
    if row:
        o, m = len(original[:pos]), len(mirror[:-pos])
        if o > m:
            # print(original[o-m:pos] == mirror[:-pos], f"[{o-m}:{pos}] == [:{-pos}]")
            return original[o-m:pos] == mirror[:-pos]
        elif o == m:
            # print(original[:pos] == mirror[:-pos], f"[:{pos}] == [:{-pos}]")
            return original[:pos] == mirror[:-pos]
        else:
            # print(original[:pos] == mirror[m-o:-pos], f"[:{pos}] == [{m-o}:{-pos}]")
            return original[:pos] == mirror[m-o:-pos]

def partOne(patterns: list[list[str, str, str]]):
    for patt in range(len(patterns)):
        equal: bool = False
        for num in range(len(patterns[patt][0][0])-2, 1, -1):
            length = len(patterns[patt][0])
            equal: list = all([checkAxis((patterns[patt][0][p], patterns[patt][1][p], num, True)) for p in range(length)])
            if equal:
                print(patterns[patt][0][0][num:])
                print(patt, num)


def partTwo(patterns: list[list[str, str, str]]): ...

if __name__ == "__main__":
    patterns: list[list[str, str, str]] = fetchData(TEST)
    print(partOne(patterns))
    print(partTwo(patterns))
