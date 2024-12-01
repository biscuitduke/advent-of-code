f = open('example', 'r').read()
Times = f.split('\n')[0].split(':')[1].split(' ')
Times = [int(x) for x in Times if x]
Distances = f.split('\n')[1].split(':')[1].split(' ')
Distances = [int(x) for x in Distances if x]

if len(Times) == len(Distances):
    race_num = len(Times)

power = 1
for i in range(race_num):
    wins = 0
    for time_button_is_pushed in range(Times[i]):
        speed = time_button_is_pushed
        time_traveled = Times[i] - time_button_is_pushed
        distance_traveled = speed * time_traveled
        if distance_traveled > Distances[i]:
            wins += 1
    power *= wins
print(power)