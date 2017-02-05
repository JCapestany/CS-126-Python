# Jose Capestany
# CS 126
# 2/9/2016
# HW 5

# 4-3
'''
x = float(input("Enter x for point (x,y): "))
y = float(input("Enter y for point (x,y): "))
b = float(input("Enter the y-intercept: "))

m = (y - b) / x

print("The slope of the line is:", m)
'''

# 4-9
'''
change = int(input("Enter amount of change(in cents): "))

dollar = change // 100

quarter = (change - 100 * dollar) // 25

dime = (change - 100 * dollar - 25 * quarter) // 10

nickel = (change - 100 * dollar - 25 * quarter - 10 * dime) // 5

penny = change - 100 * dollar - 25 * quarter - 10 * dime - 5 * nickel

print("Dollars: ",dollar)
print("Quarters:",quarter)
print("Dimes:   ",dime)
print("Nickels: ",nickel)
print("Pennies: ",penny)
'''

# 4-13
'''
date = input("Enter a date(yyyymmdd): ")

year = date[:4]

month = int(date[4:6])

if month == 1:
    month = "January"
elif month == 2:
    month = "February"
elif month == 3:
    month = "March"
elif month == 4:
    month = "April"
elif month == 5:
    month = "May"
elif month == 6:
    month = "June"
elif month == 7:
    month = "July"
elif month == 8:
    month = "August"
elif month == 9:
    month = "September"
elif month == 10:
    month = "October"
elif month == 11:
    month = "November"
elif month == 12:
    month = "December"

day = date[6:]

if day[0] == "0":
    day = date[8]

print(month,day,",",year)
'''

# 4-19
'''
h = int(input("Enter hours: "))
m = int(input("Enter minutes: "))
s = int(input("Enter seconds: "))

t = h + m / 60 + s / 3600
v = round(26.2188 / t, 3)

print("Your speed is", v, "mph.")
'''
