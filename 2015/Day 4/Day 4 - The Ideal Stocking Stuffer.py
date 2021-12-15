from hashlib import md5
from The_Ideal_Stocking_Stuffer import DATA

def MD5(number, data: str) -> str:
    return md5(f"{data + str(number)}".encode()).hexdigest()

def parts(data: str, zeros: int=0) -> int:
    number: int = 0
    zeros: str = '0'*zeros
    while True:
        hexa = MD5(number, data)
        if hexa.startswith(zeros):
            return number
        number += 1

def main() -> None:
    print(parts(DATA, zeros=5))
    print(parts(DATA, zeros=6))

if __name__ == "__main__":
    main()