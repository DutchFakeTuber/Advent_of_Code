from time import perf_counter
from Print_Queue import TEST, DATA

def fetchData(data: str) -> list[list[list[int]], list[list[int]]]:
    return [[list(map(int, _d.split(char))) for _d in d.splitlines() if len(_d)] for d, char in zip(data.split('\n\n'), ['|', ','])]

def sortOrder(order: list[list[int, int]]) -> list[dict, dict]:
    order_before, order_after = {}, {}
    for before, after in order:
        order_before.setdefault(before, set()).add(after)
        order_after.setdefault(after, set()).add(before)
    return [order_before, order_after]

def checkOrder(page: list[int], order_before: dict[int, set], order_after: dict[int, set]) -> bool:
    for num, value in enumerate(page) :
        for p in page[:num]:
            if value not in order_before:
                break
            if p in order_before[value]:
                return False
        for p in page[num+1:]:
            if value not in order_after:
                break
            if p in order_after[value]:
                return False
    return True

def correctOrder(page: list[int], order_after: dict[int, set]) -> list[int]:
    page = set(page)
    correct_page: list = []
    while len(page) > 0:
        good_position: bool = True
        for value in page:
            p: set = page - {value}
            if value not in order_after or len(order_after[value] & p) == 0:
                correct_page.append(value)
                page.remove(value)
                good_position = False
                break
        if good_position:
            page.remove(value)
            good_position.append(value)
    return correct_page

def partOne(order: list[list[int]], pages: list[list[int]]) -> int:
    before, after = sortOrder(order)
    return sum([page[len(page)//2] for page in pages if checkOrder(page, before, after)])

def partTwo(order: list[list[int]], pages: list[list[int]]) -> int:
    before, after = sortOrder(order)
    return sum([correctOrder(page, after)[len(page)//2] for page in pages if not checkOrder(page, before, after)])

if __name__ == "__main__":
    order, pages = fetchData(DATA)
    start = perf_counter()
    print(partOne(order, pages))
    print(partTwo(order, pages))
