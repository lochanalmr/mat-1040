import math

def maximum_height_cal():
    u = float(input())
    a = 9.8
    v = 0.0
    s = (math.pow(u, 2) - math.pow(v, 2))  / (2 * a)
    return s

print(maximum_height_cal())