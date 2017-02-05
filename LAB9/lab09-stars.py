# Jose Capestany
# Kyle Sabin
# Lab 09 - Stars
# April 15, 2016

import turtle
turtle.tracer(0)


# line[0,1] x and y coordinates respectively
# all coordinates are between -1 and 1
# henry draper number line[3] (HD)
# magnitude line[4]
# name  line[6]

# HD: (x,y)
# HD: magnitude
# name: HD
# pack into tuple for returning


def read_coords(file):
    starsFileHandle = open(file, "r")
    starLines = starsFileHandle.readlines()
    counter = 0
    for line in starLines:
        line = line.strip()
        try:
            while counter < 6:
                line1 = line.split(" ")
                for string in line:

                    line1[counter] = float(string)
                    counter += 1

        except ValueError:
            pass
        counter = 0
    print(line1)
read_coords("stars.txt")