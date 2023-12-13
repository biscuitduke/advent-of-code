f = open('input', 'r').read()
Times = f.split('\n')[0].split(':')[1]
Times = int(Times.replace(' ', ''))
# Times = [int(x) for x in Times if x]
Times = [Times]
Distances = f.split('\n')[1].split(':')[1]
Distances = int(Distances.replace(' ', ''))
# Distances = [int(x) for x in Distances if x]
Distances = [Distances]

if len(Times) == len(Distances):
    race_num = len(Times)

power = 1
for i in range(race_num):
    max_time = 0
    min_time = 0
    wins = 0
    for time_button_is_pushed in range(Times[i], -1, -1):
        # print(time_button_is_pushed)
        speed = time_button_is_pushed
        time_traveled = Times[i] - time_button_is_pushed
        distance_traveled = speed * time_traveled
        if distance_traveled > Distances[i]:
            max_time = time_button_is_pushed
            # print(max_time)
            break
    for time_button_is_pushed in range(Times[i]):
        # print(time_button_is_pushed)
        speed = time_button_is_pushed
        time_traveled = Times[i] - time_button_is_pushed
        distance_traveled = speed * time_traveled
        if distance_traveled > Distances[i]:
            min_time = time_button_is_pushed
            # print(min_time)
            break
            
    
    power *= wins
print(max_time - min_time + 1)