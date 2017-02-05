# Jose Capestany
# CS126
# 2/2/2016
# HW4

'''
3-2
color = input("Enter a color: ")
color = color.lower()
comp_color = 0

if color == "red":
    comp_color = "green"
elif color == "green":
    comp_color = "red"
elif color == "yellow":
    comp_color = "violet"
elif color == "violet":
    comp_color = "yellow"
elif color == "blue":
    comp_color = "orange"
elif color == "orange":
    comp_color = "blue"
else:
    print("Not a valid input!")
if comp_color != 0:
    print("The complementary color is " + comp_color + ".")
'''

'''
3-4
integer = int(input("Enter an integer: "))

if (integer % 2) == 0:
    eo = "even."
elif (integer % 2) == 1:
    eo = "odd."

print("The integer" , integer , "is " + eo)
'''

'''
3-5
grade = int(input("Enter a grade: "))

if grade >= 90:
    letter = "A."
    an = 1
elif grade >= 80:
    letter = "B."
    an = 0
elif grade >= 70:
    letter = "C."
    an = 0
elif grade >= 60:
    letter = "D."
    an = 0
elif grade < 60:
    letter = "F."
    an = 1
    
if an == 0:
    print(grade,"gives you a " + letter)
elif an == 1:
    print(grade,"gives you an " + letter)
'''

'''
3-15
word = input("Enter a word: ")
word = word.lower()

if word[0] == "a":
    latin = word[:] + "yay"
elif word[0] == "i":
    latin = word[:] + "yay"
elif word[0] == "e":
    latin = word[:] + "yay"
elif word[0] == "o":
    latin = word[:] + "yay"
elif word[0] == "u":
    latin = word[:] + "yay"
else:
    latin = word[1:] + word[0] + "ay"

print(latin)
'''

'''
3-18
bill = float(input("Enter your bill: "))
service = input("What was the quality of service (poor, good, or excellent)? ")
service = service.lower()

if service == "poor":
    total = bill * 1.15
elif service == "good":
    total = bill * 1.2
elif service == "excellent":
    total = bill * 1.25

total = round(total , 2)
print("Your bill and tip will be $" , total , ".")
'''
