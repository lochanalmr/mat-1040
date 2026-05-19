import math

def area_of_circle(radius):
    return math.pi * math.pow(radius, 2)

radius = int(input())
print(area_of_circle(radius))