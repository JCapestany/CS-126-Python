# Jose Capestany and Kyler Begay
# CS126L
# 2/12/2016
# LAB3: Math Quiz

from random import randint

print("Choose difficulty:")
difficulty = input("BEGINNER, INTERMEDIATE, or ADVANCED: ").lower()

number = int(input("Choose # of questions: "))

correct = 0

if difficulty == "beginner":
    for i in range(number):
        p = randint(1, 2)
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        if p == 1:
            add = n1 + n2
            ans = int(input("%d + %d = " % (n1, n2)))
            if ans == add:
                print("CORRECT!")
                correct += 1
            else:
                print("INCORRECT!")
        elif p == 2:
            sub = n1 - n2
            ans = int(input("%d - %d = " % (n1, n2)))
            if ans == sub:
                print("CORRECT!")
                correct += 1
            else:
                print("INCORRECT!")
elif difficulty == "intermediate":
    for i in range(number):
        p = randint(1, 4)
        n1 = randint(1, 25)
        n2 = randint(1, 25)
        if p == 1:
            add = n1 + n2
            ans = int(input("%d + %d = " % (n1, n2)))
            if ans == add:
                print("CORRECT!")
                correct += 1
            else:
                print("INCORRECT!")
        elif p == 2:
            sub = n1 - n2
            ans = int(input("%d - %d = " % (n1, n2)))
            if ans == sub:
                print("CORRECT!")
                correct += 1
            else:
                print("INCORRECT!")
        elif p == 3:
            mult = n1 * n2
            ans = int(input("%d x %d = " % (n1, n2)))
            if ans == mult:
                print("CORRECT!")
                correct += 1
            else:
                print("INCORRECT!")
        elif p == 4:
            div = round(n1 / n2, 3)
            print("Round to 3 decimal places.")
            ans = float(input("%d / %d = " % (n1, n2)))
            if ans == div:
                print("CORRECT!")
                correct += 1
            else:
                print("INCORRECT!")
elif difficulty == "advanced":
    for i in range(number):
        p = randint(1, 5)
        n1 = randint(1, 100)
        n2 = randint(1, 100)
        n3 = randint(1, 100)
        if p == 1:
            one = n1 * n2 + n3
            ans = int(input("%d x %d + %d = " % (n1, n2, n3)))
            if ans == one:
                print("CORRECT!")
                correct += 1
            else:
                print("INCORRECT!")
        elif p == 2:
            two = n1 - n2 * n3
            ans = int(input("%d - %d x %d = " % (n1, n2, n3)))
            if ans == two:
                print("CORRECT!")
                correct += 1
            else:
                print("INCORRECT!")
        elif p == 3:
            three = round(n1 - n2 / n3, 3)
            print("Round to 3 decimal places.")
            ans = float(input("%d - %d / %d = " % (n1, n2, n3)))
            if ans == three:
                print("CORRECT!")
                correct += 1
            else:
                print("INCORRECT!")
        elif p == 4:
            four = n1 + n2 - n3
            ans = int(input("%d + %d - %d = " % (n1, n2, n3)))
            if ans == four:
                print("CORRECT!")
                correct += 1
            else:
                print("INCORRECT!")
        elif p == 5:
            five = round(n1 / n2 * n3, 3)
            print("Round to 3 decimal places.")
            ans = float(input("%d / %d x %d = " % (n1, n2, n3)))
            if ans == five:
                print("CORRECT!")
                correct += 1
            else:
                print("INCORRECT!")
print("\nYou got %d correct out of %d." % (correct, number))
if correct / number >= 2/3:
    print("Well done!")
elif correct / number >= 1/3:
    print("You need more practice!")
else:
    print("Please ask your math teacher for help!")
