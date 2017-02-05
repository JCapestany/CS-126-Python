starsFileHandle = open("stars.txt", "r")

starLines = starsFileHandle.readlines()
counter = 0
for line in starLines:
    line = line.strip()
    line1 = line.split(" ")
    # converts to a float if position is <=5
    while counter <= 5:
        line1[counter] = float(line1[counter])
        counter += 1
    counter = 0  # resets for the line, so that it doesn't skip block
    if len(line1) > 6:  # name block, will put names in a list
        for i in range(6, len(line1)):
            try:
                line1[6] += " " + line1[i+1]
            except IndexError:
                pass
            except TypeError:
                pass
        nameList = line1[6].split(";")
        for i in range(len(nameList)):
            nameList[i] = nameList[i].strip()
        line1[6] = nameList
    # THIS IS WHERE TO CONTINUE
    tuple = ({line1[3]: (line1[0],line1[1])}, {line1[3]: line1[4]}, )  # fix tuple
print(line1)
starsFileHandle.close()
