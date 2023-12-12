import numpy as np

f = open('example', 'r')
lines = f.read().split("\n\n")

seeds = lines[0].split(':')[1].split(" ")
seeds = [int(x) for x in seeds if x]

seed2soil = lines[1].split('\n')[1:]

soil2fertilizer = lines[2].split('\n')[1:]
fertilizer2water = lines[3].split('\n')[1:]
water2light = lines[4].split('\n')[1:]
light2temp = lines[5].split('\n')[1:]
temp2humidity = lines[6].split('\n')[1:]
humidity2loc = lines[7].split('\n')[1:]


maps = [seed2soil, soil2fertilizer, fertilizer2water, water2light, light2temp, temp2humidity, humidity2loc]
locations = np.zeros(0)
for source in seeds:
    for map in maps:
        for line in map:
            line = [int(x) for x in line.split(' ')]
            dest_range_start = line[0]
            src_range_start = line[1]
            range_len = line[2]
            if source in range(src_range_start, src_range_start+range_len):
                source = (source - src_range_start) + dest_range_start
                break
    locations = np.append(locations, [source])
print(np.min(locations))