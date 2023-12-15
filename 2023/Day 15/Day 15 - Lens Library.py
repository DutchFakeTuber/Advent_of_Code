from Lens_Library import TEST, DATA

def fetchData(data: str) -> list[str]:
    return data.split(',')

class HashAlgo:
    def __init__(self, data: list[str]) -> None:
        self.ascii = [(d, ''.join(c for c in d if c.isalpha())) for d in data]
        self.boxes: dict = {num: [] for num in range(256)}

    def get(self, chars: list[int], prev: int=0) -> int:
        if not len(chars):
            return prev
        char: int = chars.pop(0)
        return self.get(chars, prev=((prev + char) * 17) % 256)
    
    def remove(self, location: int, label: str) -> None:
        for num, char in enumerate(self.boxes[location]):
            if label in char:
                self.boxes[location].pop(num)
    
    def present(self, location: int, label: str, focal: int) -> bool:
        for num, char in enumerate(self.boxes[location]):
            if label in char:
                self.boxes[location][num] = f'{label} {focal}'
                return True
        return False
    
    def add(self, location: int, label: str, focal: int) -> None:
        self.boxes[location].append(f'{label} {focal}')

def partOne(ascii: list[str]) -> int:
    hashAlgo: HashAlgo = HashAlgo(ascii)
    return sum(hashAlgo.get(list(map(ord, chars))) for chars, _ in hashAlgo.ascii)

def partTwo(ascii: list[str]) -> int:
    hashAlgo: HashAlgo = HashAlgo(ascii)
    for chars, label in hashAlgo.ascii:
        location = hashAlgo.get(list(map(ord, label)))
        operation, *focal = chars[len(label):]
        if operation == '-':
            hashAlgo.remove(location, label)
            continue
        if not hashAlgo.present(location, label, int(focal[0])):
            hashAlgo.add(location, label, int(focal[0]))
    return sum(((key + 1) * num * focal) for key, val in hashAlgo.boxes.items() for num, focal in enumerate(map(lambda x: int(x[-1]), val), start=1))

if __name__ == "__main__":
    data: list[str] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
