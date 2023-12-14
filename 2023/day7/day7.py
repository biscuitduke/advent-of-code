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
  Bids = {k : int(v) for line in f for k, v in [line.strip().split()]}

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
  for card in hand:
    # print(card ,Counter(hand)[card])
    power += math.pow(Cards[card], Counter(hand)[card]) * Cards[card]
    count = max(Counter(hand)[card], count)
  
  num_of_cards = len(set(hand))
  hand_dict = {hand : power}
  # print(hand_dict, count)
  if num_of_cards == 1:
    five_of_a_kind.append(hand_dict)
  if num_of_cards == 2:
    if count == 4:
      four_of_a_kind.append(hand_dict)
    elif count == 3:
      full_house.append(hand_dict)
  if num_of_cards == 3:
    if count == 3:
      three_of_a_kind.append(hand_dict)
    elif count == 2:
      two_pair.append(hand_dict)
  if num_of_cards == 4:
    one_pair.append(hand_dict)
  if num_of_cards == 5:
    high_card.append(hand_dict)

hand_types = [five_of_a_kind, four_of_a_kind, full_house, three_of_a_kind, two_pair, one_pair, high_card]
# print(hand_types)

sorted_list = []
for hand_type in hand_types:
  hand_type = sorted(hand_type, key=lambda x: x[list(x.keys())[0]], reverse=True)
  for hand in hand_type:
    sorted_list.append(list(hand.keys())[0])
    
sorted_list.reverse()
enumerated_list = list(enumerate(sorted_list, 1))
for i in enumerated_list:
  print(i)
sum = 0
for hand in enumerated_list:
  sum += hand[0] * Bids.get(hand[1])
print(sum)




    
      