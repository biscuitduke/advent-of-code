#!/usr/bin/env python3

f = open('example', 'r').readlines()
reports = []
unsafe_counter = 0

for l in f:
	reports.append(' '.join(l.split()).split())

for report in reports:
	diff = [abs(int(report[i]) - int(report[i + 1])) for i in range(len(report) - 1)]
	if any((1 > num) or (3 < num) for num in diff):
		unsafe_counter+=1
		continue
	elif any((int(report[i]) > int(report[i-1])) and (int(report[i]) > int(report[i+1])) for i in range(1,len(report)-1)):
		unsafe_counter+=1
		continue
	elif any((int(report[i]) < int(report[i-1])) and (int(report[i]) < int(report[i+1])) for i in range(1,len(report)-1)):
		unsafe_counter+=1
		continue

print(f"Part 1 solution - Safe reports: {len(reports) - unsafe_counter}")

unsafe_counter = 0
for report in reports:
	if len([i for i in range(1,len(report)-1) if (int(report[i]) > int(report[i-1])) and (int(report[i]) > int(report[i+1]))]) > 1:
		print(f"{report}: unsafe")
		unsafe_counter+=1
		continue
	elif len([i for i in range(1,len(report)-1) if (int(report[i]) < int(report[i-1])) and (int(report[i]) < int(report[i+1]))]) > 1:
		print(f"{report}: unsafe")
		unsafe_counter+=1
		continue

print(f"Part 2 solution - Safe reports: {len(reports) - unsafe_counter}")