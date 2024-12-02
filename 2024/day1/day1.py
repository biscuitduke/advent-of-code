#!/usr/bin/env python3
# f = open('example', 'r').readlines()[0]
# f = ' '.join(f.split()).split()
# print(f)

f = open('input', 'r').readlines()
right_list = []
left_list = []

for l in f:
	right_list.append(int(' '.join(l.split()).split()[0]))
	left_list.append(int(' '.join(l.split()).split()[1]))

right_list = sorted(right_list, reverse=True)
left_list = sorted(left_list, reverse=True)

distances = [abs(a - b) for a, b in zip(right_list, left_list)]

print(sum(distances))

similarity_score = []

for i in left_list:
	similarity_score.append(i * right_list.count(i))

print(sum(similarity_score))