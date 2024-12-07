from collections import Counter

TEST: str = open("test.txt")
DATA: str = open("input.txt")

def fetchData(data: str) -> dict[str, int]:
    return {line.split()[0]: int(line.split()[1]) for line in data.splitlines()}

class Cards:    
    WEIGHT_NORMAL: dict = {str(card): val for card, val in zip([*range(2,10), *'TJQKA'], [*range(1, 10), *'ABCD'])}
    WEIGHT_JOKER: dict = {str(card): val for card, val in zip(['J', *range(2, 10), *'TQKA'], [*range(1, 10), *'ABCD'])}

    def __init__(self, jokerMode: bool=False) -> None:
        self.FIVE_OF_A_KIND: list = []
        self.FOUR_OF_A_KIND: list = []
        self.FULL_HOUSE: list = []
        self.THREE_OF_A_KIND: list = []
        self.TWO_PAIR: list = []
        self.ONE_PAIR: list = []
        self.HIGH_CARD: list = []
        self.ALL_CARDS: list = []
        self.jokerMode: bool = True if jokerMode else False

    def sortValue(self, hands: list) -> None:
        weight: dict = self.WEIGHT_JOKER if self.jokerMode else self.WEIGHT_NORMAL
        for num, (hand, bid) in enumerate(hands):
            hands[num] = [int(''.join(str(weight[card]) for card in hand), base=16), hand, bid]
        hands.sort(key=lambda x: x[0])
        return hands

    def checkJoker(self, cards: str) -> str:
        hand: dict = {**Counter(cards)}
        if 'J' in hand.keys() and hand.get('J', 0) < 5:
            hand.pop('J')
            hand: list = [[card, num] for card, num in hand.items()]
            hand.sort(key=lambda x: x[1], reverse=True)
            card: str = hand[0][0]
            cards: str = cards.replace('J', card)
        return cards

    def sortKind(self, data: dict[str, int]) -> None:
        for cards, bid in data.items():
            _cards: str = cards
            if self.jokerMode:
                _cards: str = self.checkJoker(_cards)
            match sorted(list(Counter(_cards).values()), reverse=True):
                case [5]: self.FIVE_OF_A_KIND.append([cards, bid])
                case [4, 1]: self.FOUR_OF_A_KIND.append([cards, bid])
                case [3, 2]: self.FULL_HOUSE.append([cards, bid])
                case [3, 1, 1]: self.THREE_OF_A_KIND.append([cards, bid])
                case [2, 2, 1]: self.TWO_PAIR.append([cards, bid])
                case [2, 1, 1, 1]: self.ONE_PAIR.append([cards, bid])
                case [1, 1, 1, 1, 1]: self.HIGH_CARD.append([cards, bid])
                case _: raise ValueError()
        self.ALL_CARDS: list[int, str, int] = [
            *self.sortValue(self.HIGH_CARD),    
            *self.sortValue(self.ONE_PAIR),
            *self.sortValue(self.TWO_PAIR),
            *self.sortValue(self.THREE_OF_A_KIND),
            *self.sortValue(self.FULL_HOUSE),
            *self.sortValue(self.FOUR_OF_A_KIND),
            *self.sortValue(self.FIVE_OF_A_KIND),
        ]    

def partOne(data: dict[str, int]) -> int:
    cards: Cards = Cards()
    cards.sortKind(data)
    return sum([num * cards[2] for num, cards in enumerate(cards.ALL_CARDS, start=1)])

def partTwo(data: str) -> int:
    cards: Cards = Cards(jokerMode=True)
    cards.sortKind(data)
    return sum([num * cards[2] for num, cards in enumerate(cards.ALL_CARDS, start=1)])

if __name__ == "__main__":
    data: dict[str, int] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
