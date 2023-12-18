#!/usr/bin/python3
f = open('example', 'r')
total = 0
difference = []
for line in f.readlines()[:1]:
	history = [int(x) for x in reversed(line.replace('\n', '').split(' ')) if x.isdigit()]
	difference.append(history)
	# print(history)
	diff = []
	print(diff[0] !=0 , all(i != diff[0] for i in diff))
	while diff[0] !=0 and all(i != diff[0] for i in diff):
		for i in range(len(history)-1):
			diff.append(history[i]-history[i+1])
		difference.append(diff)
print(difference)