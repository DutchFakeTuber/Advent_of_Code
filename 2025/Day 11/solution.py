from os.path import dirname, realpath
from functools import cache

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> dict[str, tuple[str]]:
    return {line.split(': ')[0]: tuple(line.split(': ')[1].split(' ')) for line in data.splitlines()}

class Reactor:
    def __init__(self, data: dict[str, list[str]]) -> None:
        self.nodes: dict[str, list[str]] = data

    @cache
    def follow(self, node: str, dac: bool=False, fft: bool=False) -> int:
        match node:
            case 'out': return dac and fft
            case 'dac': dac = True
            case 'fft': fft = True
        return sum([self.follow(n, dac, fft) for n in self.nodes[node]])

def parts(data: dict[str, list[str]], start: str='you') -> int:
    reactor: Reactor = Reactor(data)
    return reactor.follow(start, dac=start == 'you', fft=start == 'you')

if __name__ == "__main__":
    data: dict[str, list[str]] = fetchData(DATA)
    print(parts(data, start='you'))
    print(parts(data, start='svr'))
