INPUT: str = """
Monkey 0:
  Starting items: 76, 88, 96, 97, 58, 61, 67
  Operation: new = old * 19
  Test: divisible by 3
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 93, 71, 79, 83, 69, 70, 94, 98
  Operation: new = old + 8
  Test: divisible by 11
    If true: throw to monkey 5
    If false: throw to monkey 6

Monkey 2:
  Starting items: 50, 74, 67, 92, 61, 76
  Operation: new = old * 13
  Test: divisible by 19
    If true: throw to monkey 3
    If false: throw to monkey 1

Monkey 3:
  Starting items: 76, 92
  Operation: new = old + 6
  Test: divisible by 5
    If true: throw to monkey 1
    If false: throw to monkey 6

Monkey 4:
  Starting items: 74, 94, 55, 87, 62
  Operation: new = old + 5
  Test: divisible by 2
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 5:
  Starting items: 59, 62, 53, 62
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 4
    If false: throw to monkey 7

Monkey 6:
  Starting items: 62
  Operation: new = old + 2
  Test: divisible by 17
    If true: throw to monkey 5
    If false: throw to monkey 7

Monkey 7:
  Starting items: 85, 54, 53
  Operation: new = old + 3
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 0
"""
