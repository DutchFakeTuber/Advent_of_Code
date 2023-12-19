from Aplenty import TEST, DATA

def fetchData(data: str) -> tuple[dict, list[dict]]:
    split: int = [num for num, val in enumerate(data.splitlines()) if not len(val)][0]
    workflow: dict = {line.split('{')[0]: line.split('{')[1][:-1].split(',') for line in data.splitlines()[:split]}
    ratings: list[dict] = [{value[0]: int(value[2:]) for value in line[1:-1].split(',')} for line in data.splitlines()[split+1:]]
    return workflow, ratings

def check(r: dict, work: dict, character: str='in') -> str:
    parse: function = lambda x: (x[0], x[1], int(x[2:].split(':')[0]), x[2:].split(':')[1])
    while character not in ['A', 'R']:
        for w in work[character]:
            if '<' in w or '>' in w:
                char, inst, num, move = parse(w)
                if (r[char] < num) if inst == '<' else (r[char] > num):
                    character = move
                    break
            else:
                character = w
                break
    return character

def partOne(workflow: dict, ratings: list[dict]) -> int:
    accepted: list = []
    for r in ratings:
        if check(r, workflow) == 'A':
            accepted.append(r)
    return sum([sum(a.values()) for a in accepted])

def partTwo(workflow: dict, ratings: list[dict]) -> int:
    # Make a https://en.wikipedia.org/wiki/K-d_tree!
    ...

if __name__ == "__main__":
    workflow, ratings = fetchData(TEST)
    print(partOne(workflow, ratings))
    print(partTwo(workflow, ratings))
