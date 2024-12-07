from collections import Counter

TEST: str = open("test.txt")
DATA: str = open("input.txt")

def getInstructions(instr: str) -> dict:
    instructions: dict = {}
    for line in instr.splitlines():
        if len(line) == 0: continue
        instruction, letter = line.strip().split(' -> ')
        instructions[instruction] = letter
    return instructions

def getCombinations(data: str) -> list:
    return [char+char_plus for char, char_plus in zip(data, data[1:])]

def partOne(data: str, instructions: dict) -> int:
    for _ in range(0, 10):
        coms: list = getCombinations(data)
        newComs: list = [
            coms[number][0:1] + instructions[combi] + coms[number][1:3] if number == 0
            else instructions[combi] + coms[number][1:3]
            for number, combi in enumerate(coms)
        ]
        data: str = ''.join(combi for combi in newComs)
    
    common: list = Counter(data).most_common()
    return common[0][1] - common[-1][1]

def partTwo(data: str, instructions: dict) -> int:
    combinations: list = getCombinations(data)
    instrCount: dict = {instr: 0 for instr in instructions.keys()}
    for comb in combinations: # First time setup of the dictionary
        instrCount[comb] += 1

    for _ in range(0, 40):
        newInstrCount: dict = {instr: value for instr, value in zip(instrCount.keys(), instrCount.values()) if value > 0}
        for instr, value in newInstrCount.items():
            instrCount[instr] -= 1 * value
            instrCount[instr[0:1] + instructions[instr]] += 1 * value
            instrCount[instructions[instr] + instr[1:3]] += 1 * value
    
    letters: dict = {letter[0]: 0 for letter in Counter(''.join(combi for combi in instrCount.keys())).most_common()}
    for char, amount in instrCount.items():
        letters[char[0:1]] += amount
        letters[char[1:3]] += amount
    for char, amount in letters.items():
        letters[char] = amount//2 if amount % 2 == 0 else amount//2 + 1
    
    common: list = Counter(letters).most_common()
    return common[0][1] - common[-1][1]

def main() -> None:
    instructions = getInstructions(INSTRUCTIONS)
    print(partOne(DATA, instructions))
    print(partTwo(DATA, instructions))

if __name__ == "__main__":
    main()