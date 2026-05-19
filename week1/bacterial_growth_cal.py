import math

def bacterial_growth_cal():
    p_o = float(input())
    t = float(input())
    d = float(input())
    p = p_o * math.pow(2, (d/t))
    return p

print(bacterial_growth_cal())