from collections import Counter
import math

Cards = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 11,
    "9": 10,
    "8": 9,
    "7": 8,
    "6": 7,
    "5": 6,
    "4": 5,
    "3": 4,
    "2": 3,
    "J": 2
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
  power = 0
  count = 0
  card_cnt=0
  for card in hand:
    if card != 'J':
      card_cnt = Counter(hand)[card]
    if card_cnt > count:
      count = card_cnt
  print(count)
  hand_set = set(hand)
  isJ = False
  if 'J' in hand_set:
    count +=Counter(hand)['J']
    isJ = True
  print(hand, count)
  num_of_cards = len(set(hand))
  if num_of_cards == 1 or (num_of_cards == 2 and isJ):
    five_of_a_kind.append(hand)
  elif num_of_cards == 2 or (num_of_cards == 3 and isJ):
    if count == 4:
      four_of_a_kind.append(hand)
    elif count == 3:
      full_house.append(hand)
  elif num_of_cards == 3 or (num_of_cards == 4 and isJ):
    if count == 3:
      three_of_a_kind.append(hand)
    elif count == 2:
      two_pair.append(hand)
  elif num_of_cards == 4 or (num_of_cards == 5 and isJ):
    one_pair.append(hand)
  elif num_of_cards == 5 and not isJ:
    high_card.append(hand)

hand_types = [
    five_of_a_kind, four_of_a_kind, full_house, three_of_a_kind, two_pair,
    one_pair, high_card
]
# print(hand_types)
sorted_list = []
for hand_type in hand_types:
  hand_type = sorted(hand_type,
                     key=lambda x: [Cards[c] for c in x],
                     reverse=True)
  for hand in hand_type:
    sorted_list.append(hand)

sorted_list.reverse()
enumerated_list = list(enumerate(sorted_list, 1))
sum = 0
for i in enumerated_list:
  print(i)
for hand in enumerated_list:
  sum += hand[0] * Bids.get(hand[1])
print(sum)
