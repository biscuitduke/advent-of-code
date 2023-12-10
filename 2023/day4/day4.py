import numpy as np
import math

f = np.loadtxt('input', dtype="U", delimiter=':')
f = np.loadtxt(f[:,1], dtype="U", delimiter='|')
winning_cards = np.char.split(f[:,0])
my_nums = (np.char.split(f[:,1]))

# total1 = np.zeros(len(my_nums))
total2 = np.zeros((len(my_nums)+1, len(my_nums)+1))
matches = np.zeros((len(my_nums)+1,1))
for i in range(1,len(my_nums)+1):
	matches[i] = len(np.intersect1d(winning_cards[i-1], my_nums[i-1]))
# 	if matches[i,0]:
# 		total1[i] = math.pow(2,matches[i,0]-1)

for i in range(1,len(my_nums)+1):
	for j in range(1,len(my_nums)+1):
		if i==j:
			total2[i,j] = total2[i,j-1] + 1
			total2[i+1:int(matches[i][0])+i+1,j] = 1#total2[i,j] + total2[i,j-1]
			total2[i,j:] = total2[i,j]
		elif total2[i,j] == 0:
			total2[i,j] = total2[i,j-1]
		elif total2[i,j] != 0:
			# total2[i,j:] = total2[i,j]
			total2[i,j] = total2[i,j-1] + total2[j,j]

print(np.sum(total2[:,j]))

# print(np.sum(total1))

