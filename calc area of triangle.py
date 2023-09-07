# remove the multy comment tags and comment the input lines for checking the predefined values
"""a = 20
b = 45
c = 48"""


a = float(input("enter the 1st side: "))
b = float(input("enter the 2st side: "))
c = float(input("enter the 3st side: "))

s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("the area of the triangle is %0.2f" % area)
