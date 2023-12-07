file = open('input', 'r')
Lines = file.readlines()

maxdict = { "red" : 12, "green" : 13 , "blue" : 14}
game_sum = 0
total_power = 0

for line in Lines:
    thisdict = { "red" : 0, "green" : 0, "blue" : 0}
    string = line.split(':')
    game_num = string[0][5:len(string[0])]
    rounds = string[1].split(';')

    for rnd in rounds:
        rnd = rnd.split(',')

        for cube in rnd:
            offset = cube.find("red")
            if offset != -1 and int(cube[:offset]) > thisdict.get("red"):
                thisdict.update({"red" : int(cube[:offset])})

            offset = cube.find("green")
            if offset != -1 and int(cube[:offset]) > thisdict.get("green"):
                thisdict.update({"green" : int(cube[:offset])})

            offset = cube.find("blue")
            if offset != -1 and int(cube[:offset]) > thisdict.get("blue"):
                thisdict.update({"blue" : int(cube[:offset])})

    if thisdict.get("red") <= maxdict.get("red") and thisdict.get("green") <= maxdict.get("green") and thisdict.get("blue") <= maxdict.get("blue"):
        game_sum += int(game_num)

    power = thisdict.get("red") * thisdict.get("green") * thisdict.get("blue")
    total_power += power

print(game_sum)
print(total_power)
