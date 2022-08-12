#1 Write an algorithm that reads a person's birth year,calculate and show the age you will complete in 2032.

bornDate = int(input("what year of your birth ?"))

futureAge = 2032 - bornDate

print("in the year 2032 you will have:", futureAge, "years")

#2 Make an algorithm that reads an integer and writes its successor and its predecessor.

integer = int(input("Type a number"))

successor = integer + 1

predecessor = integer - 1

print("the predecessor of your number is:", predecessor, "and the successor is:", successor)

#3 Build an algorithm that reads the salary value of a given employee and calculate how many minimum wages this employee earns.

salary = int(input("What s your salary ?"))

total = salary/1212

print("with your salary, you receive: ", total, "minimum salary")

#4 Make an algorithm that reads the diameter of a circle and calculates its area.
#all measurements in centimeters

diameter = float(input("How is the diameter os the circle ?"))

raio = diameter * 2
pi = 3.14
area = pi * (raio**2)

print("the area of the circle is:", area,"centimeter")

#5 Design an algorithm that reads the price of a product and then displays
#what are the amounts in: 3 installments with 5% interest, 2 installments without interest and
#the spot price with 5% discount.

productPrice = float(input("What s the price of the product ?"))

option1 = ((productPrice*0.05) + productPrice) / 3

option2 = productPrice/2

option3 = productPrice - (productPrice*0.05)

print("There are 3 forms of payment. "
      "The firts is 3 installments of:", option1,
      "the second is 2 installments of:", option2,
      "and the last is, cash:", option3)

#6 Write an algorithm that reads the value of two legs of a triangle rectangle and find the hypotenuse.

peccaryA = float(input("type the peccary A  of the triangle"))

peccaryB = float(input("type the peccary B  of the triangle"))

hypotenuseElevate = (peccaryA**2 + peccaryB**2)
import math
hypotenuse = math.sqrt(hypotenuseElevate)

print(hypotenuse)

#7 Write an algorithm that given a user-supplied time (hour,
#minutes and seconds), calculate total minutes and total seconds
#that have elapsed since the beginning of the day.

hour = int(input("What s the hour ?"))

minute = int(input("What s the exactly minute right now ?"))

second = int(input("What s the exactly second right now ?"))

totalMinutes = (hour * 60) + minute

totalSeconds = (totalMinutes * 60) + second

print("since started the day, we have:", totalMinutes, "minutes and", totalSeconds,"seconds" )

#8 Build an algorithm that calculates the number of paint cans
#needed and the cost to paint cylindrical fuel tanks, in
#which the height and radius of this cylinder are given. Knowing that:
#. A can of paint costs R$ 50.00;
#  B. Each can contains 5 liters;
#  C. Each liter of paint paints 3 square meters;
#  D. Inputs: height and radius;
#  E. Output: cost in R$ and quantity of cans.
# using square meters
height = float(input("what s the height of the cylinder ?"))

radius = float(input("what s the radius of the cylinder ?"))

pi = 3.14

aSide = (2 * pi * radius * height)

aBase = pi * (radius**2)

aTotal = (aSide + (2*aBase))

totalLiters = int(aTotal/3)

paintCans = int(totalLiters/5)

paintingCost = paintCans * 50

print("Knowing the measurements of this cylinder, we will spend:R$",paintingCost, "and", paintCans, "paint Cans")









