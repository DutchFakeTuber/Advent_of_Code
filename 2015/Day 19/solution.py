import re
from os.path import dirname, realpath

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> tuple[dict[str, list[str]], str]:
    replacements: dict = dict()
    for key, val in [line.split(' => ') for line in data.split('\n\n')[0].splitlines() if len(line)]:
        replacements.setdefault(key, []).append(val)
    return replacements, data.split('\n\n')[1]

def reverse_replacements(replacements: dict[str, list[str]]) -> dict[str, list[str]]:
    reverse: dict = dict()
    for key, values in replacements.items():
        for value in values:
            reverse.setdefault(value, []).append(key)
    return reverse

def generate_prev(target: str, replacements: dict[str, list[str]]) -> set[str]:
    molecules: set = set()
    for key, values in replacements.items():
        index: int = target.find(key)
        while index >= 0:
            for value in values:
                if value == 'e':
                    continue
                try:
                    molecules.add(target[:index]+value+target[index+len(key):])
                except IndexError:
                    molecules.add(target[:index]+value)
            index = target.find(key, index+1)
    if not molecules:
        molecules = {'e'}
    return molecules

def steps_to_generate(target: str, replacements: dict[str, list[str]]) -> int:
    seen: dict = dict()
    last_generation: set[str] = generate_prev(target, replacements)
    steps: int = 1
    while last_generation != {'e'}:
        current_generation: set = set()
        molecule: int = min(last_generation, key=len)
        try:
            new_molecules = seen[molecule]
        except KeyError:
            new_molecules = generate_prev(molecule, replacements)
            seen[molecule] = new_molecules
        current_generation |= new_molecules
        last_generation = current_generation
        steps += 1
    return steps

def partOne(replacements: dict[str, list[str]], molecule: str) -> int:
    newMolecules: set = set()
    for key, values in replacements.items():
        for value in values:
            for m in re.finditer(key, molecule):
                newMolecules.add(molecule[:m.start()] + value + molecule[m.end():])
    return len(newMolecules)

def partTwo(replacements: dict[str, list[str]], molecule: str) -> int:
    replacements: dict[str, list[str]] = reverse_replacements(replacements)
    return steps_to_generate(molecule, replacements)

if __name__ == "__main__":
    replacements, molecule = fetchData(DATA)
    print(partOne(replacements, molecule))
    print(partTwo(replacements, molecule))
