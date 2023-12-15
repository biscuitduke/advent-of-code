#result_dict = {pattern.search(s).group(1):tuple(map(str.strip, pattern.search(s).group(2).split(',')))}
import re

f = open('input', 'r')
Lines = f.readlines()

instructions = Lines[0].replace('\n', '')
# for c in instructions:
#   print(c)

network = {}
pattern = re.compile(r'(\w+)\s*=\s*\(([^)]+)\)')

for line in Lines[2:]:
  network[pattern.search(line).group(1)] = tuple(map(str.strip, pattern.search(line).group(2).split(',')))
# print(network)

current_node = list(network.keys())[0]
steps = 0
while current_node != 'ZZZ':
  for c in instructions:
    if c == 'R':
      current_node = network[current_node][1]
    if c == 'L':
      current_node = network[current_node][0]
    steps +=1
    print(current_node, c)
print(steps)
