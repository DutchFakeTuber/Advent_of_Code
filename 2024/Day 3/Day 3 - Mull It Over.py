from Mull_It_Over import TEST_P1, TEST_P2, DATA


def mul(a: int, b: int) -> int:
    return a * b

def scanForMul(data: str, position: int) -> int:
    hits: dict = dict(num1=False, num2=False, comma=False, bracket=False)
    counter: int = position+4
    while True:
        if not hits["comma"] and data[counter].isdigit():
            hits["num1"] = True
        elif hits["comma"] and data[counter].isdigit():
            hits["num2"] = True
        elif not hits["comma"] and data[counter] == ",":
            hits["comma"] = True
        elif data[counter] == ")":
            hits["bracket"] = True
            break
        else:
            break
        if counter >= len(data):
            break
        counter += 1
    if all(hits.values()):
        return eval(data[position:counter+1])
    return 0
    
def partOne(data: str) -> int:
    total: list[int] = []
    for pos in range(len(data)):
        if data[pos:pos+4] == "mul(":
            total.append(scanForMul(data, pos))
    return sum(total)

def partTwo(data: str) -> int:
    total: list[int] = []
    enabled: bool = True
    for pos in range(len(data)):
        if data[pos:pos+7] == "don't()":
            enabled = False
        elif data[pos:pos+4] == "do()":
            enabled = True
        if data[pos:pos+4] == "mul(" and enabled:
            total.append(scanForMul(data, pos))
    return sum(total)

if __name__ == "__main__":
    print(partOne(DATA))
    print(partTwo(DATA))
