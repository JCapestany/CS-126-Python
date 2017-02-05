# Jose Capestany
# CS 126
# 2/17/2016
# HW 8

import math

def cost_trip(size,miles,gas,mileage):
    refill = math.ceil(miles / mileage)
    cost_gas = size * gas
    total_cost = cost_gas * refill
    return total_cost

size = int(input("Enter the size of the gas tank in gallons: "))
miles = int(input("Enter the length of the trip in miles: "))
gas = int(input("Enter the price per gallon in dollars: "))
mileage = int(input("Enter the mileage of the car: "))

print("The cost of the trip is", cost_trip(size,miles,gas,mileage),"dollars.")
