from collections import Counter
import math

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
file = 'input'
with open(file) as f:
  Hands = [k for line in f for k, v in [line.strip().split()]]
with open(file) as f:
  Bids = {k: int(v) for line in f for k, v in [line.strip().split()]}

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []

for hand in Hands:
  # sorted_hand = sorted(list(set(hand)), key=Cards.get, reverse=True)
  # print(sorted_hand)
  power = 0
  count = 0
  max_card = ''
  for card in hand:
    card_cnt = Counter(hand)[card]
    if card_cnt > count:
      count = card_cnt
  num_of_cards = len(set(hand))
  if num_of_cards == 1:
    five_of_a_kind.append(hand)
  if num_of_cards == 2:
    if count == 4:
      four_of_a_kind.append(hand)
    elif count == 3:
      full_house.append(hand)
  if num_of_cards == 3:
    if count == 3:
      three_of_a_kind.append(hand)
    elif count == 2:
      two_pair.append(hand)
  if num_of_cards == 4:
    one_pair.append(hand)
  if num_of_cards == 5:
    high_card.append(hand)

hand_types = [
    five_of_a_kind, four_of_a_kind, full_house, three_of_a_kind, two_pair,
    one_pair, high_card
]
# print(hand_types)

sorted_list = []
for hand_type in hand_types:
  hand_type = sorted(hand_type,
                     key=lambda x: Cards[x[0]],
                     reverse=True)
  for hand in hand_type:
    sorted_list.append(hand)

sorted_list.reverse()
enumerated_list = list(enumerate(sorted_list, 1))
for i in enumerated_list:
  print(i)
sum = 0
for hand in enumerated_list:
  sum += hand[0] * Bids.get(hand[1])
print(sum)
