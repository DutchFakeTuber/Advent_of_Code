from Corporate_Policy import INPUT

ALPHABET: str = "abcdefghijklmnopqrstuvwxyz"
POSITION: dict[str, int] = {char: num for num, char in enumerate(ALPHABET)}
FORBIDDEN: list = ['i', 'o', 'l']
SEQUENCE: list = [ALPHABET[num:num+3] for num in range(0, 24) if not ALPHABET[num:num+3] in FORBIDDEN]
PAIRS: list = [char*2 for char in ALPHABET if char not in FORBIDDEN]

def passwordLoop(password: str, position: int=7) -> str:
    assert position != 0
    if password[position] != "z":
        password = password[:position] + ALPHABET[POSITION[password[position]] + 1] + password[position+1:]
    else:
        password = password[:position] + "a" + password[position+1:]
        password = passwordLoop(password, position=position-1)
    return password

def checkForbidden(password: str) -> str:
    index: list[int] = [pos for pos, char in enumerate(password) if char in FORBIDDEN]
    # index: list[int] = [password.find(forbiddenChar) for forbiddenChar in FORBIDDEN]
    if len(index) == 0:
        return password
    position: int = min(index)
    password = password[:position] + ALPHABET[POSITION[password[position]] + 1] + "a" * len(password[position+1:])
    return password

def checkMatches(password: str) -> bool:
    matches: int = 0
    for pair in PAIRS:
        if pair in password:
            matches += 1
    if matches != 2:
        return False
    sequence: bool = False
    for seq in SEQUENCE:
        if seq in password:
            sequence = True
    return sequence

def partOne(password: str) -> str:
    while True:
        password = passwordLoop(password)
        password = checkForbidden(password)
        if checkMatches(password):
            break
    return password

def partTwo(password: str) -> str:
    password = partOne(password)
    return partOne(password)

if __name__ == "__main__":
    print(partOne(INPUT))
    print(partTwo(INPUT))
