Cards = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

with open("example") as f:
  Hands = {k: int(v) for line in f for (k, v) in [line.strip().split(None, 1)]}


