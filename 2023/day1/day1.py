import numpy as np

def strToInt(str):
	tmp = ""
	for i in range(0,len(str)):
		for j in range(i,len(str)):
			if str[i].isdigit():
				tmp += str[i]
				break
			substr = str[i:j+1]		

			if substr == 'one':
				tmp+= '1'
			if substr == 'two':
				tmp+= '2'
			if substr == 'three':
				tmp+= '3'
			if substr == 'four':
				tmp+= '4'
			if substr == 'five':
				tmp+= '5'
			if substr == 'six':
				tmp+= '6'
			if substr == 'seven':
				tmp+= '7'
			if substr == 'eight':
				tmp+= '8'
			if substr == 'nine':
				tmp+= '9'
			if substr == 'zero':
				tmp+= '0'

	tmp2 = tmp[0] + tmp[len(tmp)-1]
	return tmp2

file = open('input', 'r')
Lines = file.readlines()
nums = np.empty(len(Lines))

for line in Lines:
	nums[Lines.index(line)] = int(strToInt(line))
	print(nums[Lines.index(line)])

print(np.sum(nums))