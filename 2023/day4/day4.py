import numpy as np
import math

f = np.loadtxt('input', dtype="U", delimiter=':')
f = np.loadtxt(f[:,1], dtype="U", delimiter='|')
winning_cards = np.char.split(f[:,0])
my_nums = (np.char.split(f[:,1]))

total = np.empty(len(my_nums))
for i in range(len(my_nums)):
	matches = len(np.intersect1d(winning_cards[i], my_nums[i]))
	if matches:
		total[i] = math.pow(2,matches-1)
	else:
		total[i] = 0
print(np.sum(total))