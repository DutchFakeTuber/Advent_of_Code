TEST: str = open("test.txt")
DATA: str = open("input.txt")

def fetchData(data: str) -> list[list[int]]:
    return [list(map(int, line.split())) for line in data.splitlines()]

class Mirage:
    def __init__(self, history: list[int], last: bool=True) -> None:
        self.history: list[list[int]] = [history]
        self.last: bool = last
        self.zero: bool = False
    
    def generate(self) -> None:
        while not self.zero:
            sequence: list = []
            for num in range(len(self.history[-1])):
                if num + 1 == len(self.history[-1]):
                    continue
                sequence.append(self.history[-1][num + 1]-self.history[-1][num])
            self.zero: bool = all([True if seq == 0 else False for seq in sequence])
            self.history.append(sequence)
        for num in range(len(self.history)):
            self.history[num] = [*self.history[num], None] if self.last else [None, *self.history[num]]
            
    def predict(self) -> None:
        for num in range(len(self.history)-1, -1, -1):
            if num == len(self.history) - 1:
                self.history[num][-1 if self.last else 0] = 0
                continue
            if self.last:
                self.history[num][-1] = self.history[num + 1][-1] + self.history[num][-2]
            else:
                self.history[num][0] = self.history[num][1] - self.history[num + 1][0]
    
    def __str__(self) -> str:
        return f"{self.history}"

def partOne(data: list[list[int]]):
    extrapolated: int = 0
    for d in data:
        mirage: Mirage = Mirage(d, last=True)
        mirage.generate()
        mirage.predict()
        extrapolated += mirage.history[0][-1]
    return extrapolated

def partTwo(data: list[list[int]]):
    extrapolated: int = 0
    for d in data:
        mirage: Mirage = Mirage(d, last=False)
        mirage.generate()
        mirage.predict()
        extrapolated += mirage.history[0][0]
    return extrapolated

if __name__ == "__main__":
    data: list[list[int]] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
