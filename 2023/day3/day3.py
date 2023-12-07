import re

special_characters = '!@#$%^&()_+[]{};:,/\|<>"-=`~'

file = open('input', 'r')
Lines = file.readlines()

line_length = len(Lines[0])-1
new_lineLength = line_length + 2

new_Lines = [None] * (len(Lines)+2)
new_Lines[0] = '.' + ('.' * line_length) + '.'
new_Lines[-1] = new_Lines[0]


for i in range(len(Lines)):
	string = Lines[i][:line_length]
	new_Lines[i+1] = '.' + string + '.'

total = 0
total_power = 0
for i in range(1,len(new_Lines)-1):
	prod = 1
	temp = re.findall(r'\d+', new_Lines[i])
	for num in temp:
		temp = re.search(r'\D' + num + r'\D', new_Lines[i])
		start = temp.start()+1
		end = temp.end()-1
		if (any(c in special_characters for c in new_Lines[i-1][start-1:end+1]) or 
			any(c in special_characters for c in new_Lines[i+1][start-1:end+1]) or
			any(c in special_characters for c in new_Lines[i][start-1:end+1])):
			total += int(new_Lines[i][start:end])

	for j in range(len(new_Lines[i])):
		prod = ""
		gear = 0
		power = 1
		if new_Lines[i][j] == '*':
			temp = re.finditer(r'\d+', new_Lines[i-1])
			for num in temp:
				if (num is not None) and (j in range(num.start()-1,num.end()+1)):
					gear += 1
					power *= int(new_Lines[i-1][num.start():num.end()])

			temp = re.finditer(r'\d+', new_Lines[i])
			for num in temp:
				if (num is not None) and (j in range(num.start()-1,num.end()+1)):
					gear += 1
					power *= int(new_Lines[i][num.start():num.end()])
			
			temp = re.finditer(r'\d+', new_Lines[i+1])
			for num in temp:
				if (num is not None) and (j in range(num.start()-1,num.end()+1)):
					gear += 1
					power *= int(new_Lines[i+1][num.start():num.end()])

			if gear == 2:
				print(prod)
				total_power += power



print(total_power)