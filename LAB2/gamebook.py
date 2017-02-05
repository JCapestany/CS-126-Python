# Jose Capestany and Adam Douglass
# CS126L
# 2/5/2016
# Lab2: Game Book

success_mountains = '''You eventually come across a mountain town.
The citizens offer you a ride home.
You finally escape the woods.
YOU SURVIVED THE WOODS!'''

success_river = '''You keep moving on and encounter a forest ranger cabin.
The rangers help you return home.
YOU SURVIVED THE WOODS!'''

print("Game Book: Survive the woods!")
print("=============================")
print("You decide to go hunting.")
print("What type of weapon do you bring?")

weapon = input("SHOTGUN, BOW, or RIFLE: ").lower()  # Three choices

print("You become lost in the woods and you do not know where you are going.")
print("You come across a fork in the woods.")
print("To the left you see a river and the right heads toward the mountains.")
print("Which way do you go?")

fork = input("RIGHT or LEFT: ").lower()

if fork == "right":
    print("On the way towards the mountains you spot a bear in your path.")
    print("The bear notices you and starts approaching.")
    print("What do you do?")

    bear = input("RUN, NOTHING, APPROACH: ").lower()  # Three choices

    if bear == "run":
        print("The bear starts chasing you.")
        print("It catches you and mauls you to pieces.")
        print("YOU DIED!")
    elif bear == "nothing":
        print("The bear continues to approach you.")
        print("What do you do?")

        nothing = input("FIRE or NOTHING: ").lower()

        if nothing == "fire":
            if weapon == "shotgun":
                print("You fire your shotgun but miss the bear.")
                print("The bear comes after you and kills you.")
                print("YOU DIED!")
            elif weapon == "bow":
                print("You hit the bear with your arrow.")
                print("The now angry bear chases you and catches you.")
                print("You are shredded to pieces.")
                print("YOU DIED!")
            elif weapon == "rifle":
                print("You fire your rifle.")
                print("You hit the bear square in the eyes.")
                print("The bear drops dead and you proceed past its corpse.")
                print(success_mountains)
        elif nothing == "nothing":
            print("The bear stops and leaves the trail after a few seconds.")
            print("You move on ahead.")
            print(success_mountains)
    elif bear == "approach":
        print("The bear takes this as a sign of aggression.")
        print("The bear starts running towards you.")
        print("What do you do?")

        approach = input("NOTHING or FIRE: ").lower()

        if approach == "nothing":
            print("The bear kills you.")
            print("YOU DIED!")
        elif approach == "fire":
            if weapon == "bow":
                print("You fire your bow.")
                print("The bear isn't fazed.")
                print("It reaches you and shreds you to pieces.")
                print("YOU DIED!")
            elif weapon == "rifle":
                print("You fire your rifle.")
                print("You hit the bear in its shoulder.")
                print("However, it continues running towards you.")
                print("It reaches you and swipes you.")
                print("YOU DIED!")
            elif weapon == "shotgun":
                print("You fire your shotgun.")
                print("The bear stops dead in its tracks and falls over dead.")
                print("You move on ahead.")
                print(success_mountains)
elif fork == "left":
    print("You reach the bank of the river.")
    print("The river seems crossable.")
    print("Do you cross the river?")

    river = input("YES or NO: ").lower()

    if river == "no":
        print("You head downstream of the river.")
        print("Another hunter mistakes you for a deer and fires at you.")
        print("The shot kills you instantly.")
        print("YOU DIED!")
    elif river == "yes":
        print("You managed to cross the river.")
        print("You are exhausted and decide to take a break.")
        print("How long is your break?")

        rest = float(input("LENGTH OF BREAK IN MINUTES: "))
        # Numerical comparison

        if rest >= 60:
            print("You take a nice long break.")
            print(success_river)
        elif rest >= 10:
            print("You take a break.")
            print("You keep moving on ahead and encounter a bobcat.")
            print("What do you do?")

            bobcat = input("RUN or FIRE: ").lower()

            if bobcat == "run":
                print("The bobcat chases you and bites you in the throat.")
                print("YOU DIED!")
            elif bobcat == "fire":
                if weapon == "bow":
                    print("You fire your bow.")
                    print("You hit the bobcat in its throat.")
                    print(success_river)
                elif weapon == "shotgun" or weapon == "rifle":
                    print("You can't fire your weapon because it is wet.")
                    print("The bobcat pounces and bites you in the throat.")
                    print("YOU DIED!")
        elif rest < 10:
            print("You take a short break.")
            print("You keep moving on ahead and encounter a bobcat.")
            print("What do you do?")

            bobcat = input("RUN or FIRE: ").lower()

            if bobcat == "run":
                print("The bobcat chases you and bites you in the throat.")
                print("YOU DIED!")
            elif bobcat == "fire":
                if weapon == "bow":
                    print("You fire your bow.")
                    print("Your exhaustion causes you to miss.")
                    print("The bobcat pounces and bites you in the throat.")
                    print("YOU DIED!")
                elif weapon == "shotgun" or weapon == "rifle":
                    print("You can't fire your weapon because it is wet.")
                    print("The bobcat pounces and bites you in the throat.")
                    print("YOU DIED!")
